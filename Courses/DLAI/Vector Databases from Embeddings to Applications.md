---
tags:
  - Course
  - DLAI
URL: https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications
---
## What you'll learn

- Build efficient, practical applications including ==hybrid and multilingual searches, for diverse industries==.
- ==Understand vector databases and use them to develop GenAI applications without needing to train or fine-tune an LLM yourself.==
- Learn to discern when best to apply a vector database to your application.

## About this course

Vector databases play a pivotal role across various fields, such as natural language processing, image recognition, recommender systems and semantic search, and have gained more importance with the growing adoption of LLMs. 

These databases are exceptionally valuable as they provide LLMs with access to real-time proprietary data, enabling the development of Retrieval Augmented Generation (RAG) applications.

At their core, ==vector databases rely on the use of embeddings to capture the meaning of data and gauge the similarity between different pairs of vectors== and sift through extensive datasets, identifying the most similar vectors. 

This course will help you gain the knowledge to make informed decisions about when to apply vector databases to your applications. You’ll explore:

- How to use vector databases and LLMs to gain deeper insights into your data.
- Build labs that show how to form embeddings and use several ==search techniques to find similar embeddings.==
- Explore algorithms for fast searches through vast datasets and build applications ranging from RAG to multilingual search.

# Outline

## Introduction
## How to Obtain Vector Representations of Data

![VAE](https://upload.wikimedia.org/wikipedia/commons/4/4a/VAE_Basic.png)

```python
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Lambda
from tensorflow.keras.models import Model
from tensorflow.keras import backend as K
from tensorflow.keras import losses
from scipy.stats import norm

# Load data – training and test
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Normalize and Reshape images (flatten)
x_train, x_test = x_train.astype('float32')/255., x_test.astype('float32')/255.
x_train_flat, x_test_flat = x_train.reshape(x_train.shape[0], -1), x_test.reshape(x_test.shape[0], -1)

print(x_train.shape, x_test.shape)
print(x_train_flat.shape, x_test_flat.shape)

# Neural Network Parameters
batch_size, n_epoch = 100, 50
n_hidden, z_dim = 256, 2

# Example of a training image
plt.imshow(x_train[1]);
```

```python
# sampling function
def sampling(args):
    mu, log_var = args
    eps = K.random_normal(shape=(batch_size, z_dim), mean=0., stddev=1.0)
    return mu + K.exp(log_var) * eps

# Encoder - from 784->256->128->2
inputs_flat = Input(shape=(x_tr_flat.shape[1:]))
x_flat = Dense(n_hidden, activation='relu')(inputs_flat) # first hidden layer
x_flat = Dense(n_hidden//2, activation='relu')(x_flat)  # second hidden layer

# hidden state, which we will pass into the Model to get the Encoder.
mu_flat = Dense(z_dim)(x_flat)
log_var_flat = Dense(z_dim)(x_flat)
z_flat = Lambda(sampling, output_shape=(z_dim,))([mu_flat, log_var_flat])

#Decoder - from 2->128->256->784
latent_inputs = Input(shape=(z_dim,))
z_decoder1 = Dense(n_hidden//2, activation='relu')
z_decoder2 = Dense(n_hidden, activation='relu')
y_decoder = Dense(x_tr_flat.shape[1], activation='sigmoid')
z_decoded = z_decoder1(latent_inputs)
z_decoded = z_decoder2(z_decoded)
y_decoded = y_decoder(z_decoded)
decoder_flat = Model(latent_inputs, y_decoded, name="decoder_conv")

outputs_flat = decoder_flat(z_flat)

# variational autoencoder (VAE) - to reconstruction input
reconstruction_loss = losses.binary_crossentropy(inputs_flat,
                                                 outputs_flat) * x_tr_flat.shape[1]
kl_loss = 0.5 * K.sum(K.square(mu_flat) + K.exp(log_var_flat) - log_var_flat - 1, axis = -1)
vae_flat_loss = reconstruction_loss + kl_loss

# Build model
#  Ensure that the reconstructed outputs are as close to the inputs
vae_flat = Model(inputs_flat, outputs_flat)
vae_flat.add_loss(vae_flat_loss)
vae_flat.compile(optimizer='adam')

# train
vae_flat.fit(
    x_tr_flat,
    shuffle=True,
    epochs=n_epoch,
    batch_size=batch_size,
    validation_data=(x_te_flat, None),
    verbose=1
)
```
## Search for Similar Vectors
## Approximate nearest neighbours
## Vector Databases
## Sparse, Dense, and Hybrid Search
## Application - Multilingual Search
## Conclusion