---
tags:
  - GeneStory
  - Seminar
links:
  - "[[Python]]"
URL: https://github.com/phamdinhha/python-concurrency-test
---
process, threads in C

Golang ...

Python 

# Threads

# Asyncio

# Timeline

# Introduction

## What is concurrency

## Concurrency and parallelism

## Why we need concurrency

Performance improvement

- Better resource ultilzation
- Reduced waiting time

Real-world requirements

Modern architecture demands

- Micorservices architecture
- Distributed systems
- Event-driven applications
- Web applications and API

## Process and Thread

## I/0 bound vs CPU bound

Interact with other system, query, read, load file is I/O bound

CPU bound like computation

## Concurrency in Python

**Multiprocessing**

Global Interpreter Lock (GCL)

- Process
- Queue
- Pipe
- Lock
- Shared Memory: Value + Queue

**Multithreading Pre-emptive multitasking**

The OS decides when to switch task-external to Python

**Asyncio Cooperative multitasking**

The tasks decide ehrn to give up control

When we know when task end, for 1 thread

## Can you bypass GIL

- Use GIL-immune libraris like numpy and pandas
- New version of Python have experimental code for disabling GIL 3.13

Demo handon

Benchmarking


io bound multiprocess
cpu bound multithreading