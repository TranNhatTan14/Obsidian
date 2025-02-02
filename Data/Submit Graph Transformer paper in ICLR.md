---
tags:
  - Goal
  - Research
  - Attention
  - Graph
aliases:
  - Identify of bacterial plasmid with assembly graph using Graph Transformer
URL: https://www.overleaf.com/7527286978jcpybvmjgdxt#db3c39
---
Objective

- Advanced Bacterial Plasmid Identification using Graph Transformer

Key Results

1. Develop Graph Transformer model for plasmid assembly graph analysis
- Target: Achieve >90% accuracy in plasmid identification
- Metric: Precision, recall, and F1 score of plasmid detection

2. Preprocessing and graph representation
- Target: Create robust graph embedding method
- Metric: Successful graph transformation and feature extraction

3. Model performance validation
- Target: Comparative analysis with existing plasmid identification methods
- Metric: Benchmark against state-of-the-art tools (e.g., MOB-suite, PlasmidFinder)

4. Generalizability and scalability
- Target: Test model across diverse bacterial datasets
- Metric: Consistent performance across different bacterial species and sequencing platforms

**Success Criteria:** Innovative Graph Transformer approach for accurate and efficient bacterial plasmid identification.

# Problem definition

- DNA assembly to short read to unitig to contig and unitig assembly graph and contig assembly graph
- Identification of plasmids from sequencing data is an important and challenging problem related to antimicrobial resistance spread and other One-Health issues.
- Plasmids can horizontally transmit genetic traits, enabling rapid bacterial adaptation to new environments and hosts.
- Accurate reconstruction of Escherichia coli antibiotic resistance gene (ARG) plasmids from Illumina sequencing data has proven to be a challenge with current bioinformatic tools. In this work, we present an improved method to reconstruct E. coli plasmids using short reads
- Xác định được chính xác plasmid contig từ assembly chỉ từ short-read thay vì long-read
- Tái cấu trúc lại được plasmid

# Abstract

- Most of the task treat contig as independent
- Classification of a contig can be improved from the knowledge of the neighboring node from alignment in the assembly graph
- Use unitig instead of contig to reduce error

# Introduction

There are two major challenges for plasmid identification

- Plasmids exhibit high genetic diversity
- The shared genes or segments between plasmids and chromosomes
- Vấn đề đang gặp phải là số lượng mẫu có thể alignment được với database không nhiều

# Related Work

- Thông tin từ những plasmid đã tìm được (database), những thông tin liên quan đến plasmid và chromosome
- Contig có những đoạn rất ngắn, không liên kết với các contig khác, và không xác định được các giá trị vật lý
- Đoạn chứa thông tin có thể bị cắt ngắn ra làm không xác định được protein, hoặc là có lỗi trong quá trình assembly
- Hiện tại gặp khó khăn đối với các contig ngắn dưới 1000 kb

Alignment-based tools

- Based on the similarities between queries and reference
- For database we can use vector database to query faster. But we need a way to tokenize the query sequence
    
Learning-based tools

- provide a promising alternative for detecting more diverged plasmids via learning abstract patterns beyond sequence similarity.
- Use k-mer freq as the features and applied sequential minimal optimization, fully connected neural network
- PPR-Meta encodes the sequences and the contained codons into one-hot matrices and then trains a CNN model for prediction
- Decreased precision on short contigs, whose length limits the capacity of feature learning
- Can have ambiguous predictions for contigs from shared regions between plasmids and chromosomes

Hybrid
    
- In order to achieve an optimal trade-off between sensitivity and precision, combine homology search and machine learning to identify as many as possible
- PlasmidVerify train a Naive Bayes classifier using protein domain alighment-based feature
- PlasForest using homology search results as features
- Also exhibit decreased accuracy on short contigs
- [[PLASMe]]: treat plasmid as a language defined on a vocabulary of protein. Transformer, to learn the protein importantce and their associations for plasmid
- Plasmids have a large diversity, novel plasmids may contain proteins that cannot be aligned with the current database, leading to inaccurate predictions
- The current tokens contain only proteins of plasmids. Studies have shown that proteins critical for bacterial survival are more likely to be found in chromosomes
- The interpretation of the Transformer identified potentially unannotated PCs that may also play an important role in the life of plasmids

# Method

- Download complete genome and short-read data
## Data preparation

1. **Input Data**:
   - Download Illumina paired-end short-read sequencing data from SRA (Sequence Read Archive).
   - Download complete genomes of target bacteria (e.g., *E. coli*, *K. pneumoniae*, *S. aureus*) from NCBI.
   
1. **Data Preparation**:
   - Perform **assembly** using **metaSPAdes** to generate **unitig assembly graphs**.
   - Extract **contigs** and **unitigs** from the assembly graph.
   
1. **Ground Truth**:
   - Use known plasmid sequences from databases like **PlasmidDB** or **PLSDB**.
   - For novel plasmids, use tools like **PlasmidEC** or **gplas2** to infer plasmid sequences.

## Quality Control

1. Filter by length < 100 bp
2. Alignment with chromosome database to exclude high predict chromosome, markers, ... to get information about gene (both plasmid and chromosome)
4. Extract information from assembly graph
5. Create unitig or assembly graph file

Kết hợp theo 3 hướng

- Alignment
- Graph sử dụng thông tin từ asssembly graph
- Transformer sử dụng token liên quan đến protein đặc trưng cho plasmid và chromosome. Transfer Learning from Natural Language Processing

##  Alignment approach

- Align contigs to known plasmid databases (e.g., PLSDB, plasmidFinder) and ==chromosome database==
- Extract features from alignment results:
    - Percentage of contig aligned
    - Number of hits
    - E-values of hits
    - Coverage of known plasmid genes

- You can also reverse the process, and map your de novo assembly against a reference genome, only containing chromosomal DNA. 
	- Then look at the pieces that don't match, if you get a large (or several) contigs that don't map, have a higher coverage and different GC content, you could be looking at a (or several) plasmid (s). 
	- You can then blast the sequence(s) to see if you find a hit.

## Graph approach

- Mapping the known plasmids of your organism against the de novo assembly. 
	- Plasmid DNA has a higher coverage and different GC content compared to your chromosomal DNA, so this is also a key point that you can look at.
	- So if you get a contig that shows a high similarity to a known plasmid, has a higher coverage and a different GC content than the majority of contigs, you can be quite sure you are looking at a plasmid.
- Relative features
- Additional information encoded in the longer sequences
- Codon usage patterns

### Node features

- Coverage depth
- Sequencing composition
	- GC content [[plASgraph2]] for relative idea
	- k-mer frequencies [[UnitigBIN]]
	- Length of contigs
	- Node connectivity patterns
    
- ==Degree==: The number of edges connected to a node. It helps quantify the importance or centrality of a node in the network.
- **Node Centrality**: Metrics like betweenness centrality, closeness centrality, or eigenvector centrality to quantify the importance of a node within the graph.
- ==Node Embeddings==: Representations learned from node neighborhoods (e.g., using methods like Node2Vec or Graph Neural Networks) to capture node similarities in low-dimensional space.
- K-mer composition
    
### Edge Features
    
- **Edge Weight**: In weighted graphs, edge weights signify the strength of connections between nodes.
- **Edge Betweenness**: Quantifies the number of shortest paths passing through an edge, helping identify bottleneck connections.
- ==Edge Type==: In heterogeneous graphs, edges can represent different types of relationships (e.g., friend vs. colleague in a social network). ==Positive or negative relation==
- Confident of edge like length of the overlap
    
### Graph-Level Features
    
- **Graph Density**: Ratio of the number of edges to the number of possible edges, describing how interconnected the graph is.
- **Graph Diameter**: The longest shortest path between any two nodes, indicating the "spread" of the graph.
- **Average Path Length**: The average distance between pairs of nodes, useful for understanding the graph's compactness.
- **Graph Laplacian**: A matrix representation capturing node connectivity that is useful in spectral graph analysis.

- hai contig noi voi nhau va can kiem tra thong tin lien quan den coverage because of randon fragmentrtion
- One key feature of plasmids is that many are circular. In an assembly graph, if you observe that certain contigs form a **small circular structure**, that’s a strong indication of a plasmid. Tools that detect circularity, such as SPAdes or Unicycler, can identify these loops in the graph and suggest plasmid contigs.

## Binning

## Classification

## Modeling

## Ensemble Approach

- Combine predictions from Transformer and Graph models
## Post-processing

- Filtering: Remove contigs with low prediction scores
- Clustering: Group contigs predicted as plasmids based on their connectivity in the assembly graph and other feature (coverage similarity)
- Validation
- Manual curation of high-confidence predictions
- Experimental validation of novel plasmid predictions

# Evaluation and Validation

- What metrics you use to evaluate performance?
	- Precision/Recall for plasmid identification
	- Accuracy of plasmid boundary determination
	- Robustness to different assembly qualities
- How will you compare your method to existing tools
	- PlasmidSPAdes
	- PlasFlow
	- Other machine learning-based approaches

## Compare with alignment, machine learning, hybrid
## Compare with different length include short contig
## Test in novel contig

# Results

# Conclusion
# Future Work

- Identify both plasmid and chromosome
- Ambiguous label

# References

## Embedding

- [Exphormer: Scaling transformers for graph-structured data](https://research.google/blog/exphormer-scaling-transformers-for-graph-structured-data/)
- [A Generalization of Transformer Networks to Graphs](https://arxiv.org/pdf/2012.09699)
- [Self-Supervised Graph Transformer on Large-Scale Molecular Data](https://proceedings.neurips.cc/paper_files/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf)
- [TORMES: an automated pipeline for whole bacterial genome analysis](https://academic.oup.com/bioinformatics/article/35/21/4207/5430930)
- [MetaGraph: Plasmid/Chromosome Classification Enhancement Using Graph Neural Networks](https://ieeexplore.ieee.org/document/9906285)
- [3CAC: improving the classification of phages and plasmids in metagenomic assemblies using assembly graphs](https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii56/6702013)
- [Plassembler: an automated bacterial plasmid assembly tool](https://academic.oup.com/bioinformatics/article/39/7/btad409/7208863)

## Hybrid

- [https://github.com/rrwick/Trycycler/wiki/Guide-to-bacterial-genome-assembly#2-short-read-qc](https://github.com/rrwick/Trycycler/wiki/Guide-to-bacterial-genome-assembly#2-short-read-qc)

## Binning

- [GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs](https://drops.dagstuhl.de/storage/00lipics/lipics-vol172-wabi2020/LIPIcs.WABI.2020.8/LIPIcs.WABI.2020.8.pdf)
- [Metagenomic binning with assembly graph embeddings](https://academic.oup.com/bioinformatics/article/38/19/4481/6668279)
- [Metagenomic Binning using Connectivity-constrained Variational Autoencoders](https://proceedings.mlr.press/v202/lamurias23a/lamurias23a.pdf)
- [Metagenomic binning with assembly graph embeddings](https://academic.oup.com/bioinformatics/article/38/19/4481/6668279)

---

1. Download the data
2. Clean data
3. Assembly with metaSPAdes
4. 