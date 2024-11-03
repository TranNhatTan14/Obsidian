---
tags:
  - Microsoft
  - Competition
  - Zindi
URL: https://zindi.africa/competitions/microsoft-learn-location-mention-recognition-challenge
---
# Data

- We can only use data from the CSV file, so we should get the most from the

# Computational Resources

https://github.com/mehranshakarami/AI_Spectrum

Try to retrieve JSON data instead. So you won't lose too much data ([](https://github.com/rsuwaileh/IDRISI/blob/main/LMR/data/EN/gold-random-json/)[https://github.com/rsuwaileh/IDRISI/blob/main/LMR/data/EN/gold-random-json/](https://github.com/rsuwaileh/IDRISI/blob/main/LMR/data/EN/gold-random-json/))

The effect of this:

I have just used the Golden random json data on Github , with the same strategy I used in the CSV data that got me 0.16 on the LB and I just got 0.28. So this is a valid point. Most probably the test dataset labelling has followed the Train csv provided format and not the JSON data on github.

For example, if the text was "South Africa is larger than South Wales but neither is bigger than South East Asia." You would need to return "**South Africa South East Asia South Wales**".

so the first priority is given to locations with a larger number of words, followed by locations in alphabetical order as the second priority ?

I think thats a mistake: It should be

South Africa South East Asia South Wales

If I am not wrong given the updated train set.

And to answer your question Nayal I think all locations should be returned even if they are repeated. I am saying this because the updated train has repeated locations. You sshould probably check it out

For example, if the text was "South Africa is larger than South Wales but neither is bigger than South East Asia." You would need to return "South Africa South East Asia South Wales".

The data for this competition was prepared using location mentions labeled by human annotators. Duplicate mentions, if any, should be treated as one and your model need only generate every unique location mentioned in a sample text. Only distinct locations mentioned in a text, and picked up by your model, should be grouped and ordered alphabetically.

- Duplicate location mentions, should be treated as one
- Only distinct locations mentioned in a text
- Hello, the casing is the same as that in the tweet, an extra challenge
- Don't remove character like
	- 732 .
	- 9 @
	- 8 ,
	- 0 !
	- 1 : ;
	- 0 ' "
	- 202 -
	- 28 _
	- 103 /
	- 0 
	- 6 +
	- 2 ~
	- 3 #
	- Not remove number

https://huggingface.co/adambuttrick/ner-test-bert-base-uncased-finetuned-500K-AdamW-3-epoch-locations/tree/main

219 sample don't have location

### Resource

[1st place solution for GeoAI Challege Location Mention Recognition from Social Media](https://github.com/moadel2002/Location-Mention-Recognition)

https://huggingface.co/blog/stefan-it/autotrain-flair-mobie

### Benchmark

https://paperswithcode.com/sota/named-entity-recognition-ner-on-conll-2003
https://noisy-text.github.io/2024/
https://paperswithcode.com/sota/named-entity-recognition-on-wnut-2016

# Model

https://huggingface.co/docs/transformers/en/tasks/token_classification

https://huggingface.co/tasks/token-classification
https://huggingface.co/dslim/bert-base-NER
https://huggingface.co/flair/ner-english

https://huggingface.co/flair/ner-english-large

https://huggingface.co/models?pipeline_tag=token-classification&language=en&sort=trending

https://huggingface.co/crisistransformers
https://huggingface.co/botryan96/GeoBERT
https://github.com/clarinsi/geobert

## [CrisisTransformers](https://huggingface.co/crisistransformers/CT-M2-BestLoss#crisistransformers)

The models were trained based on the RoBERTa pre-training procedure on a massive corpus of over 15 billion word tokens sourced from tweets associated with 30+ crisis events such as disease outbreaks, natural disasters, conflicts, etc.

CrisisTransformers has 8 pre-trained models, 1 mono-lingual and 2 multi-lingual sentence encoders. The pre-trained models should be finetuned for downstream tasks just like [BERT](https://huggingface.co/bert-base-cased) and [RoBERTa](https://huggingface.co/roberta-base). The sentence encoders can be used out-of-the-box just like [Sentence-Transformers](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) for sentence encoding to facilitate tasks such as semantic search, clustering, topic modelling.

We will use CT-M3-Complete for better tokenizer
## [Flair](https://flairnlp.github.io/docs/intro)

https://datascience.stackexchange.com/questions/107725/what-are-the-differences-between-bert-embedding-and-flair-embedding

[Flair on Hugging Face](https://huggingface.co/flair)

### Embeddings using Flair

==Flair allows you to combine embeddings into "embedding stacks". When not fine-tuning, using combinations of embeddings often gives best results==

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

### Transformer embeddings

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

### Post Processing

Use a Gazetteer (OSM) to improve results
Don't apply Data augmentation to enlarge the training dataset

2. Reprojection linear layers

How to change the last layer 

CRF related "Viterbi Loss" function can be outperformed using "CrossEntropy loss" if weight are provided for classes

Flair with DeBerta V3 large embedding trained on Ontonote 5 for training

### Train and Fine-tune

The difference is the set of defaut parameters. Train is usually used for feature-extraction method, where you have a frozen weight and some LSTM layers afterward while `fine_tune` is used for fine-tuning the whole embedding (e.g. using transformers with `fine_tune=True`). Function `train` is for FLAIR embedding, and `fine_tune` is for Transformer embeddings.

### [Automatic Mixed Precision](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html)

### [Mini-batch](https://stackoverflow.com/questions/58269460/what-is-the-meaning-of-a-mini-batch-in-deep-learning)

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