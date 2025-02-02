---
aliases:
  - LLM
---
==We will not train LLM, we will finetuning instead==

# Tactical

Practices for prompt, RAG, flow engineering, evals and monitoring

# Strategic

- Find and filter open source models on Hugging Face Hub based on task, rankings, and memory requirements.
- Using the transformers library to perform text, audio, image, and multimodal tasks.
- Easily share your AI apps with a user-friendly interface or via API and run them on the cloud using Gradio and Hugging Face Spaces.

The availability of models and their weights for anyone to download enables a broader range of developers to innovate and create.

In this course, you’ll select open source models from Hugging Face Hub to perform NLP, audio, image and multimodal tasks using the Hugging Face transformers library. Easily package your code into a user-friendly app that you can run on the cloud using Gradio and Hugging Face Spaces.

You will:

- Use the transformers library to turn a small language model into a chatbot capable of multi-turn conversations to answer follow-up questions.
- Translate between languages, summarize documents, and measure the similarity between two pieces of text, which can be used for search and retrieval.
- Convert audio to text with Automatic Speech Recognition (ASR), and convert text to audio using Text to Speech (TTS).
- Perform zero-shot audio classification, to classify audio without fine-tuning the model.
- Generate an audio narration describing an image by combining object detection and text-to-speech models.  
- Identify objects or regions in an image by prompting a zero-shot image segmentation model with points to identify the object that you want to select.
- Implement visual question answering, image search, image captioning and other multimodal tasks.
- Share your AI app using Gradio and Hugging Face Spaces to run your applications in a user-friendly interface on the cloud or as an API. 

The course will provide you with the building blocks that you can combine into a pipeline to build your AI-enabled applications!


Rule of thumb that I use to estimate how much memory I will need for a model

Go to FIle and versions - Find "pytorch_model.bin"

Load model from Transformer library with both use a pipeline as a high-level helper or load model directly

When working with large-scale AI and large language models (LLMs), several factors are critical:

# Data

# Computational Resources

- From server from work
- Free GPU from Kaggle and Google Colab
- Free GPU from Github pack
- Hugging Face

1. Colab Pro - 10 USD/mo with faster GPUs. You can ssh via VSCode to it and treat it like a local machine.
2. GCP 300 USD Free credit Will last a few months.
3. Azure 300 USD? (or 150 USD) free credit if you're a student.
4. E mail paperspace, (there's one more that I forget, but that's extremely cheap, just google) and tell you're a student and ask for discounts.

# Model Architecture

# Optimization and Scaling

---

https://developers.google.com/machine-learning/resources/intro-llms
https://aws.amazon.com/what-is/large-language-model
https://medium.com/data-science-at-microsoft
https://medium.com/data-science-at-microsoft/how-large-language-models-work-91c362f5b78f

# Transformers

# Self-attention