---
tags:
  - Course
links:
  - "[[Artificial Intelligence]]"
  - "[[Andrej Karpathy]]"
---
We build a **Generatively Pretrained Transformer (GPT)**, following the paper "Attention is All You Need" and OpenAI's GPT-2 / GPT-3. We talk about **connections to ChatGPT**, which has taken the world by storm. We watch **GitHub Copilot**, itself a GPT, help us write a GPT (meta :D!) . I recommend people watch the earlier makemore videos to get comfortable with the autoregressive language modeling framework and basics of tensors and PyTorch nn, which we take for granted in this video.

- Attention is All You Need
    

Build ChatGPT

Pretraining

Finetuning

We will train on Small Shake Spiere

Character sequence looklike

NanoGPT

How under the hood ChatGPT work

Tokenize mean convert some word from text to sequence of interger

ChatGPT ise tiktoken use BPE

Trade-off between vocabulary size and sequence of interger length

We only train with chunk of dataset

Block_size

Train with many batches of multiple chunks of text for

GPU

---

Micrograd

Backpropagation is

backpropagation signal which is carrying the information about derivatives of L to all children node

Foward pass

NN is just mathematical expression

**GPU like high-way with many roads**

Multi-layer perceptron is a sequence of layers of neutron

efficiency

**derivative**

Mình cảm thấy bất ngờ, wow vì hiểu thêm dựa trên nhưng gì A K dạy

Gradientc

Crux of the backpropagation

The most important node

Local derivative

Chain-rule in calculus to calculate dF/dc

Toppological Sortc

Tensors are just n-dimensional arrays of scalars

Start with implement with Micrograd from scratch then learn to use PyTorch API

Or check how PyTorch have built but to understand we need to watch this video

Gradient as a vector pointing in the direction of increased loss.

Learning rete decay

PyTorch: Defining new autograd functions

#### Make More

Character language models

#### Bigram

Just look at 1 characters