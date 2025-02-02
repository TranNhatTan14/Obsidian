---
tags:
  - Paper
links:
  - "[[Submit Graph Transformer paper in ICLR]]"
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7320608/pdf/btaa233.pdf
aliases:
  - gplas a comprehensive tool for plasmid analysis usingshort-read graphs
---
https://bio.tools/Gplas

# Abstract

- Plasmids can horizontally transmit genetic traits, enabling rapid bacterial adaptation to new environments and hosts. 
- Short-read whole-genome sequencing data are often applied to large-scale bacterial comparative genomics projects but the reconstruction of plasmids from these data is facing severe limitations, such as the inability to distinguish plasmid from each other in a bacterial genome.
- We developed gplas, a new approach to reliably separate plasmid contigs into discrete components using sequence composition, coverage, assembly graph information and network partitioning based on pruned network of plasmid contigs.
- Gplas facilitates the analysis of large numbers of bacterial isolates and allows a detailed analysis of plasmid epidemiology based solely on short-read sequence data.

# Introduction

- A single bacterial cell can harbor several distinct plasmid, however, current plasmid prediction tools from short-read WGS often have a binary outcome (plasmid or chromosome)
- To bin predicted plasmids into discrete entities, we built a new method based on the following concept
	- Contigs of the same plasmid have a uniform sequence coverage
	- Plasmid paths in the assembly graph can be searched for using of a greedy approach
	- Removal of repeat units from the plasmid graph disconnects the graph into independent components

Introduce the concept of unitigs co-occurrence to create a pruned plasmidone network
Using an unsupervised approach, the network is queried to find highly connected nodes corresponding to sequence belong to the same discrete plasmid unit, representing a single plasmid

# Matetials and methods

## Gplas algorithm

Gplas use mlplasmid and plasflow to classify node as plasmid or chromosome-derived and selects segments with an in- and out- degree of 1 (unitigs)
The k-mer coverage SD of the chromosome-derived unitig is computed to quantify the fluctuation in the coverage of segments belong to the same replicon unit
Plasmid-derived unitigs are considered to search for plasmid walks with a similar coverage and composition using a greedy approach
Gplas creates a plasmidome network (undirected graph) in which nodes correspond to plasmid unitigs and edges are created and weighted based on the co-existence of the nodes in the solution space of the computed walk