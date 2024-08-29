---
tags:
  - Status/InProgress
links:
  - "[[Project]]"
---
Transfer Learning from [[Natural Language Processing]], [[Machine Learning Workflow]]

# Problem definition

Pros

Ban đầu là chuỗi ADN được cắt nhỏ thành từng đoạn read nhỏ, từ những đoạn contig sẽ được xác định overlap để tạo lên contig. Tiếp tục overlap chúng ta sẽ tạo được assembly graph bao gồm các liên kết giữa các contig

Có những thông tin từ những plasmid đã tìm được, những thông tin liên quan đến plasmid và chromosome

Cons

- Contigs có những đoạn rất ngắn, không có liên kết với các contig khác và không xác đinh được các giá trị như GC, ...
- Đoạn chứa thông tin có thể bị cắt ngắn ra làm không xác định được hoặc là đoạn có lỗi trên quá trình assembly

### Sequence assembly

# System Design

## Input

Input đầu vào là file có thể là fasta
## Function

Processing to assembly - QC - Extract features - Query - Classify with multiple model to increase confidence - Testing with existing model

## Output

Label kết quả từng contig theo 3 nhóm p c ambigous

(Optional) Rebuild data

# Data 

Start with data from 

# Workflow

# Data collection

## Data storage

(Optional) Store data in graph database or vector database
## QC

QC giống như tiền xử lý 









































- Thu thập dữ liệu tìm tất cả complete genomes của một loài từ cơ sở dữ liệu GeneBank
	- E. coli
	- K. pneumoniea
	- S. aureus
- Xác định được sequence nào là chromosome và plasmid
- Mô phỏng lại quá trình giải trình tự gene sử dụng ART
- Chạy genome assembly trên dữ liệu mô phỏng sẽ tạo ra assembly graph
- Map contig vào trong genome thì mình sẽ biết được nguồn gốc 






Ứng dụng transformer vào trong bài toán cụ thể là plasmid

1. Từ bộ gene hoàn chỉnh
2. Tạo thành các contig từ short-read
3. Chuyển đổi giữa assembly graph và dạng độc lập fasta
4. Alignment các contig vào database để xác định đâu là contig với độ chính xác cao (Hiện tại theo mình biết thì các phương pháp align chủ yếu tập trung vào nhận diện các gene trên plasmid))
    
    <aside> 💡 Thêm cách để nhận diện gene trên chromosome
    
    </aside>
    
5. Từ thông tin liên quan để xác định thêm đâu là contig
6. Tokenize thông tin liên quan đến plasmid và liên quan đến chromosome (PC)
7. Tìm ra các gene đặc thù cho vi khuẩn bằng cách tokenize từ Transformer
8. Mô phỏng lại bộ gene hoàn chỉnh của vi khuẩn (Đoạn CHR or PLM đúng ra thì phải có 2 mạch, tìm vế tương ứng để sửa những điểm sai)
9. Test
    1. Chạy dữ liệu trên platon và PLASMe

---

### Analysis

306 edges

- chromosome,chromosome 109
- chromosome,plasmid 0
- chromosome,unlabeled: 70
- chromosome,ambiguous 4

- plasmid,chromosome 0
- plasmid,plasmid 51
- plasmid,ambiguous 2
- plasmid,unlabeled 24

- unlabeled,unlabeled 12
- unlabeled,plasmid 6
- unlabeled,chromosome 20
- unlabeled,ambiguous 0

- ambiguous,ambiguous 1
- ambiguous,plasmid
- ambiguous,chromosome 1
- ambiguous,unlabeled 4

# Abstract

Most of the task treat contig as independent, but the relation (edge) connect with different contig (had detected as plasmid is also important information)

- Classification of a contig can be improved from the knowledge of the classification of the neighboring contigs in the assembly graph

1. Check độ chính xác của việc align, mình có thể tăng ngưỡng
2. Từ SPdes, IUnicycler v0.5.0 (Wick et al., 2017) and SKESA v2.4.0 (Souvorov et al., 2018), two widely used assemblers for bacterial genomes that provide an assembly graph, thus leading to two data sets per isolate… xác định xem các contig kết nối có chính xác là plasmid không?
3. Mình sẽ lấy thông tin này thế nào (lấy trung bình hay sao)

**shaw-2021_cfre-SAMN15148288-s.gfa.csv**

<aside> 💡 Platon dự đoán được 15/16 plasmid. Phần lớn các contig kết nối với n thì đúng là plasmid Xác đinh được contig này là plasmid với độ tự tin bao nhiêu thì kết quả kéo theo sẽ như vậy

</aside>

# Introduction

There are two major challenges for plasmid identification

1. Plasmids exhibit high genetic diversity
2. The shared genes or segments between plasmids and chromosomes

Tools

1. Graph-based tools
    
    Attempted to reconstruct plasmid underlying assembly graph
    
[https://github.com/cchauve/plASgraph2](https://github.com/cchauve/plASgraph2)
    
Rely on read coverage and cyclic topology for plasmid assembly, which is best used to find relatively comple plasmid rather than short contig
    
2. Alignment-based tools
    
    based on the similarities between queries and reference
    
    <aside> 💡 For database we can use vector database to query faster. But we need a way to tokenize the query sequence
    
    </aside>
    
3. Learning-based tools
    
    provide a promising alternative for detecting more diverged plasmids via learning abstract patterns beyond sequence similarity.
    
    Use k-mer freq as the features and applied sequential minimal optimization, fully connected neural network
    
    PPR-Meta encodes the sequences and the contained codons into one-hot matrices and then trains a CNN model for prediction
    
    <aside> 💡 Decreased precision on short contigs, whose length limits the capacity of feature learning
    
    </aside>
    
    Can have ambiguous predictions for contigs from shared regions between plasmids and chromosomes
    
4. Hybrid
    
    In order to achieve an optimal trad-off between sensitivity and precision, combine homology search and machine learning to identify as many as possible
    
    PlasmidVerify train a Naive Bayes classifier using protein domain alighment-based feature
    
    PlasForest using homology search results as features
    
    <aside> 💡 Also exhibit decreased accuracy on short contigs
    
    </aside>
    
    PLASMe: treat plasmid as a language defined on a vocabulary of protein. Transformer, to learn the protein importantce and their associations for plasmid
    
    > Train for each order
    

# Data

# Alignment

### Embedding

[https://academic.oup.com/mbe/article/32/12/3079/2579220?login=false](https://academic.oup.com/mbe/article/32/12/3079/2579220?login=false)

### Features

- K-mer
- Dùng log length để làm gì mình không nhớ
- Relative features
- Additional information encoded in the longer sequences

# Modeling

Kết hợp theo 3 hướng

- Alignment
- Graph
- Transforme

**The Graphormer is a graph classification model.**

Transformer for Graphs: An Overview from Architecture Perspective

A Generalization of Transformer Networks to Graphs

Dựa trên thông tin về những contig xung quanh

Thông tin từ contig xung quanh gì có thể ảnh hưởng đến kết quả

# Result

**Performancs of different token sets**

PC-based token achieved the best precision, recall and F1-score

- Using PCs as the tokens allows Transformer to learn the importantce of protein directly
- Can capture the correlation between different proterin on the contig

**Interpreting the performance of Transformer**

- plasmids’ core genes play an essential role in Transformer’s prediction
- Among of them, 23 have protein function annotations, and 12 are related to plasmid core genes: 5 are about conjugation, 4 about transposases, 2 about partitioning and 1 about replication
- Conjugation proteins are responsible for the horizontal gene transfer between bacteria, while the spread of AMR and virulence factors can help hosts improve their adaptability to the environment.
- The function analysis indicated that these tokens were also associated with the core functions of plasmids.
- However, PC-level tokenization also has some limitations, as it is more prone to out-of-vocabulary (OOV) issues. Therefore, for newer plasmids, using PC tokens may lead to false negatives.

## Future Work

- First, because plasmids have a large diversity, novel plasmids may contain proteins that cannot be aligned with the current database, leading to inaccurate predictions
- Second, the current tokens contain only proteins of plasmids. Studies have shown that proteins critical for bacterial survival are more likely to be found in chromosomes
- Third, the interpretation of the Transformer identified potentially unannotated PCs that may also play an important role in the life of plasmids

<aside> 💡 Thay vì chỉ tập trung vào đặc điểm plasmid có (gene, protein tren do), tap trung them vao nhung gen co trong bacterial ma khong co trong plasmid (như là hình của biểu đồ ven)

</aside>

# Resources

[https://research.google/blog/exphormer-scaling-transformers-for-graph-structured-data/](https://research.google/blog/exphormer-scaling-transformers-for-graph-structured-data/)

- [A Generalization of Transformer Networks to Graphs](https://arxiv.org/pdf/2012.09699)
- [Self-Supervised Graph Transformer on Large-Scale Molecular Data](https://proceedings.neurips.cc/paper_files/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf)
- [TORMES: an automated pipeline for whole bacterial genome analysis](https://academic.oup.com/bioinformatics/article/35/21/4207/5430930)
- [PLASMe: a tool to identify PLASMid contigs from short-read assemblies using transformer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10450166/pdf/gkad578.pdf)
- [MetaGraph: Plasmid/Chromosome Classification Enhancement Using Graph Neural Networks](https://ieeexplore.ieee.org/document/9906285)
- [plASgraph2: using graph neural networks to detect plasmid contigs from an assembly graph](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1267695/full)
- [3CAC: improving the classification of phages and plasmids in metagenomic assemblies using assembly graphs](https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii56/6702013)
- [Plassembler: an automated bacterial plasmid assembly tool](https://academic.oup.com/bioinformatics/article/39/7/btad409/7208863)
- [Why There Are No Essential Genes on Plasmids](https://academic.oup.com/mbe/article/32/12/3079/2579220?login=false)

[https://github.com/rrwick/Trycycler/wiki/Guide-to-bacterial-genome-assembly#2-short-read-qc](https://github.com/rrwick/Trycycler/wiki/Guide-to-bacterial-genome-assembly#2-short-read-qc)

- Temp
    
    **GNNs as Auxiliary Modules**
    
    - Directly inject GNNs into Transformer architecture.
    - Types
        - Build Transformer blocks on top of GNN blocks
        - Stack GNN blocks and Transformer blocks in each layer
        - Parallel GNNs blocks and Transformer block in each layer
    
    **Improved Positional Embedding from Graphs**
    
    Đây là dự định ban đầu khi thêm features trước khi sử dụng Transformer
    
    - Compress the graph structure into positional embedding vectors
    - Add them to the input before it fed to the vanilla Transformer model
    - This graph positional embedding can be derived from the structural information of graphs, such as degree and centrality
    
    **Improved Attention Matrices from Graphs**
    
    **GNNs as Auxiliary Modules**
    
    - Directly inject GNNs into Transformer architecture.
    - Types
        - Build Transformer blocks on top of GNN blocks
        - Stack GNN blocks and Transformer blocks in each layer
        - Parallel GNNs blocks and Transformer block in each layer
    
    **Improved Positional Embedding from Graphs**
    
    Đây là dự định ban đầu khi thêm features trước khi sử dụng Transformer
    
    - Compress the graph structure into positional embedding vectors
    - Add them to the input before it fed to the vanilla Transformer model
    - This graph positional embedding can be derived from the structural information of graphs, such as degree and centrality
    
    **Improved Attention Matrices from Graphs**
    
    - Inject graph priors into the attention computation via graph bias terms, or restrict a node only attending to local neighbours in the graph, which can be computationally formulated as an attention masking machanism

[Transformer as a Graph Neural Network — DGL 2.2 documentation](https://docs.dgl.ai/en/latest/tutorials/models/4_old_wines/7_transformer.html)

[Transformers are Graph Neural Networks | NTU Graph Deep Learning Lab](https://graphdeeplearning.github.io/post/transformers-are-gnns)

[The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html)

---
# [Contig](https://www.genome.gov/genetics-glossary/Contig)

A contig (as related to genomic studies; derived from the word “contiguous”) is a set of DNA segments or sequences that overlap in a way that provides a contiguous representation of a genomic region. For example, a clone contig provides a physical map of a set of cloned segments of DNA across a genomic region, while a sequence contig provides the actual DNA sequence of a genomic region.

![contig](https://www.genome.gov/sites/default/files/media/images/tg/Contig.jpg)

**“Reads” are small segments of nucleic acid sequence produced by a sequencing instrument (there are many kinds).** **“Contigs” represent contiguous sequence formed by assembling the reads**

A genome is typically studied by breaking down its DNA into pieces, analyzing those pieces in the laboratory, and then computationally putting those pieces back together in a conceptual way. Years ago, before genome sequencing became routine, the pieces of DNA would first be cloned and then individual clones would be analyzed to determine which clones overlapped which other clones. A set of overlapping clones that together contain a ‘contiguous’ region of a genome is called a contig – or in this case a clone contig. Genome sequencing uses the concept of a contig, but in a different way. For genome sequencing, the pieces are not actually physical segments of DNA but rather are stretches of generated DNA sequence (often called a sequence read). By establishing the overlaps among a set of sequence reads, one can assemble a sequence contig, from which the actual sequence of the genomic region can be deduced.

https://www.quora.com/What-are-reads-and-contigs-file-formats-bioinformatics#:~:text=%E2%80%9CReads%E2%80%9D%20are%20small%20segments%20of,formed%20by%20assembling%20the%20reads.
https://www.biostars.org/p/9510018/
https://www.researchgate.net/post/How-to-find-plasmid-sequence-from-contigs

---

### Other tools can help identify plasmid contigs

Kraken

Can assign taxonomy IDs to contigs, indicating whether they are on mobile genetic elements that can be found on chromosomes or plasmid

Plasmer

Can learn from contigs of various lengths by sliding chromosome and plasmid sequences into different window size
https://www.biostars.org/p/9510018/

---

### Structured approach to efficiently retrieve plasmid sequences from contigs, ensuring a comprehensive analysis of sequencing data

The process of identifying plasmid sequences within contigs generated from sequencing projects ==involves== a combination of bioinformatics tools and databases. This approach facilitates the differentiation of chromosomal and plasmid DNA, allowing for the accurate assembly and annotation of plasmid sequences.

Step-by-Step Guide

1. **Quality Assessment and Assembly**:Initially, assess the quality of your raw sequencing data using tools such as FastQC. Utilize assembly software (e.g., SPAdes, Velvet) to generate contigs from your sequencing reads. This process will compile both chromosomal and plasmid-derived sequences.
2. **Contig Classification**:Employ contig classification tools (e.g., PlasmidFinder, PlasFlow) to distinguish between chromosomal and plasmid contigs. These tools utilize databases of known plasmid sequences and machine learning algorithms to predict the origin of contigs.
3. **Database Comparison**:Compare your identified plasmid contigs against plasmid databases (e.g., NCBI's Plasmid Database, PATRIC) using BLAST or similar sequence alignment tools. This step helps to identify known plasmid sequences and assign potential functions to the contigs.
4. **Plasmid Assembly (if necessary)**:For fragmented plasmid sequences scattered across multiple contigs, consider using specialized assembly tools designed for plasmid reconstruction (e.g., plasmidSPAdes) to generate complete plasmid sequences.
5. **Annotation**:Annotate the assembled plasmid sequences using tools such as Prokka or RAST to identify genes, resistance markers, and other functional elements within the plasmid DNA.
6. **Verification and Validation**:Where possible, verify the assembled plasmid sequences through comparison with known plasmids or experimental validation methods, such as PCR, to confirm the presence of specific genes or sequences.

Considerations and Best Practices

- **Database Utilization**: Regularly update your database references to include the latest known plasmid sequences for improved accuracy in classification and annotation.
- **Cross-Validation**: Use multiple tools and databases for contig classification and annotation to cross-validate your results and increase confidence in the identified plasmid sequences.
- **Experimental Confirmation**: Whenever feasible, complement bioinformatic predictions with experimental validation to confirm the existence and structure of plasmids within your samples.