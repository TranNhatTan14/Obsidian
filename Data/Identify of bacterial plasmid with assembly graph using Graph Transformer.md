---
tags:
  - Research
  - Attention
  - Work
links:
  - "[[PyTorch]]"
  - "[[Conda]]"
  - "[[Nextflow]]"
---
# Purpose and Motivation

- https://www.youtube.com/watch?v=NsdUuXN2SVg
- Reduce cost

# Problem definition

- DNA assembly to short read to unitig to contig and unitig assembly graph and contig assembly graph
- Identification of plasmids from sequencing data is an important and challenging problem related to antimicrobial resistance spread and other One-Health issues.
- Plasmids can horizontally transmit genetic traits, enabling rapid bacterial adaptation to new environments and hosts.
- Accurate reconstruction of Escherichia coli antibiotic resistance gene (ARG) plasmids from Illumina sequencing data has proven to be a challenge with current bioinformatic tools. In this work, we present an improved method to reconstruct E. coli plasmids using short reads
1. Xác định được chính xác plasmid contig từ assembly chỉ từ short-read thay vì long-read
2. Tái cấu trúc lại được plasmid

# Goal

- Use assembly graph (unitig or contig) as input and use GraphTransformer for better result
	- Use graph edge update compare with plASgraph
	- Use Graph Transformer for better 
- No need to train specific model for each specie like PLASMe
- Can handle short contig (contig between 100 - 1000 bp)

# Roadmap

- Contig assembly graph with [[Graph Neural Networks]] with additional information from alignment
- Contig assembly graph with [[Graph Transformer]]
# Tasks

- Handle short contig
	- First focus on contig longer than 1000 bp
- Prepare data
	- I have data for 
- Prepare features
- Identify

## Alignment and Binning

## Modeling

- Dữ liệu đầu vào là graph file with node is contig and edge is overlap sequence
	- Type of graph file. Better is short-read assembly graph or unitig assembly graph instead of contig assembly graph
	- Convert from graph filie to FASTA file (I know some tool can do this or we can use pipeline, I think we will have)
	- Extract node features and edge features
		- Node features
			- Coverage and GC content
		- Edge features (like UnitigBin)
			- Positive and negative edge
			- Confident of edge

## Testing

- Testing result with and without alignment

# Problems

- Vấn đề đang gặp phải là số lượng mẫu có thể alignment được với database không nhiều

# Abstract

- Most of the task treat contig as independent
- Classification of a contig can be improved from the knowledge of the neighboring node from alignment in the assembly graph
- Use unitig instead of contig to reduce error

# Introduction

Considerations and Best Practices

There are two major challenges for plasmid identification

- Plasmids exhibit high genetic diversity
- The shared genes or segments between plasmids and chromosomes

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
- PLASMe: treat plasmid as a language defined on a vocabulary of protein. Transformer, to learn the protein importantce and their associations for plasmid
- Plasmids have a large diversity, novel plasmids may contain proteins that cannot be aligned with the current database, leading to inaccurate predictions
- The current tokens contain only proteins of plasmids. Studies have shown that proteins critical for bacterial survival are more likely to be found in chromosomes
- The interpretation of the Transformer identified potentially unannotated PCs that may also play an important role in the life of plasmids

# Method

- Download complete genome and short-read data
- The data for testing

## Data preparaion

## Quality Control

1. Filter by length < 100 bp
2. Alignment with chromosome database to exclude high predict chromosome, markers, ... to get information about gene (both plasmid and chromosome)
3. Use SPdes, Unicycle, SKESA to create assembly graph for bacterial genomes
4. Extract information from assembly graph


Kết hợp theo 3 hướng

- Alignment
- Graph sử dụng thông tin từ asssembly graph
- Transformer sử dụng token liên quan đến protein đặc trưng cho plasmid và chromosome. Transfer Learning from [[Natural Language Processing]]

##  Alignment

- Align contigs to known plasmid databases (e.g., PLSDB, plasmidFinder) and ==chromosome database==
- Extract features from alignment results:
    - Percentage of contig aligned
    - Number of hits
    - E-values of hits
    - Coverage of known plasmid genes

- You can also reverse the process, and map your de novo assembly against a reference genome, only containing chromosomal DNA. 
	- Then look at the pieces that don't match, if you get a large (or several) contigs that don't map, have a higher coverage and different GC content, you could be looking at a (or several) plasmid (s). 
	- You can then blast the sequence(s) to see if you find a hit.

## Binning

- Check database in this step

## Classification

- Use data features and information from Binning step

==Change SAMN05729957 to SAMN31007786==

- Dữ liệu đầu vào
	- để có thể phổ biến nhất thì là 2 file FASTQ short-read sequences
	- Assembly graph file
- Quanlity control
- Create unitig or assembly graph file

## Transformer Model

### Tokenization

Transformer can capture the correlation between tokens and alleviate the long-time memory loss problem. However, unlike natural language, when modeling biological sequences as a language , it is not trivial to determine the best vocabulary (token set). 

- All the proteins, amino acids or k-mers can be used to consruct the token set and each of them has its advantages and drawbacks.
- PLASMe paper consider different sets of vocabulary and determine the best one emprically
- Nucleotide level
- Protein level
	- Protein clusters: This token set comprises protein clusters from plasmid
	- The protein domains or curated set of genes are more improtant features than the "physical" features of the sequence (such as GC content)

1. Use Prodigal to predict all the protein from the reference plasmid ==(improve with use of reference chromosome)==
2. Use DIAMOND to do an all-against-all alignment on the proteins
3. Construct a graph where the nodes are proteins, and the edges represent pairwise alignment with the e-value below 1e-5
4. Apply Markow clustering to cluster these proteins into PCs
5. Only the clusters containing at least two proteins will be kept, leading to 151086 PCs
6. Set the length of the encode vector to 400 which can cover 99.9% of the plasmids in the database
7. Use the mask token (with a token ID of 0) to indicate the position of the padding and use an unknown protein token (with a token ID of 1) to represent the unknown proteins

During the prediction stage, we first predict the protein in the query sequence using Prodigal and align them to reference plasmid proterins in PCs using DIAMOND PLASTTP
Then we encode the vector with the index of the aligned PCs
We set the stringent thresholds for the alignment of PCs

PC-based token achieved the best precision, recall and F1-score

- Using PCs as the tokens allows Transformer to learn the importantce of protein directly
- Can capture the correlation between different proterin on the contig

**Interpreting the performance of Transformer**

- plasmids’ core genes play an essential role in Transformer’s prediction
- Among of them, 23 have protein function annotations, and 12 are related to plasmid core genes: 5 are about conjugation, 4 about transposases, 2 about partitioning and 1 about replication
- Conjugation proteins are responsible for the horizontal gene transfer between bacteria, while the spread of AMR and virulence factors can help hosts improve their adaptability to the environment.
- The function analysis indicated that these tokens were also associated with the core functions of plasmids.
- However, PC-level tokenization also has some limitations, as it is more prone to out-of-vocabulary (OOV) issues. Therefore, for newer plasmids, using PC tokens may lead to false negatives.

- Input: Sequence data and alignment features
- Architecture: BERT-like model pre-trained on plasmid and chromosomal sequences
- Fine-tune on labeled plasmid data
- Output: Probability of contig being plasmid-derived

## Graph Neural Network

- Construct graphs based on:
    - Sequence similarity between contigs
    - Shared genomic features
- Node features: Sequence composition and alignment features
- Edge features: Similarity scores, shared gene content
- Use Graph Convolutional Networks (GCN) or Graph Attention Networks (GAT)
- Output: Classification of nodes (contigs) as plasmid or chromosomal

## Ensemble Approach

- Combine predictions from Transformer and Graph models

## Post-processing and Validation

- Manual curation of high-confidence predictions
- Experimental validation of novel plasmid predictions

# Data

- Download short-reads from SRA and complete genome from NCBI for ==3 species==
- Handle hybrid assemblies if using multiple sequencing technologies

- Use Illumina sequencing technology for generating the raw reads
- Which assembler will you use to generate the assembly graphs (SPAdes, Unicycler, metaSPAdes)?
- Do you have a specific bacterial species/genus in focus, or is this meant to be a general-purpose tool?
	- E. Coli
	- K.
	- S. 
- How will you handle hybrid assemblies if using multiple sequencing technologies?

- How will you define ground truth for training [[PlasmidEC and gplas2]]
	- Will you use known plasmid sequences from databases like PlasmidDB
	- How will you handle novel plasmid (it mean we can't align to database)
- What specific plasmid characteristics are you planning to leverage
	- Circular nature of plasmids
	- Presence of plasmid-specific genes (rep genes, mob genes)
	- Size distributions

# Features

- Mapping the known plasmids of your organism against the de novo assembly. 
	- Plasmid DNA has a higher coverage and different GC content compared to your chromosomal DNA, so this is also a key point that you can look at.
	- So if you get a contig that shows a high similarity to a known plasmid, has a higher coverage and a different GC content than the majority of contigs, you can be quite sure you are looking at a plasmid.
- Relative features
- Additional information encoded in the longer sequences
- Codon usage patterns

## Node features

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
- Node coverage
    
## Edge Features
    
- **Edge Weight**: In weighted graphs, edge weights signify the strength of connections between nodes.
- **Edge Betweenness**: Quantifies the number of shortest paths passing through an edge, helping identify bottleneck connections.
- ==Edge Type==: In heterogeneous graphs, edges can represent different types of relationships (e.g., friend vs. colleague in a social network). ==Positive or negative relation==
    
## Graph-Level Features
    
- **Graph Density**: Ratio of the number of edges to the number of possible edges, describing how interconnected the graph is.
- **Graph Diameter**: The longest shortest path between any two nodes, indicating the "spread" of the graph.
- **Average Path Length**: The average distance between pairs of nodes, useful for understanding the graph's compactness.
- **Graph Laplacian**: A matrix representation capturing node connectivity that is useful in spectral graph analysis.

- hai contig noi voi nhau va can kiem tra thong tin lien quan den coverage because of randon fragmentrtion
- One key feature of plasmids is that many are circular. In an assembly graph, if you observe that certain contigs form a **small circular structure**, that’s a strong indication of a plasmid. Tools that detect circularity, such as SPAdes or Unicycler, can identify these loops in the graph and suggest plasmid contigs.

# Evaluation and Validation

- Compare with alignment, machine learning, hybrid
- Compare with different length include short contig
- Test in novel contig

- What metrics you use to evaluate performance?
	- Precision/Recall for plasmid identification
	- Accuracy of plasmid boundary determination
	- Robustness to different assembly qualities
- How will you compare your method to existing tools
	- PlasmidSPAdes
	- PlasFlow
	- Other machine learning-based approaches

The Transformer identified more plasmid than BLAST
The top 3 tools are all ==hybrid method== that combine machine learning and features derived from protein alignment 

Combining deep learning and homology search to identify plasmids in short-read assemblies.
==Identify what is plasmid and what is NOT plasmid (chromosome)==
Contigs that are highly similar to known  plasmid are directly classified as plasmid. Inputs that share somewhat similarities are examined by the deep learning component in PLASME
Construct the plasmid protein clusters as vocabulary and then used Transformer to learn the important of proteins and correlation between them
By interpreting Transformer, we found that the more important tokens for identifying plasmids were associated with plasmid were associated with plasmid core genes.
Overall, PLASME can quickly and accurately identify plasmids in assembled contigs

Short contigs tend to contain more false positives. Due to thte horizontal gene transfer between chromosomes and plasmid, identifying plasmid from short sequeces may result in false positive. Thus, idnetifying the fragment plasmid sequences remain a challenging task
PLASMe had the best performance on identifying short plasmid.
PLASMe will output the identified plasmids with marking the starting and ending position in an input sequence if it can be aligned to chromosomal genomes with high similarity
==User can use our prediction and the marked region to further screen false positive using their domain knowledge about the data/sample.==

PC-level token is better at learning the importance of different proteins and the relationship between them
==This use PC-level, I think we don't use PC instead we use protein unique for plasmid and chromosome==

For longer sequences. using protein as tokens and embedding them into vectors result in much shorter vectors than those generated by k-mer or BPE
Using shorter input vectors can reduce the model complexity which helps model trianing on a GPU
However PC-clustering tokenization also help some limiatation as it is more prone to OOV isssues. Therefore, for newer plasmid, using PC tokens may lead to false negatives

# Results

# Conclusion
# Future Work

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

# Q&A

==Should we identify only plasmid or both plasmid, chromosome, ambiguous==

- Benefit of ambiguous can see in plASgraph2

==Differences between Plasmids and Chromosomes==

Plasmids

- Typically ==**small**, circular== pieces of DNA.
- Often carry genes that provide **adaptive advantages**, such as antibiotic resistance or toxin production.
- Replicate independently of the host’s chromosomal DNA.
- Found in bacteria and sometimes in eukaryotes.
- Contain fewer genes compared to chromosomes, often coding for **non-essential** functions.

Chromosomes

- **Larger** in size, usually linear in eukaryotes (but circular in prokaryotes).
- Contain **essential genes** required for cell growth, division, and survival.
- Replicate as part of the organism's regular cell cycle.
- Carry regulatory regions like **promoters, enhancers**, and **silencers** for controlling gene expression.

- Sequeces Composition
	- GC content: Plasmids and chromosomes from the same species may have different GC content. (but when split into contig this information maybe change, how about relatives in plASgraph2
- k-mers
	- 3-5 k-mers can help capture specific motifs or sequence patterns that are more frequent in plasmid (antibiotic resistance genes) or chromosome (essential genes)

==What features we can extract from sequence related to plasmid and chromosome==

==Trong cùng một bộ gene thì có khoảng bao nhiêu plasmid và sequence của plasmid có giống nhau không==

Higher coverage depth usually indicates plasmid contigs, while more consistent coverage suggests chromosome contigs.
Plasmids may have different GC content compared to the chromosome.
Chromosome contigs are typically much longer than plasmid contigs.

Gene content analysis:

- Look for plasmid-specific genes (e.g., replication initiation proteins, mobilization proteins).
- Search for essential chromosomal genes (e.g., ribosomal proteins, DNA polymerase).

Machine learning approaches
Use features like k-mer frequencies, coverage, and GC content to train classifiers.

The confidence of edges in assembly graph can be evaluated through several factors:

Let me help you understand edge confidence in assembly graphs and strategies to improve it, drawing from my bioinformatics expertise.

The confidence of edges in assembly graphs can be evaluated through several factors:

1. Read Support
- Coverage depth at the overlap region
- Consistency of read pairs spanning the connection
- Quality scores of the supporting reads

2. Overlap Characteristics
- Length of overlap between contigs
- Sequence similarity in the overlap region
- Presence of repetitive elements