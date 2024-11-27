---
tags:
  - Course
  - DLAI
aliases:
  - "Retrieval Optimization: From Tokenization to Vector Quantization"
---
## What you'll learn

- Learn ==how tokenization works in large language and embedding models== and ==how the tokenizer can affect the quality of your search==.
- Explore how different tokenization techniques including Byte-Pair Encoding, WordPiece, and Unigram are trained and work.
- Understand ==how to measure the quality of your retrieval== and how to optimize your search by adjusting HNSW parameters and vector quantizations.

## About this course

In _Retrieval Optimization: From Tokenization to Vector Quantization_, taught by _Kacper Łukawski_, _Developer Relations Lead of Qdrant_, you’ll learn all about tokenization and also how to optimize vector search in your large-scale customer-facing RAG applications. You’ll explore the technical details of how vector search works and how to optimize it for better performance.

- Learn about tokenization and how to optimize vector search in large scale customer-facing RAG applicaion
- Technique details of how vector search works and how to optimize it for better performance

This course focuses on optimizing the first step in your RAG and search results. You’ll see how different tokenization techniques like Byte-Pair Encoding, WordPiece, and Unigram work and how they affect search relevancy. You’ll also learn how to address common challenges such as ==terminology mismatches and truncated chunks in embedding models.==

To optimize your search, you need to be able to measure its quality. You will learn several quality metrics for this purpose. Most vector databases use ==Hierarchical Navigable Small Worlds== (HNSW) for approximate nearest-neighbor search. You’ll see how to balance the HNSW parameters for higher speed and maximum relevance. Finally, you would use different vector quantization techniques to enhance memory usage and search speed.

What you’ll do, in detail: 

- Learn about the internal workings of the embedding model and how your text is turned into vectors.
- Understand how several tokenizers such as Byte-Pair Encoding, WordPiece, Unigram, and SentencePiece are trained.
- Explore common challenges with tokenizers such as unknown tokens, domain-specific identifiers, and numerical values, that can negatively affect your vector search.
- Understand how to measure the quality of your search across several quality metrics
- Understand how the main parameters in HNSW algorithms affect the relevance and speed of vector search and how to optimally adjust these parameters.
- Experiment with the three major quantization methods, product, scalar, and binary, and learn how they impact memory requirements, search quality, and speed.

By the end of this course, you’ll have a solid understanding of how tokenization is done and how to optimize vector search in your RAG systems.

- Introduction    
- Embedding models
- Role of the tokenizers
- Practical implications of the tokenization
- Measuring Search Relevance
- Optimizing HNSW search    
- Vector quantization    
- Conclusion

- Appendix – Tips and Help