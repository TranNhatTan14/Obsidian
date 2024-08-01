- [ ] Convert BILUO to BIOES
- [ ] Preprocessing is the most important
- [ ] Fine-tuning

https://github.com/moadel2002/Location-Mention-Recognition
https://github.com/flairNLP/flair/blob/master/resources/docs/HUNFLAIR_TUTORIAL_2_TRAINING.md
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

1. Sentence embedding
2. Reprojection linear layers
3. Output

###### Embedding

1. Download the IDRISI dataset
2. Replace all tags with "LOC" tags
3. Preprocessing sentences to BIOES
4. Training on dataset

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