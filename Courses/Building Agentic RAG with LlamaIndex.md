---
tags:
  - Course
  - RAG
---
- Build an agent that can reason over your documents and answer complex questions.
- Build a router agent that can help you with Q&A and summarization tasks, and extend it to handle passing arguments to this agent.
- Design a research agent that handles multi-documents and learn about different ways to debug and control this agent.

## About this course

Join our new short course and learn from Jerry Liu, co-founder and CEO at LlamaIndex to start using agentic RAG, a framework designed to build research agents skilled in tool use, reasoning, and decision-making with your data.

In this course:

- Build the simplest form of agentic RAG – a router. ==Given a query, the router will pick one of two query engines==, Q&A or summarization, to execute a query over a single document.
- Add tool calling to your router agent where you will use an LLM to not only pick a function to execute but also ==infer an argument to pass to the function.==
- Build a research assistant agent. Instead of tool calling in a single-shot setting, an agent is ==able to reason over tools in multiple steps.== 
- Build a multi-document agent where you will learn how to extend the research agent to handle multiple documents.

Unlike the standard RAG pipeline—suitable for simple queries across a few documents—this intelligent approach adapts based on ==initial findings to enhance further data retrieval==. You’ll learn to develop an autonomous research agent, enhancing your ability to engage with and analyze your data comprehensively.

You’ll practice building agents capable of intelligently navigating, summarizing, and comparing information across multiple research papers from arXiv. Additionally, you’ll learn how to debug these agents, ensuring you can guide their actions effectively. 

Explore one of the most rapidly advancing applications of agentic AI!

- Topic and wwant to pull out the parts relevant to a quesiton
- Build an autonomous research agent
	- Routing add decision making to route request to multiple tools
	- Tool use create an interfae for agents
	- Multi-step researing 

# Router Query Engine

Given a query, the router will pick one of several query engines to execute a query 

User asks a complex question consisting of multiple steps or a vague question that need clarification 

agent reasoning loop

