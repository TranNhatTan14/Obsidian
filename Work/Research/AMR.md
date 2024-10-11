- [ ] Phân tích khả năng của việc sử dụng thông tin liên quan đến kết nối của các contig,  lựa chọn tham số tối ưu của BLAST cho kết quả tốt nhất
	==Vấn đề đang gặp phải là số lượng mẫu có thể alignment được với database không nhiều==
- [ ] Test kết quả đầu ra nếu thêm thông tin về alignment
- [ ] Thêm thông tin liên quan đến protein trên chromosome xem kết quả có cải thiện không

# Problem definition

Ban đầu là chuỗi ADN được cắt nhỏ thành từng đoạn read nhỏ, từ những đoạn contig sẽ được xác định overlap để tạo lên contig. Tiếp tục overlap chúng ta sẽ tạo được assembly graph bao gồm các liên kết giữa các contig. 

# Literature Review

- Thông tin từ những plasmid đã tìm được (database), những thông tin liên quan đến plasmid và chromosome
- Contig có những đoạn rất ngắn, không liên kết với các contig khác, và không xác định được các giá trị vật lý
- Đoạn chứa thông tin có thể bị cắt ngắn ra làm không xác định được protein, hoặc là có lỗi trong quá trình assembly

# Abstract

- Most of the task treat contig as independent, but the relation (edge) connect with different contig (had detected as plasmid is also important information)
- Classification of a contig can be improved from the knowledge of the classification of the neighboring contigs in the assembly graph
- Check độ chính xác của việc align, mình có thể tăng ngưỡng
- Từ SPdes, IUnicycler v0.5.0 (Wick et al., 2017) and SKESA v2.4.0 (Souvorov et al., 2018), two widely used assemblers for bacterial genomes that provide an assembly graph, thus leading to two data sets per isolate… xác định xem các contig kết nối có chính xác là plasmid không?
- Mình sẽ lấy thông tin này thế nào (lấy trung bình hay sao)

 Platon dự đoán được 15/16 plasmid. Phần lớn các contig kết nối với n thì đúng là plasmid Xác đinh được contig này là plasmid với độ tự tin bao nhiêu thì kết quả kéo theo sẽ như vậy

# Introduction

There are two major challenges for plasmid identification

- Plasmids exhibit high genetic diversity
- The shared genes or segments between plasmids and chromosomes
- Dựa trên thông tin về những contig xung quanh
- Thông tin từ contig xung quanh gì có thể ảnh hưởng đến kết quả

# Method

Xác định chính xác những contig nào được align là plasmid với độ chính xác cao, thông tin này có thể không sử dụng trong quá trình huấn luyện nhưng sử dụng trong quá trình phía sau giúp tăng hiệu quả của mô hình.

Kết hợp theo 3 hướng

- Alignment
- Graph sử dụng thông tin từ asssembly graph
- Transformer sử dụng token liên quan đến protein đặc trưng cho plasmid và chromosome. Transfer Learning from [[Natural Language Processing]]
### QC

1. Filter by length
	1. Can we have hypothesis for with length to filter 
2. Alignment with chromosome database to exclude high predict chromosome
	1. Use information from assembly graph to exclude connect contigs
3. Alignment with plasmid database 
- Xác định được sequence nào là chromosome và plasmid
- Mô phỏng lại quá trình giải trình tự gene sử dụng ART
- Chạy genome assembly trên dữ liệu mô phỏng sẽ tạo ra assembly graph
- Map contig vào trong genome thì mình sẽ biết được nguồn gốc 

##  Alignment

- Align contigs to known plasmid databases (e.g., PLSDB, plasmidFinder) and ==chromosome database==
- Extract features from alignment results:
    - Percentage of contig aligned
    - Number of hits
    - E-values of hits
    - Coverage of known plasmid genes

- Mapping the known plasmids of your organism against the de novo assembly. 
	- Usually, plasmid DNA has a higher coverage and different GC content compared to your chromosomal DNA, so this is also a key point that you can look at. 
	- So if you get a contig that shows a high similarity to a known plasmid, has a higher coverage and a different GC content than the majority of contigs, you can be quite sure you are looking at a plasmid.
- You can also reverse the process, and map your de novo assembly against a reference genome, only containing chromosomal DNA. 
	- Then look at the pieces that don't match, if you get a large (or several) contigs that don't map, have a higher coverage and different GC content, you could be looking at a (or several) plasmid (s). 
	- You can then blast the sequence(s) to see if you find a hit.

## Analysis

- Hypothesis
	- Align được contig nào là plasmid (chromosome) thì khả năng cao là những contig kết nối là plasmid (chromosome)

- Keep only contig in range 1000 - 350,000 base pairs
- FASTA to GFA
- Process FASTA with BLAST
	- Query data in database for both plasmid and chromosome
- Extract features to use
- Classify with multiple model to increase confidence using CV
- Testing with existing model

## Features

- K-mer
- Dùng log length để làm gì mình không nhớ
- Relative features
- Additional information encoded in the longer sequences
- **Length**: 40,103 base pairs
- **Coverage**: 8.6x (from assembly)

### Results

PC-based tokens achieved the best precision, recall, and F1-score
- Using PCs as the tokens allows Transformers to learn the important of proteins directly
- PC-based Transformer can capture the correlation between different proteins on the contig
Those protein-originated features are more critical for plasmid identification

The Transformer identified more plasmid than BLAST
The top 3 tools are all ==hybrid method== that combine machine learning and features derived from protein alignment 

Deeplasmid has difficulties recognizing short plasmid contig

test plasmid of lengths between 1000 and 3000, which account for about 5.58% of the dataset
All command used by each tools can be found in ==Supplementary Table S5==

The learning based tools achieve higher recall. and the alignment-based methods achieve higher precision
The learning based approach can be more sensitve to remote homologous sequences by capturing sequence patterns
The alignment-based methods usually set stringent alignment threshold to reduce the false positive, leading to high presision but low recall

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



As an expert in genomics focusing on bacterial and plasmid identification, I can suggest a robust approach for identifying plasmid contigs. Here's a concise overview of an effective method:

1. Assembly: Start with high-quality genome assembly, preferably using long-read sequencing data (e.g., PacBio or Nanopore) combined with short-read data for error correction.
2. Initial contig classification:
    - Use tools like PlasFlow or PlasClass to predict plasmid-derived contigs based on sequence composition.
    - Examine circular contigs, as many plasmids are circular.
3. Sequence analysis:
    - Search for plasmid-specific markers (e.g., rep genes, mobilization genes, conjugation genes).
    - Use databases like PlasmidFinder to identify known plasmid replicons.
4. Coverage analysis:
    - Compare read depth of putative plasmid contigs to chromosomal contigs. Plasmids often have different copy numbers.
5. Annotation and comparative genomics:
    - Annotate contigs and look for plasmid-associated genes.
    - Compare to known plasmid sequences using tools like BLAST or PLSDB.
6. Experimental validation:
    - PCR amplification of plasmid-specific regions.
    - Plasmid extraction and gel electrophoresis.
7. Integration of results:
    - Combine computational predictions with experimental evidence for final classification.

## Sequence Composition Analysis

- Calculate k-mer frequencies
- GC content
- Codon usage patterns

## AI-based Classification

### Transformer Model:

#### Tokenization

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

#### Embedding

[https://academic.oup.com/mbe/article/32/12/3079/2579220?login=false](https://academic.oup.com/mbe/article/32/12/3079/2579220?login=false)

### Graph Neural Network:

- Construct graphs based on:
    - Sequence similarity between contigs
    - Shared genomic features
- Node features: Sequence composition and alignment features
- Edge features: Similarity scores, shared gene content
- Use Graph Convolutional Networks (GCN) or Graph Attention Networks (GAT)
- Output: Classification of nodes (contigs) as plasmid or chromosomal

## Ensemble Approach

- Combine predictions from Transformer and Graph models
- Integrate with traditional methods (e.g., PlasFlow, PlasClass) for robust prediction

## Post-processing and Validation

- Manual curation of high-confidence predictions
- Experimental validation of novel plasmid predictions

# Data

- Data in FASTA and GFA format in plASgraph2 dataset
- First we can only focus on: E. coli, K. pneumoniea, S. aureus

## Assembly graph

- hai contig noi voi nhau va can kiem tra thong tin lien quan den coverage because of randonfragmentrtion
- One key feature of plasmids is that many are circular. In an assembly graph, if you observe that certain contigs form a **small circular structure**, that’s a strong indication of a plasmid. Tools that detect circularity, such as SPAdes or Unicycler, can identify these loops in the graph and suggest plasmid contigs.

# Evaluation

- Compare with platon, PLASMe, plASgraph2 (alignment, machine learning, hybrid)
- Compare with different contig length 

# Future Work

- First, because plasmids have a large diversity, novel plasmids may contain proteins that cannot be aligned with the current database, leading to inaccurate predictions
- Second, the current tokens contain only proteins of plasmids. Studies have shown that proteins critical for bacterial survival are more likely to be found in chromosomes
- Third, the interpretation of the Transformer identified potentially unannotated PCs that may also play an important role in the life of plasmids

- Thay vì chỉ tập trung vào đặc điểm plasmid có (gene, protein tren do), tap trung them vao nhung gen co trong bacterial ma khong co trong plasmid (như là hình của biểu đồ ven)

- Cho loài mới khi chưa có dữ liệu để training, chưa có dữ liệu để align
- Cảm giác giống như bài toán Go khi có nhiều nước đi mới mà máy tính thực hiện mà con người chưa tỉm ra

- Plasmid have a large diversity, novel plasmids may contain proteins that cannot be aligned with the current database, leading to inaccurate predictions. ==Something like Auto Tokenize==
	- If a contig only contain new proteins that cannot be aligned to the database, it poses a difficult case for most tools (PLASMe and alignment-based tools)
		- Deeplasmid also relies on alignment based features such as those from HM-MER, without alignmnent length and the number of contained genes, learning to inaccurate predictions
		- Tools that rely on motifs or k-mer frequeccy, such as PPR-Meta can only predict accurately if the sequence contain specific motifs or k-mer frequency distribution that have been seen before 
	- Plasmids contain "unseen" proteins that can still be aligned with known ones. PLASMe can still accurately classify these contigs as long as they possess know essential proteins. Howerver, alignme based tools may classigy these contigs as chromosome due to the poor alignment. For example, Deeplasmid may not construc Pfam vector correct for these novel protein, jeopardizing its overral performance. ==To improve the model'sensitivity, besides updating and expanding the database in time, we will dig deeper into the relationship between plasmid proteins to buld a bridge between known and unknown tokens==
- The current tokens contains only proteins of plasmid. Studies have shoen that priterin critical for bacterial survival are more likely to be found in chromosme. Therefore adding protein specific to chromosme may help further improve the learning model accuracy. We will add the essential chromosome proterin to the current prootein databse to improve precision further
- The interpretation of Transformer identified potentially unannotated PCs that may also play an important role tin the life of plasmid. Predicting the dunction of these unaootated pplasmid protein may help study the evelotionary as well as ecological significance of plasmid
- 8Mô phỏng lại bộ gene hoàn chỉnh của vi khuẩn (Đoạn CHR or PLM đúng ra thì phải có 2 mạch, tìm vế tương ứng để sửa những điểm sai)
- Tìm ra các gene đặc thù cho vi khuẩn bằng cách tokenize từ Transformer

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

# References

[https://research.google/blog/exphormer-scaling-transformers-for-graph-structured-data/](https://research.google/blog/exphormer-scaling-transformers-for-graph-structured-data/)

- [A Generalization of Transformer Networks to Graphs](https://arxiv.org/pdf/2012.09699)
- [Self-Supervised Graph Transformer on Large-Scale Molecular Data](https://proceedings.neurips.cc/paper_files/paper/2020/file/94aef38441efa3380a3bed3faf1f9d5d-Paper.pdf)
- [TORMES: an automated pipeline for whole bacterial genome analysis](https://academic.oup.com/bioinformatics/article/35/21/4207/5430930)

- [MetaGraph: Plasmid/Chromosome Classification Enhancement Using Graph Neural Networks](https://ieeexplore.ieee.org/document/9906285)
- [plASgraph2: using graph neural networks to detect plasmid contigs from an assembly graph](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1267695/full)
- [3CAC: improving the classification of phages and plasmids in metagenomic assemblies using assembly graphs](https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii56/6702013)
- [Plassembler: an automated bacterial plasmid assembly tool](https://academic.oup.com/bioinformatics/article/39/7/btad409/7208863)
- [Why There Are No Essential Genes on Plasmids](https://academic.oup.com/mbe/article/32/12/3079/2579220?login=false)

## Hybrid

- [PLASMe: a tool to identify PLASMid contigs from short-read assemblies using transformer](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10450166/pdf/gkad578.pdf)
- [https://github.com/rrwick/Trycycler/wiki/Guide-to-bacterial-genome-assembly#2-short-read-qc](https://github.com/rrwick/Trycycler/wiki/Guide-to-bacterial-genome-assembly#2-short-read-qc)
- [Transformer as a Graph Neural Network — DGL 2.2 documentation](https://docs.dgl.ai/en/latest/tutorials/models/4_old_wines/7_transformer.html)
- [Transformers are Graph Neural Networks | NTU Graph Deep Learning Lab](https://graphdeeplearning.github.io/post/transformers-are-gnns)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html)

# Approach

The process of identifying plasmid sequences within contigs generated from sequencing projects involves a ==combination of bioinformatics tools and databases==. This approach facilitates the differentiation of chromosomal and plasmid DNA, ==allowing for the accurate assembly and annotation of plasmid sequences.==

Step-by-Step Guide

1. **Quality Assessment and Assembly**: Initially, assess the quality of your raw sequencing data using tools such as FastQC. Utilize assembly software (e.g., SPAdes, Velvet) to generate contigs from your sequencing reads. This process will compile both chromosomal and plasmid-derived sequences.
2. **Contig Classification**: Employ contig classification tools (e.g., PlasmidFinder, PlasFlow) to distinguish between chromosomal and plasmid contigs. These tools utilize databases of known plasmid sequences and machine learning algorithms to predict the origin of contigs.
3. **Database Comparison**: Compare your identified plasmid contigs against plasmid databases (e.g., NCBI's Plasmid Database, PATRIC) using BLAST or similar sequence alignment tools. This step helps to identify known plasmid sequences and assign potential functions to the contigs.
4. **Plasmid Assembly (if necessary)**: For fragmented plasmid sequences scattered across multiple contigs, consider using specialized assembly tools designed for plasmid reconstruction (e.g., plasmidSPAdes) to generate complete plasmid sequences.
5. **Annotation**: Annotate the assembled plasmid sequences using tools such as Prokka or RAST to identify genes, resistance markers, and other functional elements within the plasmid DNA.
6. **Verification and Validation**: Where possible, verify the assembled plasmid sequences through comparison with known plasmids or experimental validation methods, such as PCR, to confirm the presence of specific genes or sequences.

Considerations and Best Practices

- **Database Utilization**: Regularly update your database references to include the latest known plasmid sequences for improved accuracy in classification and annotation.
- **Cross-Validation**: Use multiple tools and databases for contig classification and annotation to cross-validate your results and increase confidence in the identified plasmid sequences.
- **Experimental Confirmation**: Whenever feasible, complement bioinformatic predictions with experimental validation to confirm the existence and structure of plasmids within your samples.

### Tools

Graph-based tools
    
Attempted to reconstruct plasmid underlying assembly graph
[https://github.com/cchauve/plASgraph2](https://github.com/cchauve/plASgraph2)
Rely on read coverage and cyclic topology for plasmid assembly, which is best used to find relatively comple plasmid rather than short contig
    
Alignment-based tools

- based on the similarities between queries and reference
- For database we can use vector database to query faster. But we need a way to tokenize the query sequence
    
Learning-based tools

- provide a promising alternative for detecting more diverged plasmids via learning abstract patterns beyond sequence similarity.
- Use k-mer freq as the features and applied sequential minimal optimization, fully connected neural network
- PPR-Meta encodes the sequences and the contained codons into one-hot matrices and then trains a CNN model for prediction
- Decreased precision on short contigs, whose length limits the capacity of feature learning
- Can have ambiguous predictions for contigs from shared regions between plasmids and chromosomes

Hybrid
    
- In order to achieve an optimal trad-off between sensitivity and precision, combine homology search and machine learning to identify as many as possible
- PlasmidVerify train a Naive Bayes classifier using protein domain alighment-based feature
- PlasForest using homology search results as features
- Also exhibit decreased accuracy on short contigs
- PLASMe: treat plasmid as a language defined on a vocabulary of protein. Transformer, to learn the protein importantce and their associations for plasmid

# Q&A

- Should we identify only plasmid or both plasmid, chromosome, ambiguous
	- Benefit of ambiguous can see in plASgraph2

# Differences between Plasmids and Chromosomes

- **Plasmids**:
    - Typically ==**small**, circular== pieces of DNA.
    - Often carry genes that provide **adaptive advantages**, such as antibiotic resistance or toxin production.
    - Replicate independently of the host’s chromosomal DNA.
    - Found in bacteria and sometimes in eukaryotes.
    - Contain fewer genes compared to chromosomes, often coding for **non-essential** functions.
- **Chromosomes**:
    - **Larger** in size, usually linear in eukaryotes (but circular in prokaryotes).
    - Contain **essential genes** required for cell growth, division, and survival.
    - Replicate as part of the organism's regular cell cycle.
    - Carry regulatory regions like **promoters, enhancers**, and **silencers** for controlling gene expression.

- Sequeces Composition
	- GC content: Plasmids and chromosomes from the same species may have different GC content. (but when split into contig this information maybe change, how about relatives in [plASgraph2])
- k-mers
	- 3-5 k-mers can help capture specific motifs or sequence patterns that are more frequent in plasmid (antibiotic resistance genes) or chromosome (essential genes)