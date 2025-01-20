---
tags:
  - Book
description: Practical techniques and architectures for building powerful graph and deep learning apps with PyTorch
---
# Part 1: Introduction to Graph Learning

##  Chapter 1: Getting started with Graph Learning

### Why graph?

### Why graph learning?

### Why graph neural networks?

##  Chapter 2: Graph Theory for Graph Neural Network

## Introducing graph properties

### Directed graphs

### Weighted graphs

### Connected graphs

### Types of graphs

## Discovering graph concepts

### Fundamental objects

### Graph measures

### Adjacency matrix representation

## Exploring graph algorithms

### Breadth-first search

### Depth-first search

##  Chapter 3: Creating Node Representations with DeepWalk

### Introducing Word2Vec

#### CBOW versus skip-gram

#### Creating skip-grams

#### The skip-gram model

### DeepWalk and random walks

### Implementing DeepWalk

#  Part 2: Fundamentals

##  Chapter 4: Improving Embeddings with Biased Random Walks in Node2Vec

### Introducing Node2Vec

### Defining a neighborhood

### Introducing biases in random walks

### Implementing Node2Vec

### Building a movie RecSys

##  Chapter 5: Including Node Features with Vanilla Neural Networks

### Introducing graph datasets

#### The Cora dataset

#### The Facebook Page-Page dataset

### Classifying nodes with vanilla neural networks

You will master the implementation of vanilla neural networks and vanilla GNNs in PyTorch. You will be able to embed topological features into the node representations, which is the basis of very GNN architecture. This will allow you to greatly improve the performance of your models by transforming tabular datasets into graph problems.

We'll cover the following topics

- Introducing graph datasets
- Classifying nodes with both vannilla neural networks and vanilla [[Graph Neural Networks]]

#### Graph datasets

The Cora dataset represents a networks of 2,708 publications, where each connection is a reference. Each publication is described as a binary vector of 1,433 unique words, where 0 and 1 indicate the absence or presence of the corresponding word, respectively. This representation is also called a binary bag of words in [[Natural Language Processing]]. Our goal is to classify each node into one of senven categories

### Classifying nodes with vanilla graph neural networks

A basic neural network layer corresponds to a linear transformation

In our case, the adjacency matrix A contains the connections between every node in the graph. 

### Summary

- We learned about the missing link between vanilla neural networks and GNNs
- The our intuitive version of a GNN completely outperforms the MLP on both datasets

In next chapter, we refine our vanilla GNN architecture to correctly normalize its inputs. This graph convolutional network model is an incredibly efficient baseline we'll keep using in the rest of the book. We will compare its result on our two previous datasets and introduce a new interesting task: node regression.

##  Chapter 6: Introducing Graph Convolutional Networks

**Goals**

- Refine our vanilla GNN architecture to correctly normalize its inputs
- Know the limitations of our previous vanilla GNN layers
- Understand the motivation behind GCNs
- How the GCN layer works and why it performs better

- The GCN architecture is the blueprint of GNN
- GCN is an approximation of a graph convolution operation in graph signal processing [[Brain–Computer Interface]]

- The features from nodes with a lot of neighbors spread very easily, unlike features from more isolated nodes

### Designing the graph convolutional layer

First, let's talk about a problem we did not anticipate in the previous chapter. Unlike tabular or image data, nodes do not always have the same number of neighbors.

However, we don't take into account the difference in the number of neighbors in GNN layers.

### Implementing a GCN in PyTorch Geometric

### Predicting web traffic with node regression

##  Chapter 7: Graph Attention Networks

- GATs are a theoretical improvement over GCNs
- Instead of static normalization coefficients, they propse weighting factors calculated by a process called self-attention

### Introducing the graph attention layer

- The main idea behind GATs is that some nodes are more important than others.
- In fact, this was already the case with th graph convolutional layer: nodes with few neighbors were more important than others. thank to the normalization cofficient.
	- This approach is limiting because it only takes into account node degrees
- The goal of the graph attention layer is to produce weighting factors that also consider the importance of node features

An important characteristic of GATs is that the attention scores are calculated implicitly by comparing
inputs to each other (hence the name self-attention). In this section, we will see how to calculate these
attention scores in four steps and also how to make an improvement to the graph attention layer:

- Linear transformation
- Activation function
- Softmax normalization
- Multi-head attention
- Improved graph attention layer

**Linear Transformation**

The attention score represents the importance between a central node i and a neighbor j.

### Implementing the graph attention layer in NumPy

### Implementing a GAT in PyTorch Geometric

Graph Attention Networks (GATs) are a theoretical improvement over GCNs

### Multi-head attention

Self-attention is not very stable. This issue was already noticed in the original [[Transformer]] paper. Their proposed solution consists of calculating multiple embedding with their own attention scores instead of a single one. This technique is called multi-head attention.

### Summary

- The GAT architecture

# Part 3: Advanced Techniques

## Chapter 8: Scaling Up [[Graph Neural Networks]] with GraphSAGE

### Introducing GraphSAGE

#### Neighbor Sampling

#### Aggregation

### Classifying nodes on PubMed

### Inductive learning on protein-protein interactions
##  Chapter 9: Defining Expressiveness for Graph Classification

### Defining expressiveness

### Introducing the GIN

### Classifying graphs using GIN

#### Graph classification

#### Implementing the GIN

##  Chapter 10: Predicting Links with [[Graph Neural Networks]]

### Predicting links with traditional methods

#### Heuristic techniques

#### Matrix factorization

### Predicting links with node embeddings

#### Graph Autoencoder

#### Variational Graph Autoencoder

### Predicting links with SEAL

##  Chapter 11: Generating Graphs Using [[Graph Neural Networks]]

### Generating graphs with traditional techniques

#### Erdos-Renyi model

#### Barabasi-Albert model

#### Watts-Strogatz model

### Generating graphs with graph neural networks

#### GraphRNN

#### Variational Graph Autoencoder

### Generating molecules with MolGAN

##  Chapter 12: Learning from Heterogeneous Graphs

### The message passing neural network framework

### Introducing heterogeneous graphs

### Transforming homogeneous GNNs to heterogeneous GNNs

### Implementing a hierarchical self-attention network

##  Chapter 13: Temporal [[Graph Neural Networks]]

### Introducing dynamic graphs

#### Discrete-time dynamic graphs

#### Continuous-time dynamic graphs

### Forecasting web traffic

#### Implementing EvolveGCN

### Predicting cases of COVID-19

#### MPNN-LSTM architecture for COVID-19 prediction

##  Chapter 14: Explaining [[Graph Neural Networks]]

### Introducing explanation techniques

### Explaining GNNs with GNNExplainer

#### Introducing GNNExplainer

### Explaining GNNs with Captum

#### Introducing Captum and integrated gradients

# Part 4: Applications

##  Chapter 15: Forecasting Traffic Using A3T-GCN


### Exploring the PeMS-M dataset

### Processing the dataset

### Implementing a temporal GNN

#### A3T-GCN architecture

##  Chapter 16: Detecting Anomalies Using Heterogeneous GNNs

### Exploring the CIDDS-001 dataset

### Preprocessing the CIDDS-001 dataset

### Implementing a heterogeneous GNN

##  Chapter 17: Building a Recommender System Using LightGCN

### Exploring the Book-Crossing dataset

### Preprocessing the Book-Crossing dataset

### Implementing the LightGCN architecture

## Chapter 18: Unlocking the Potential of Graph Neural Networks for Real-World Applications
# [[Q&A]]