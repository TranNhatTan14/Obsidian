---
tags:
  - Book
---
https://static.packt-cdn.com/downloads/9781836200079_ColorImages.pdf

# Forewords

- AI is becoming the default way of building techlonogy

# Preface

# Who this book is for

# What this book covers

# Understanding the [[Large Language Model|LLM]] Twin Concept and Architecture

==Introduces the [[Large Language Model|LLM]] Twin project, which is used throughout the book as an end-to-end example of a production-level [[Large Language Model|LLM]] application, and defines the FTI architecture for building scalable ML systems and applies it to the [[Large Language Model|LLM]] Twin use case.==

When starting to implement a new product, from an engineering point of view, there are three planning steps we must go through before we start building

1. It is critical to understand the problem we are trying to solve and what we want to build, and why build it
2. To reflect a real-world scenario, we will design the first iteration of product with minimum functionality. Here, we must clearly define the core features requires to create a working and valuable product. The choices are made based on the timeline, resources, and team's knowledge.
3. System design step, laying out the core architecture and design choices used to build the LLM system.

The first two components are primarily product-related, while the last one is technical and focuses on the "How"

- Understanding the LLM Twin concept
- Planning the MVP of the LLM Twin product
- Building ML systems with feature/training/inference pipelines
- Designing the system architecture of the LLM Twin

## What is an LLM Twin?

LLM Twin is an AI character that incorporates your writing style, voice, and personality into an LLM, which is a complex AI model

LLM reflects the data it was trained on. This is also known as style transfer. But instead of choosing a personality, we will do it on our own persona.

To adjust the LLM to given style and voice along with fine-tuning, we also leverage various advanced retrieval-augmented generation (RAG) techniques that condition the autoregressive process with previous embedding of ourselves.

## Why building an LLM Twin matters

As an engineer (or any other professional career), building a personal brand is more valuable than a standard CV. The biggest issue with creating a personal brand is that writing content on platform such as LinkedIn, X, or Medium takes a lot of time. Even if you enjoy writing and creating content, you will evventually run out of inspiration or time and feel like you need assistance.

## Why not use other chatbot

## Key of the LLM Twin

- What data we collect
- How to preprocess the data
- How we feed the data into the LLM
- How we chain multiple prompts for the disired results
- How we evaluate the generated content

## Planning the MVP of the LLM Twin product

- Collect data from your LinkedIn, Medium, Substack, and Github profiles
- Fine-tune an open-source LLM using the collected data
- Populate a vector database using our digital data for RAG
- Create LinkedIn posts leveraging the following
	- User prompts
- RAG to reuse and reference old content
- New post, articles, or papers as additional knowledge to the LLM
- Have a simple web interface to interact with LLM Twin and be able to do
	- Configure you social medial links and trigger the collection step
- Send prompts or links to external resources
- Make system cost effective, scalable, and modular

## Defining the LLM Twin MVP

## Building ML systems with FTI pipelines

## The problem with building ML systems

## Benefit of the FTI architecture

## Design the system architecture of the LLM Twin

## Listing the technical details of the LLM Twin architecture

## How to design the LLM Twin architecture using the FTI pipeline design

## Data collection pipeline

## Feature pipeline

## Training pipeline

## Inference pipeline

# Tooling and Installation

Presents Python, MLOps, and cloud tools used to build real-world [[Large Language Model|LLM]] applications, such as orchestrator, experiment tracker, prompt monitoring and [[Large Language Model|LLM]] evaluation tool. It shows how to use and install them locally for testing and development.

## Python ecosystem and project installation

## Poetry: dependency and virtual environment management

## Poe the Poet: Task execution tool

## MLOps and LLMOps tooling

## Hugging Face: model registry

## ZenML: orchestrator, artifacts, and metadata

### Orchestrator

### Artifacts and metadata

### How to run and configure a ZenML pipeline

## Comet ML: Experiment tracker

## Opik: prompt monitoring

## Databases for storing unstructured and vector data

### [[MongoDB]]: No SQL database

### [[Qdrant]]: vector database

## [[AWS]]

### Preparing for [[AWS]]

## [[SageMaker]]: training and inference compute

## Summary

Reviewed the core tools

- How to install the correct version of Python
- How to create a virtual environment and install all the dependencies using Poetry
- How to use a task execution tool like Poe the Poet to aggregate all the commands required to run the application.

# Data Engineering

Shows the implementation of a data collection pipeline that scrapes multiple sites, such as [[Medium]], [[Github]], and [[Subtack]] and stores the raw data in a data warehouse. It emphasizes collecting raw data from dynamic sources over static datasets for real-world ML applications.

## Designing the LLM Twin's data collection pipeline

## Implementing the LLM Twin's data collection pipeline

## ZenML pipeline and steps

## The dispatcher: How do you instantiate the right crawler

## The crawlers

### GitHubCrawler class

### CustomArticleCrawler class

### MediumCrawler class

## The NoSQL data warehouse document

## The ORM and ODM software patterns

## Data categories and user document classes

## Gathering raw data into the data warehouse


# RAG Feature Pipeline

Introduces RAG fundamental concepts, such as embeddings, the vanilla RAG framework, vector databases, and how to optimize RAG applications. It applies the RAG theory by architecting and implementing [[Large Language Model|LLM]] Twin's RAG feature pipeline using software best practices.

Understanding RAG

Why use RAG

Hallucinations

Old information

The vanilla RAG framework

Ingestion pipeline

Retrieval pipeline

Generation pipeline

What are embeddings

Why embeddings are so powerful

How are embeddings created

Application of embeddings

vector DBs

How does a vector DB work

Algorithms for creating the vector index

DB operations

Advanced RAG

Pre-retrieval

Retrieval

Post-retrieval

Exploring the LLM Twin's RAG feature pipeline architecture

The problem we are solving

The feature store

What does the raw data come from

Designing the architecture of the RAG feature pipeline

Batch pipelines

Batch versus streaming pipelines

Core steps

Change data capture syncing the data warehouse and feature store

Why is the data stored in two snapshoots

Orchestration

Implementing the LLM Twin's RAG feature pipeline

Settings

ZenML pipeline and steps

Querying the data warehouse

Clearning the documents

Chunk and entired the cleaned documents

Loading the documents to the vector DB

Pydantic domain entities

OVM

The dispatcher layer

The handlers

The cleaning handlers

The chunking handlers

The embedding handlers

# Supervised Fine-Tuning

Explores the process of refining pre-trained language models for specific task using instruction-answer pairs. It covers creating high-quality datasets, implementing fine-tuning techniques like full fine-tuning, LoRA, and QLoRA, and provides a practical demonstration of fine-tuning a Llama 3.1 model on a custom dataset.

Creating an instruction dataset

General framework

Data quantity

Data curation

Rule-based filtering

Data 

# Fine-tunning with Preference Alignment

Introduces techiniques for aligning language models with human preferences, focusing on Direct Preference Optimization (DPO). It covers creating custom preference datasets, implementing DPO, and provides a practical demonstration of aligning the TwinLlama-3.1-8B model using the [[Unsloth]] library.

# Evaluating LLMs

Details various methods for assessing the performance of language models and [[Large Language Model|LLM]] systems. It introduces general-purpose and domain-specific evaluations and discusses popular benchmarks. This chapter includes a practical evaluation of the TwinLlama-3.1-8B model using multiple criteria.

# Inference Optimization

Covers key optimization strategies such as speculative decoding, model parallelism, and weight quantization. It discusses how to improve inference speed, reduce latency, and minimize memory usage, introducing popular inference engines and comparing their features

# RAG Inference Pipeline

Explore advanced RAG tachniques by implementing method such as self-query, reranking, and filtered vector search from scratch. It covers designing and implementing the LLM Twin's RAG inference pipeline and a custom retrieval module similar to what you see in popular frameworks such as LangChain.

# Inference Pipeline Deployment

ML deployment strategies, such as online, asynchronous and batch inference, which will help in architecting and deploying the LLM Twin fine-tuned model to AWS SageMaker and building a [[FastAPI]] microservice to expose the RAG inference pipeline as RESTful API

# MLOps and LLMOps

Present what LLMOps is, starting with its roots in DevOps and MLOps. This chapter explains how to deploy the LLM Twin project to the cloud, such as ML pipelines to AWS and shows how to containerize the code using Docker and build a CI/CD/CT pipeline. It also add a prompt monitoring layer on top of LLM Twin's Inference pipeline

