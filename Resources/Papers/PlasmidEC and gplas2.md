---
tags:
  - Paper
  - Research
aliases:
  - "PlasmidEC and gplas2: An optimized short-read approach to predict and reconstruct antibiotic resistance plasmids in E. coli"
links:
  - "[[Plasmid]]"
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10926690/pdf/mgen-10-1193.pdf
---
A dataset of 240 complete E. Coli genomes from eight different phylogroups and 117 sequence types (STs), carrying plasmids, was selected as previously described in ...

- All genome sequences were completed by the combination of short-and long-read sequencing data
	- Short-read sequences and complete genomes were download from NCBI using SRA tool and ncbi-genome-download
- First we can only focus on: E. coli, K. pneumoniea, S. aureus
- We can hybrid with alignment for our task, the metagenomic binning can use it

- The resulting contig were labelled by alignment to their respective complete geonmes using ==QUAST==
	- Only contig larger than 1000 bp with an alignment of at least 90% the contig length were considered
	- Of those, contigs aligning to multiple positions in the genome (ambiguously aligned contigs) were included as long as they exclusively aligned to either the chromosome or to plasmid

# Discussion

- Accurately recontructing E. Coli plasmids from IIlumina reads has proven to be a challenge, especially in the context of ARG-plasmid.
- Develop a high-throughput method to recontruct E. Coli plasmids de novo from short-read sequencing data.
- Method relies on an accurate identification of plasmid-derived nodes in the asssembly graph, followed by the binning of these notes using sequencing and node connectivity information.
- To improve the identification of plasmid-derived contigs, we build plasmidEC, an ensemble classifier that combines predictions from three individual binary classifier and implement a majority voting system.











Gplas, which enables the bining and a detailed analysis workflow of binary classified plasmid into discrete plasmid units by relying on the structure of the assembly graph, k-mer information and ==partitioning of a pruned plasmidone network.==

- Limitation
	- The generation of chimeras resulting from plasmids with similar k-mer profiles, k-mer coverage and sharing repeat unit, such as a transposase or an IS element
		- These cases cannot be unambiguously solved

Here, we integrated and extended upon features to predict plasmid sequences and exploit the information present in short-read graphs to automate the reconstruction of plasmids.