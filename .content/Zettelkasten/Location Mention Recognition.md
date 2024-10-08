---
tags: 
links:
  - "[[Competition]]"
  - "[[Microsoft]]"
---
https://huggingface.co/adambuttrick/ner-test-bert-base-uncased-finetuned-500K-AdamW-3-epoch-locations/tree/main

219 sample don't have location

### Resource

[Flair Github](https://github.com/flairnlp/flair)

[1st place solution for GeoAI Challege Location Mention Recognition from Social Media in Zindi](https://github.com/moadel2002/Location-Mention-Recognition)

https://huggingface.co/blog/stefan-it/autotrain-flair-mobie

###### [Microsoft Learn Location Mention Recognition Challenge](https://zindi.africa/competitions/microsoft-learn-location-mention-recognition-challenge)

###### [2022 ITU GeoAI Location Mention Recognition Challenge Finale](https://aiforgood.itu.int/event/2022-itu-geoai-location-mention-recognition-challenge-finale/)

Record video: https://www.youtube.com/watch?v=AJadU-y2fYg

https://www.youtube.com/watch?v=kYlw_CClBAM

###### Model

https://huggingface.co/docs/transformers/en/tasks/token_classification

https://huggingface.co/tasks/token-classification
https://huggingface.co/dslim/bert-base-NER
https://huggingface.co/flair/ner-english

https://huggingface.co/flair/ner-english-large

https://huggingface.co/models?pipeline_tag=token-classification&language=en&sort=trending

### Benchmark

https://paperswithcode.com/sota/named-entity-recognition-ner-on-conll-2003
https://noisy-text.github.io/2024/
https://paperswithcode.com/sota/named-entity-recognition-on-wnut-2016

### Model

https://huggingface.co/crisistransformers
https://huggingface.co/botryan96/GeoBERT
https://github.com/clarinsi/geobert

### [Flair](https://flairnlp.github.io/docs/intro)

https://datascience.stackexchange.com/questions/107725/what-are-the-differences-between-bert-embedding-and-flair-embedding

[Flair on Hugging Face](https://huggingface.co/flair)

###### Embeddings using Flair

==Flair allows you to combine embeddings into "embedding stacks". When not fine-tuning, using combinations of embeddings often gives best results!==

```python
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings

# Initialize embeddings
glove_embedding = WordEmbeddings('glove')

# Initialize Flair forward and backwards embeddings
flair_embedding_forward = FlairEmbeddings('news-forward')
flair_embedding_backward = FlairEmbeddings('news-backward')

# Create a StackedEmbedding object
stacked_embeddings = StackedEmbeddings([
	glove_embedding,
	flair_embedding_forward,
	flair_embedding_backward,
])

sentence = Sentence('Hoang Sa and Truong Sa belong to Vietnam.')
  
# Embed a sentence using the StackedEmbedding  
stacked_embeddings.embed(sentence)  
  
# Check out the embedded tokens
for token in sentence:  
print(token)  
print(token.embedding)
```
Words are now embedded using a concatenation of three different embeddings. This means that the resulting embedding vector is still a single PyTorch vector.

###### Transformer embeddings

Flair supports various Transformer-based architectures like BERT or XLNet from [HuggingFace](https://github.com/huggingface), with two classes `TransformerWordEmbeddings` (to embed words) and `TransformerDocumentEmbeddings` (to embed documents).

### Fine-tune

### Solution

Adopting NER model (retrained on IDRISI-R)

- Using Flair NER model (1st) and using SpaCy NER model or training deep learning network: LSTM, Roberta, BERT
- No Gazetteers employed
- Training data
	- All team used IDRISI
	- No external training data was used

Use a Gazetteer (OSM) to improve results
Apply Data augmentation to enlarge the training dataset

###### Post Processing

Use a Gazetteer (OSM) to improve results
Don't apply Data augmentation to enlarge the training dataset


2. Reprojection linear layers

How to change the last layer 

CRF related "Viterbi Loss" function can be outperformed using "CrossEntropy loss" if weight are provided for classes

Flair with DeBerta V3 large embedding trained on Ontonote 5 for training

Epochs = 3
Learning rate = 5e-6
MiniBatch size = 8
Optimizer AdamW
Scheduler OneCycleLR
Weight decay 0
Hidden state 768

Use RNN False
Use CRF False

Reproject Embedding True

### Train and Fine-tune

The difference is the set of defaut parameters. Train is usually used for feature-extraction method, where you have a frozen weight and some LSTM layers afterward while `fine_tune` is used for fine-tuning the whole embedding (e.g. using transformers with `fine_tune=True`). Function `train` is for FLAIR embedding, and `fine_tune` is for Transformer embeddings.

### Micro Average and Macro Average

Certainly! The difference between macro and micro averaging is an important concept in evaluation metrics, particularly for classification tasks. Let's break down each one:

1. Macro Average:

Macro averaging calculates the metric independently for each class and then takes the average of these values. This treats all classes equally, regardless of their support (number of instances).

Process:

1. Calculate the metric (e.g., precision, recall, F1-score) for each class.
2. Sum these values.
3. Divide by the number of classes.

Characteristics:

- Gives equal weight to each class.
- Can be skewed by performance on small classes.
- Useful when you want to know how the system performs across all classes, regardless of class imbalance.

2. Micro Average:

Micro averaging aggregates the contributions of all classes to compute the average metric. In effect, it treats the entire dataset as one large multi-class confusion matrix.

Process:

1. Sum up all the true positives, false positives, and false negatives for all classes.
2. Calculate the metric using these aggregate counts.

Characteristics:

- Gives more weight to classes with more instances.
- Less affected by performance on small classes.
- Useful when you have class imbalance and want to weight the metric toward the classes with more samples.

Key Differences:

1. Class Weighting:
    - Macro average gives equal importance to each class.
    - Micro average gives more importance to classes with more samples.
2. Sensitivity to Class Imbalance:
    - Macro average is more sensitive to performance on minority classes.
    - Micro average is more influenced by performance on majority classes.
3. Use Cases:
    - Use macro average when you want to treat all classes equally.
    - Use micro average when you want to weight classes by their frequency.
4. Calculation:
    - Macro average: Calculate metrics for each class, then average.
    - Micro average: Calculate metrics on aggregate counts across all classes.

Example: Let's say you have a 3-class classification problem with the following results:

Class A (100 samples): Precision = 0.8, Recall = 0.7 Class B (10 samples): Precision = 0.6, Recall = 0.5 Class C (1000 samples): Precision = 0.9, Recall = 0.85

Macro Average Precision: (0.8 + 0.6 + 0.9) / 3 = 0.77 Micro Average Precision: Will be closer to 0.9 due to Class C's large sample size

In this case, the macro average gives equal weight to the poorly-performing Class B, while the micro average would be dominated by the well-performing Class C.

Recommendation: For your task, I would recommend using micro averaging as the main evaluation metric. Here's why: a. Entity-Level Evaluation: In named entity recognition tasks (which your location mention recognition is a type of), we often care more about correctly identifying entire entities rather than individual tokens. Micro averaging aligns well with this goal. b. Handling Imbalance: While macro averaging might seem appealing for handling the imbalance between 'O' and location tags, it might give too much weight to potentially rare tagging errors (like confusing 'B-LOC' and 'S-LOC'). c. Standard Practice: Micro averaging is often the standard in NER tasks because it provides a good balance between precision and recall across all classes.


###### [Automatic Mixed Precision](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html)

###### [Mini-batch](https://stackoverflow.com/questions/58269460/what-is-the-meaning-of-a-mini-batch-in-deep-learning)

Check if Florence in train has label as LOC
Check in test

Danh sách các location ở trong BILOU và danh sách Location ở trong JSON, dùng thống kê xem có miss match thế nào

# Papers

### Model

[CrisisTransformers: Pre-trained language models and sentence encoders for crisis-related social media texts](https://www.sciencedirect.com/science/article/pii/S0950705124005501)
https://huggingface.co/rsuwaileh
https://huggingface.co/crisistransformers

### Dataset

[IDRISI-RE: A generalizable dataset with benchmarks for location mention recognition on disaster tweets](https://www.sciencedirect.com/science/article/pii/S0306457323000778)
https://github.com/uhuohuy/DLRGeoTweet

[DLRGeoTweet: A comprehensive social media geocoding corpus featuring fine-grained places](https://doi.org/10.1016/j.ipm.2024.103742)
https://crisisnlp.qcri.org/humaid_dataset.html

### Gazette

[Automatic gazette creation for named entity recognition and application to resume processing](https://www.researchgate.net/publication/262369926_Automatic_gazette_creation_for_named_entity_recognition_and_application_to_resume_processing)

# [CrisisTransformers](https://huggingface.co/crisistransformers/CT-M2-BestLoss#crisistransformers)

The models were trained based on the RoBERTa pre-training procedure on a massive corpus of over 15 billion word tokens sourced from tweets associated with 30+ crisis events such as disease outbreaks, natural disasters, conflicts, etc.

## Uses

CrisisTransformers has 8 pre-trained models, 1 mono-lingual and 2 multi-lingual sentence encoders. The pre-trained models should be finetuned for downstream tasks just like [BERT](https://huggingface.co/bert-base-cased) and [RoBERTa](https://huggingface.co/roberta-base). The sentence encoders can be used out-of-the-box just like [Sentence-Transformers](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) for sentence encoding to facilitate tasks such as semantic search, clustering, topic modelling.

We will use CT-M3-Complete for better tokenizer