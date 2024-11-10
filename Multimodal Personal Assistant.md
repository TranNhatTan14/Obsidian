# Process RAW data with TEMPLATE (created with prompt)

- [ ] Prompt for vocabulary

- [ ] Learn how to create chatbot use ChatGPT API
- [ ] Use custom model with chatbot
- [ ] Make people can work with chatbot

> [!important]
> Mục đích của Chatbot này vừa là để cho như công việc của mình bên GeneStory về xây dựng Chatbot, học thêm kiến thức cần thiết, và cũng là để xây dựng công cụ giúp bản thân mình

# Requirements

- Host in Cloud and access with API

# ChatGPT Next Web

ChatGPT Next Web is a versatile open-source application that uses OpenAI and Google AI API to access 

The tool is like ChatGPT

https://www.datacamp.com/tutorial/introduction-to-chatgpt-next-web-nextchat
https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web
## Functions

- Summarization content (video, document)
- Mentor (help me learn language, vocabulary, prepared for IELTS)
- Chatbot can chat with me in voice like ChatGPT

![[Pasted image 20240729135543.png]]

The model only has knowledge of the content that was in the training data.

People often try to add new knowledge without pre-training, focus on fine-tuning the model with smaller datasets. However, this doesn't work in every situation, especially if the new knowledge is not well represented in the base model.

LLM have two phases of training:

# Pre-training

> [!tip] Pre-training is like Reading

I'd like to reiterate that pre-training large models of large datasets is an expensive activity, with a minimum cost of maybe about $1,000 for the smallest models, up to $1,000,000 for a billion parameter scale model.

### Use cases

When pre-training a model is the best option to get the good performance.

Discuss the difference between pre-training and fine-tuning

Pre-training a large language model is a process of taking model, and train it on a large corpus of text using supervised learning.

The output of pre-training is known as a base model.

Training from scrath (randomly initialized weights) is computationally expensive, requiring multiple SOTA GPUs and training runs that can last weeks or months

###### Auto-Regressive text generation

###### Training on model that's already been pre-trained and continuing the pre-training process on our own data.

Building models for tasks in specific domains like legal, healthcare, and e-commerce
Other need models with stronger abilities in specific languages such as Vietnamese or Chinese.

Further, new training methods are making more efficient pre-training possible like 

###### Depth Upscaling

Uses two or more sets of existing models to build larger models
Create new, larger model by duplicating layers of a smaller pre-trained model.
Model created in this way can be pre-trained with up to 70% less compute than traditional pre-training, representing a large cost saving.

###### Gathering and preparing training data

![[Pasted image 20240729141836.png]]

Step to obtain high quality training data, including deduplication, filtering on the length of text example, and language cleaning

Dataverse is ready to use data cleaning pipeline.

### Data Cleaning

Parquet is a columnar storage file format that widely used in Big Data and data analytics scerarios.

### Prepare data for training (Data Manipulation)

Package training data so that can be used in Hugging Face

Tokenizing the data and then packing it

Tokenization is the step that transforms text data into numbers. Related with vocabulary and tokenization algorithm of model

![[Pasted image 20240729143305.png]]

The addition of special tokens
Reshapeing make training much more efficient.


```python
# Tokenizing and creating input_ids
import datasets

dataset = datasets.load_dataset(
	"parquet",
	data_files="file_path",
	split="train"
)

dataset = dataset.shard(num_shards=10, index=0)

from transformers import AutoTokenizer

model_path_or_name = "upstage/SOLAR-10.7B-v1.0"

tokenizer = AutoTokenizer.from_pretrained(
	model_path_or_name,
	use_fast=False # If True, AutoTokenizer use a tokenizer implemented in Rust, which operates in parallel and faster
)

tokenizer.tokenizer("I'm a short sentence")
# ['▁I', "'", 'm', '▁a', '▁short', '▁sentence']
```


```python
def tokenization(example):
	# Tokenize
	tokens = tokenizer.tokenizer(example["text"])

	# Convert token to ids
	token_ids = tokenizer.convert_tokens_to_ids(tokens)

	# Add <BOS> and <EOS> tokens
	token_ids = [
		tokenizer.bos_token_id] \
		+ token_ids \
		+ [tokenizer.eos_token_id
	]

	example["input_ids"] = token_ids
	example["num_tokens"] = len(token_ids)

	return example

dataset = dataset.map(tokenization, load_from_cache_file=False)
```

### Packing the data

![[Pasted image 20240729143718.png]]

```python
input_ids = np.concatenate(dataset["input_ids"])

print(len(input_ids))
# 5113663

# Max sequence length, longer length if device have enough memory. 
# Llama-2 uses 4096
max_seq_length = 32

total_length = len(input_ids) - len(input_ids) % max_seq_length
input_ids = input_ids[:total_length]
# Shape (5113632,)

# Reshape input IDs
input_ids_reshaped(-1, max_seq_length).astype(np.int32)
# Shape (159801, 32)

# Transforming input IDs to a list
input_ids_list = input_ids_reshaped.to_list()

# Convert to Hugging Face dataset
packed_pretrain_dataset = datasets.Dataset.from_dict(
	{"input_ids": input_ids_list}
)

print(packed_pretrain_dataset)

# Dataset({
#     features: ['input_ids'],
#     num_rows: 159801
# })

# Save to parquet file to use later
packed_pretrain_dataset.to_parquet("file_path")
```

### Configuring model architecture

Modify Meta's Llama models to create larger or smaller models and then look at a few options for initializing weights, either randomly or from other models

### Model configuration

### Training

Need more memory to training models than you do for inference. The extra memory is needed to store the gradient and then activations that get updated during the training process.

![[Pasted image 20240729203808.png]]

You can use [Training Cluster](https://huggingface.co/training-cluster) to check how much your training job cost before you get started

```python
import torch
from transformers import AutoModeForCausalLM

pretrained_model = AutoModeForCausalLM.from_pretrained(
   "../model",
   device_map="auto",
   torch_dtype=torch.bfloat16,
   use_cache=False
)

# Load dataset
class CustomDataset(Dataset):
	def __init__(self, args, split="train"):
		self.args = args
		self.dataset = datasets.load_dataset(
			"parquet",
			data_files=args.dataset_name,
			split=split
		)

	def __len__(self):
		return len(self.dataset)

	def __getitem__(self, index):
		# Convert the lists to a LongTensor for PyTorch
		input_ids = torch.LongTensor(self.dataset[index]["input_ids"])
		labels = torch.LongTensor(self.dataset[index]["input_ids"])

		# Return the sample as a dictionary
		return {"input_ids": input_ids, "labels": labels}

# Configure Training Arguments

```

We are setting labels equal to input IDs here because we want to perform next token prediction. Then Llama for causal LM will shift labels internally to create multiple input output pairs for supervised learning.

A rule of thumb is to maximize batch size given the memory capacity of your training device. If you have 8 GPUs available, you will process 8 times the batch size, resulting in 512 tokens per training step.

```python
import transformers
from dataclasses import dataclass, field

@dataclass
class CustomArguments(transformers.TrainingArguments):
    dataset_name: str = field(default="./parquet/packaged_pretrain_dataset.parquet")
    num_proc: int = field(default=1)                     # Number of subprocesses for data preprocessing
    max_seq_length: int = field(default=32)              # Maximum sequence length

    # Core training configurations
    seed: int = field(default=0)                         # Random seed for initialization, ensuring reproducibility
    optim: str = field(default="adamw_torch")            # Optimizer, here it's AdamW implemented in PyTorch
    max_steps: int = field(default=30)                   # Number of maximum training steps
    per_device_train_batch_size: int = field(default=2)  # Batch size per device during training

    # Other training configurations
    learning_rate: float = field(default=5e-5)           # Initial learning rate for the optimizer
    weight_decay: float = field(default=0)               # Weight decay
    warmup_steps: int = field(default=10)                # Number of steps for the learning rate warmup phase
    lr_scheduler_type: str = field(default="linear")     # Type of learning rate scheduler
    gradient_checkpointing: bool = field(default=True)   # Enable gradient checkpointing to save memory
    dataloader_num_workers: int = field(default=2)       # Number of subprocesses for data loading
    bf16: bool = field(default=True)                     # Use bfloat16 precision for training on supported hardware
    gradient_accumulation_steps: int = field(default=1)  # Number of steps to accumulate gradients before updating model weights
    
    # Logging configuration
    logging_steps: int = field(default=3)                # Frequency of logging training information
    report_to: str = field(default="none")               # Destination for logging (e.g., WandB, TensorBoard)

    # Saving configuration
    save_strategy: str = field(default="steps")          # Can be replaced with "epoch"
    save_steps: int = field(default=3)                   # Frequency of saving training checkpoint
    save_total_limit: int = field(default=2)             # The total number of checkpoints to be saved
```

###### Configure Training Arguments

Choosing parameters for LLM can be challenging and often involves significant research. Because training LLM is  a costly process and typically does not allow for much trial and error

###### Run the trainer and monitor the loss

Normally you would pre-train a model for weeks if ot months. Note that we don't slack off during training.  We would record the losses with weights and biases, which allow team to check the progress at any time. See [Evaluating and Debugging Generative AI Models Using Weights and Biases](https://www.deeplearning.ai/short-courses/evaluating-debugging-generative-ai) for more details.

```python
from transformers import Trainer, TrainingArguments, TrainerCallback

# Define a custom callback to log the loss values
class LossLoggingCallback(TrainerCallback):
	def on_log(self, args, state, control, logs=None, **kwargs):
		if logs is not None:
			self.logs.append(logs)

	def __init__(self):
		self.logs = []

# Initialize the callback
loss_logging_callback = LossLoggingCallback()

# Trainer
trainer = Trainer(
	model=pretrained_model,
	args=args,
	train_dataset=train_dataset,
	eval_dataset=None
	callbacks=[loss_logging_callback]
)

trainer.train()
```

### Checkpoint

We would also create checkpoints or an intermediate version of the model 

```python
from transformers import Trainer, TrainingArguments, TrainerCallback

# Saving the configuration
save_strategy: str = field(default="steps")
save_steps: int = field(default=3)
save_total_limit: int = field(default=2)
```

Check the model after 1000 steps

```python
from transformers import AutoTokenizer, TextStreamer, AutoModelForCausalLM

tokenizer_path = "upstage/TinySolar-248m-4k"

tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

model_1000_path = "output/checkpoint-1000"

model_1000 = AutoModelForCausalLM.from_pretrained(
	model_1000_path,
	device_map="auto",
	torch_dtype=torch.bfloat16
)

prompt = "I am an Mechatronics Engineer. I love"

inputs = tokenizer(prompt return_tensors="pt").to(model_1000.device)

streamer = TextStreamer(
	tokenizer,
	skip_prompt=True,
	skip_special_tokens=True
)

output = mdel_1000.generate(
	**inputs,
	streamer=streamer,
	use_cache=True,
	max_new_token=64,
	do_sample,
	temperature=1.0
)
```

Using open source Hugging Face library

This course use smaller models with just a few of million parameters

Can use to scale to both larger datasets, and models, and also train on GPUs


- Gain in-depth knowledge of the steps to pretrain an LLM, encompassing all the steps, from data preparation, to model configuration and performance assessment.
- Explore various options for configuring your model’s architecture, including modifying Meta’s Llama models to create larger or smaller versions and initializing weights either randomly or from other models.
- Learn innovative pretraining techniques like Depth Upscaling, which can reduce training costs by up to 70%.

Training large language models using a technique called pretraining. You’ll learn the essential steps to pretrain an LLM

understand the associated costs, and discover how starting with smaller, existing open source models can be more cost-effective.

Pretraining involves teaching an LLM to predict the next token using vast text datasets, resulting in a base model, and this base model requires further fine-tuning for optimal performance and safety.

Pretrain a model from scratch and also to take a model that’s already been pretrained and continue the pretraining process on your own data. 

In detail: 

- Explore scenarios where pretraining is the optimal choice for model performance. Compare text generation across different versions of the same model to understand the performance differences between base, fine-tuned, and specialized pre-trained models.
- Learn how to create a high-quality training dataset using web text and existing datasets, which is crucial for effective model pretraining.
- Prepare your cleaned dataset for training. Learn how to package your training data for use with the Hugging Face library.
- Explore ways to configure and initialize a model for training and see how these choices impact the speed of pretraining.
- Learn how to configure and execute a training run, enabling you to train your own model.
- Learn how to assess your trained model’s performance and explore common evaluation strategies for LLMs, including important benchmark tasks used to compare different models’ performance.

After taking this course, you’ll be equipped with the skills to pretrain a model—from data preparation and model configuration to performance evaluation.

[Pretraining LLMs](https://www.deeplearning.ai/short-courses/pretraining-llms)

### Fine-tuning

> [!tip] Fine-tuning is like a Practice Exam
> The data used for fine-tuning is highly structured like Q&A pairs, instruction reponse pairs.

![[Pasted image 20240729141544.png]]

Tune a model to a particular task. For chat model, that task is to be conversational.

LLMs are trained on publically available data for general use cases. If your application requires unique knowledge, like a profession-specific vocabulary or a distinct personality, you may turn to fine-tuning to accomplish this.

[Finetuning Large Language Models](https://www.deeplearning.ai/short-courses/finetuning-large-language-models)

[Prompt Compression and Query Optimization](https://www.deeplearning.ai/short-courses/prompt-compression-and-query-optimization)

### Serving LLM

https://www.deeplearning.ai/courses/generative-ai-with-llms/

[Efficiently Serving LLMs](https://www.deeplearning.ai/short-courses/efficiently-serving-llms)

LLM-service services provide the GPUs needed for training and hosting. 

Techniques used to serve LLMs efficiently.
LoRa – Low Rank Adaption, a parameter-efficient approach to fine-tuning as well as quantization – a means of reducing the memory used by your model.

###### Memory

LLM does not have a memory beyond what is presented in a prompt. To remember the turns of a conversation, you can add memory

###### Guardrails

Use chatbot in production, it should be monitored to ensure safe, non-toxic conversation.

###### Quantization 

[Introduction to On-Device AI](https://www.deeplearning.ai/short-courses/introduction-to-on-device-ai)
https://www.deeplearning.ai/short-courses/quantization-in-depth/
https://www.deeplearning.ai/short-courses/quantization-fundamentals-with-hugging-face/

### Retrieval Augmented Generation

RAG over documents has two phases:

1. The documents are processed and installed in a database, often a vector database.
2. Retrieving the data

![800](https://wordpress.deeplearning.ai/wp-content/uploads/2024/05/Rag-Pipeline-2024-05-08-1002.png)

###### Extract

Documents come in all sorts of file formats (.doc, .pdf, etc.) and contain all sorts of data formats (text, tables, images, movies). These must be extracted and put into a format that can be processed by the next stages. Ingesting data from many sources and formats and preparing them for embedding.

[Preprocessing Unstructured Data for LLM Applications](https://www.deeplearning.ai/short-courses/preprocessing-unstructured-data-for-llm-applications)

###### Chunking

Text data is broken into smaller chunks – a process inventively named ‘chunking’

###### Embedding

Converting a chunk into a ‘**dense vector**’ that represents the meaning of the text. 

[Large Language Models with Semantic Search](https://www.deeplearning.ai/short-courses/large-language-models-semantic-search)

[Understanding and Applying Text Embeddings](https://www.deeplearning.ai/short-courses/google-cloud-vertex-ai)

###### Loading

Adding the embedding and original data to a database.

## Database

### Relation database

### Vector database

The database is going to provide storage for the embedding and data. Often these are **vector databases** due to the embedding, but **graph databases** and traditional databases are also used.

[Vector Databases: from Embeddings to Applications](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications)

- How vector database work
- Approximate Nearest Neighbor (ANN) algorithm used in many vector databases
- Hierarchical Navigable Small World, or HNSW

### Graph database

[Knowledge Graphs for RAG](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag)

This course demonstrates RAG applications using the Neo4j graph database which stores objects and their relationships. 

### Query

###### Embedding

The query is converted to a dense vector using the same embedding model.

###### Retrieval

The stored and query vectors represent meaning, so retrieval is the process of finding the k entries in the database that are ‘closest’ to the query vector. k results are provided to an LLM which uses them to form an ‘augmented’ response.

[Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai)

### Agent

###### LangChain

[Functions, Tools and Agents with LangChain](https://www.deeplearning.ai/short-courses/functions-tools-agents-langchain)

Use OpenAI function calling. You then create tools using LangChain. 
uilding a conversational agent, is not required. You will learn that in the Agent Courses below.

Build a RAG pipeline

###### LlamaIndex

Implement an agentic version of RAG

### Summary the PDF

The agent can help me to summary the PDF research paper like [Typeset](Tools.md#Typeset) and summary the research news like [Emergent Mind](https://www.emergentmind.com)

### List of agents

- [AI Agentic Design Patterns with Autogen](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/): Autogen is an agentic framework that specializes in agentic tasks. This course provides multiple project examples: Customer Onboarding, Blog-post writing, Tool Use (important for a research agent), Financial Analysis, and Report generation.
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/): Crew is a multi-agent framework. This course shows you how to build many projects including a research agent described in lesson 3.
- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/): LangGraph allows you to build your own agentic dataflows. It is a bit more effort than a purely agentic framework but allows you fine-grain control of dataflows. This course covers tool use and finishes by building a research agent. It uses Tavily, a search engine built for agents.
- [Building Agentic RAG with LlamaIndex](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/): This course builds a RAG research agent that can be used to research local documents. LlamaIndex also supports tools like Serper and Tavily to add web search.
- Research Agent
- [Building Your Own Database Agent](https://www.deeplearning.ai/short-courses/building-your-own-database-agent)

https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/

### Pipeline

- Set up private Github and sign-in option for website
- Build GUI with [Quartz](https://quartz.jzhao.xyz)
- Build LLM agents with API
	- Summarizing (e.g., summarizing user reviews for brevity)
	- Inferring (e.g., sentiment classification, topic extraction)
	- Transforming text (e.g., translation, spelling & grammar correction)
	- Expanding (e.g., automatically writing emails)
- Knowledge database idea from [Recall](https://www.getrecall.ai)
	- Graph or vector database
	- Auto summarize
	- Automatic connections
	- Auto categorized based on what it mentions
	- Data export
- Review with space repitition
- Agent
	- When have new word from image or text, extract vocabulary and save to database
	- Report
		- To do list
		- Work process
	- RAG and generate output
	- Help me to analysis based on my data like habit checker, website visit and recommend help
- Scale up and MMO
	- Deploy in Cloud
	- Chrome extension
	- Application

### [Host AI locally](https://www.youtube.com/watch?v=Wjrdr0NU4Sk)

- Visualize and Interactive with me like pesonal assistant
- Like database for me
- Tính đóng gói có thể truy cập được từ nhiều nơi mà không cần cài đặt gì nhiều
- Tạo template use for guest
- Có thể đứng trên vai người khổng lồ (sử dụng những tiến bộ khoa học, nền tảng lớn)

### Database

**Types of data and data format**

- Text
- Image
- GIF
- Audio
- Video
- Object

**How to store data in database**

- Raw
- Base64
- JSON
- Vector

### Inspiration

Website

- [Pelayo Arbués](https://www.pelayoarbues.com/)
- [A Pattern Language](https://patternlanguage.cc/)
- [Pedro](https://www.pmcf.xyz/topo-da-mente/)
- [Quart](https://quartz.jzhao.xyz/)

[Khoj](https://github.com/khoj-ai/khoj)

- Chat
- Agents
- Automate
    - Automations allow you to schedule smart reminders
    - **Market summary**: Get the market summary for today and share it with me. Focus on tech stocks and the S&P 500.
    - **Front Page of Hacker News**: Summarize the top 5 posts from [https://news.ycombinator.com/best](https://news.ycombinator.com/best) and share them with me, including links

### Chatbot

Basic of an LLM
How to prompt?
The difference between a pre-trained and fine-tuned model

Build a chatbot from scratch and have GUI

Langchain

Make a project more robust by providing things like LLM independence, retry logic, tracing, and other features
# References

- [Open Source Models with Hugging Face](https://www.deeplearning.ai/short-courses/open-source-models-hugging-face)
- Meta Llama 3, LLaMA 2
- [Prompt Engineering with Llama 2 & 3](https://www.deeplearning.ai/short-courses/prompt-engineering-with-llama-2)
- Mistral AI
- [Getting Started with Mistral](https://www.deeplearning.ai/short-courses/getting-started-with-mistral)
- GPT-2, BLOOM, Grok.AI, Falcon, BERT
- https://cloud.google.com/blog/products/ai-machine-learning/rag-with-bigquery-and-langchain-in-cloud

Build a personal assistant to enhance various aspects of your life. A well-designed personal assistant can significantly improve your productivity, learning, and overall quality of life. Here are some key areas where a personal assistant can help:

1. Learning and Knowledge Management:

- Track your learning progress across different subjects
- ==Recommend relevant resources (books, articles, courses) based on your interests==
- ==Create flashcards and quizzes for spaced repetition learning== - Connect data with model, it will automatically create flashcard
- Summarize complex information for quick review

2. Productivity and Work Management:

- Manage your to-do lists and prioritize tasks
- Set reminders for deadlines and important events
- Automate repetitive tasks and workflows
- Organize and categorize your digital files and emails

3. Personal Development:

- ==Track your goals and habits==
- Provide daily motivational content or affirmations - [[Motivation]] application in App Store
- Suggest personalized self-improvement activities
- Monitor your progress on various skills or objectives

4. Health and Wellness:

- Track your exercise, sleep, and nutrition
- Provide personalized workout plans and meal suggestions
- Remind you to take breaks and practice mindfulness
- Monitor your mood and suggest stress-reduction techniques

5. Time Management:

- Analyze how you spend your time and suggest optimizations
- Schedule your day efficiently, considering your energy levels and preferences
- Manage your calendar and coordinate meetings

6. Financial Management:

- Track your expenses and income
- Provide budget recommendations and financial insights
- Alert you to bill due dates and unusual spending patterns

7. Information Filtering:

- Curate news and content based on your interests
- Summarize lengthy articles or reports
- Filter and prioritize your emails and messages

8. Decision Support:

- Provide pros and cons for important decisions
- Offer data-driven insights to support your choices
- Suggest alternatives you might not have considered

9. Creativity and Brainstorming:

- Generate ideas for projects or problem-solving
- Provide writing prompts or creative exercises
- Offer constructive feedback on your creative work

10. Social and Networking:

- Remind you to keep in touch with important contacts
- Suggest networking opportunities aligned with your goals
- Help prepare for meetings or social events

To build such a personal assistant, you'd need to consider:

1. Data integration: Connecting to various apps and services you use
2. Natural language processing: For easy interaction
3. Machine learning: To personalize recommendations and insights
4. Privacy and security: To protect your personal information
5. User interface: For seamless interaction across devices


# Goal

- Build with S.M.A.R.T mean build specific like application to learn language

# Expectation

- First will be application help me to build "data" like Obsidian, or smaller like Obsidian plugins
- Summary what you learn in yesterday, this weekend based on what you note or input

# Model

- Most effective way for finance is use opensource model to reduce cost, but it require knowledge

# Input


# Functions

- Natual Language Processing for interaction
- Machine Learning to personalize recommendations and insights
- Help me learn (language, skills, knowledge) as an assistant with feedback
- Extract information in days, weeks, months based on update file or query
- Can help me when working with project, like SQL can do with various file
# Output

- Interfaces people can interact with, input is (text, voice) in website or smartphone applications.
- Tối ưu chi phí bằng việc giới hạn đầu vào và đầu ra để không tính phí nhiều

# Obsidian-Copilot: An Assistant for Writing & Reflecting

https://eugeneyan.com/writing/obsidian-copilot


- Sử dụng API hoặc sử dụng Subscription
	- Sử dụng API thì pay as you go và có thể sử dụng nhiều mô hình

# Finance

https://learnen.io


https://eugeneyan.com/writing/llm-ux
https://eugeneyan.com/writing/obsidian-copilot

- Giúp mình take note hiệu quả hơn, có thể kiếm tiền từ đây, vừa có kiến thức cũng như dự án #Finance #Knowledge #Work 