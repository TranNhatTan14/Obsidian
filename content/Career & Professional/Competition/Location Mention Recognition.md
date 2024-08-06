https://huggingface.co/adambuttrick/ner-test-bert-base-uncased-finetuned-500K-AdamW-3-epoch-locations/tree/main

Run the baseline bert

- [ ] Convert BILUO to BIOES
- [ ] Preprocessing is the most important
	- [ ] Remove all stopword, ?, and #
- [ ] Fine-tuning
- [ ] Check if result change if text in lowcase

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

1. Sentence embedding

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

![[Pasted image 20240804103833.png]]

![[Pasted image 20240804104538.png]]

2. Reprojection linear layers

How to change the last layer 

![[Pasted image 20240804104942.png]]

![[Pasted image 20240804105126.png]]

![[Pasted image 20240804105247.png]]


![[Pasted image 20240804105544.png]]

### Train and Fine-tune

The difference is the set of defaut parameters. Train is usually used for feature-extraction method, where you have a frozen weight and some LSTM layers afterward while `fine_tune` is used for fine-tuning the whole embedding (e.g. using transformers with `fine_tune=True`). Function `train` is for FLAIR embedding, and `fine_tune` is for Transformer embeddings.

###### Micro Average and Macro Average

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

### https://www.researchgate.net/figure/Performance-of-gazette-based-NER-algorithm_fig2_262369926

