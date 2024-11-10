---
tags:
  - Book
description: Practical techniques and architectures for building powerful graph and deep learning apps with PyTorch
---
# Introduction to Graph Learning

## Getting started with Graph Learning

## Graph Theory for Graph Neural Network

## Creating Node Representations with DeepWalk

# Fundamentals

## Improving Embeddings with Biased Random Walks in Node2Vec

## Including Node Features with Vanilla Neural Networks

You will master the implementation of vanilla neural networks and vanilla GNNs in PyTorch. You will be able to embed topological features into the node representations, which is the basis of very GNN architecture. This will allow you to greatly improve the performance of your models by transforming tabular datasets into graph problems.

We'll cover the following topics

- Introducing graph datasets
- Classifying nodes with both vannilla neural networks and vanilla [[Graph Neural Networks]]

### Graph datasets

The Cora dataset represents a networks of 2,708 publications, where each connection is a reference. Each publication is described as a binary vector of 1,433 unique words, where 0 and 1 indicate the absence or presence of the corresponding word, respectively. This representation is also called a binary bag of words in [[natural language processing]]. Our goal is to classify each node into one of senven categories

### Classifying nodes with vanilla graph neural networks

A basic neural network layer corresponds to a linear transformation

In our case, the adjacency matrix A contains the connections between every node in the graph. 

### Summary

In this chapter, we learned about the missing link between vanilla neural networks and GNNs. We built own own GNN architecture using our intuition and a bit of linear algebra. We explored two popular graph datasets from the scientific literature to compare our two architectures. Finnaly, we implemented them in PyTorch and evaluated their performance.

In next chapter, we refine our vanilla GNN architecture to correctly normalize its inputs. This graph convolutional network model is an incredibly efficient baseline we'll keep using in the rest of the book. We will compare its result on our two previous datasets and introduce a new interesting task: node regression.

## Introducing Graph Convolutional Networks

### Designing the graph convolutional layer

First, let's talk about a problem we did not anticipate in the previous chapter. Unlike tabular or image data, nodes do not always have the same number of neighbors.

However, we don't take into account the difference in the number of neighbors in GNN layers.

## Graph Attention Networks

Graph Attention Networks (GATs) are a theoretical improvement over GCNs

### Multi-head attention

Self-attention is not very stable. This issue was already noticed in the original [[Transformer]] paper. Their proposed solution consists of calculating multiple embedding with their own attention scores instead of a single one. This technique is called multi-head attention.

# Advanced Techniques

## Scaling Up [[Graph Neural Networks]] with GraphSAGE

## Defining Expressiveness for Graph Classification

## Predicting Links with [[Graph Neural Networks]]

## Generating Graphs Using [[Graph Neural Networks]]

## Learning from Heterogeneous Graphs

## Temporal [[Graph Neural Networks]]

## Explaining [[Graph Neural Networks]]

# Applications

## Forecasting Traffic Using A3T-GCN

## Detecting Anomalies Using Heterogeneous GNNs

## Building a Recommender System Using LightGCN

# [[Q&A]]