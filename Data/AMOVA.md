---
tags:
  - Work
links:
  - "[[Current Work]]"
description: Sử dụng phương pháp AMOVA để phân tích sự đồng nhất về kiểu gen
---
Use AMOVA (Analysis of Molecular Variance) method to analyze genetic homogeneity with human STR or mtDNA data. Display the genetic homogeneity results in a table format.

Use the AMOVA (Analysis of Molecular Variance) method to assess the genetic variation within and between populations to determine their genetic homogeneity using STR or mtDNA data

- AMOVA is a method used to understand how genetics differences vary with and between groups.
- Imagine dividing peole into groups and seeing if they're genetically similar.
- AMOVA helps us check if the variation in genes is mostly within the same group or spead across different groups.
- AMOVA partitions molecular variance into components attributable to hierarchical population structures, using a distance matrix calculated from genetic data.
- It is especially usefull when working with genetics data across geographically or genetically defined population

Requires genetic data that can be used to calculate genetic distances between individuals or groups

1. Molecular Marker Data

- STR: Highly variable sequences that provide detailed information on genetics differences
- SNP
- mtDNA: Often used in studies of material lineage and population structure

# Definition

Analysis of Molecular Variance (AMOVA) is a statistical method used primarily in population genetics to assess the genetic variation among populations and within populations. It serves as a nonparametric alternative to traditional analysis of variance (ANOVA), allowing researchers to evaluate hypotheses regarding genetic diversity without assuming normality in the data distribution.

# Purpose and Application

AMOVA is designed to test whether the genetic diversity observed within two or more populations significantly differs from what you would be expected if the populations were pooled together.

# Input

### Raw genetic data from ==different populations==

- STR: Allele frequencies or genotype data from multiple loci
- mtDNA data: Sequence data or haplotype information

### Population structure information

- Population grouping/hierarchical levels
- Geographic locations
- Sample size per population

Population Structure Information Types:

- Geographic Hierarchy:
	- Continental (Europe, Asia, Africa)
	- Regional (Northern Europe, Southern Europe)
	- Local (Individual countries/regions)
- Linguistic Groups
- ==Ethnic Groups==
- Migration History Groups
- Social/Cultural Groups
- Temporal Groups (Ancient vs Modern populations)

### Distance matrix

- For STR: Allelic distance or RST distance
- For mtDNA: Sequence differences or genetic distance (like Nei's or FST)

# Output

Source of          Degrees of    Sum of      Variance         Percentage of
Variation          Freedom       Squares     Components       Variation
-------------------------------------------------------------------------
Among Groups         2           245.85      0.85 Va            15.3%
Among Populations    6           178.90      0.62 Vb            11.2%
Within Populations   291         1186.75     4.08 Vc            73.5%
-------------------------------------------------------------------------
Total               299         1611.50      5.55              100.0%

Fixation Indices:
FCT (Among groups): 0.153
FSC (Among populations within groups): 0.132
FST (Among all populations): 0.265



# Methodology

The core of AMOVA involves partitioning the total genetic variance into components atributable to different hierarchical levels, such as among populations, among individuals within populations, and within individuals.

The fundamental equations used in AMOVA include:

- Total Sum of Squares (SS_total) represents the total variance.
- Within Sum of Squares (SS_within): Variance within populations
- Among Sum of Squares (SS_among): Variance among population

1. Data Collection

Distance Matrix Calculation

Construct a distance matrix that quantifies genetic differences among samples.
For STR data, this could be based on the number of allelic differences

Group Stratification

Define the groups (populations) for comparision. This involves assigning each sample to its respective population in a separate design file that indicates group membership

Running AMOVA

Interpreting Results

- The output will include
	- variance components (among populations and within population)
	- F-statistics (often represented as u-statistics)
	- ANOVA uses the F-test to compare the ratio of variance between groups to variance within groups. The larger the F-value, the more likely it is that there are significant differences between group means. There are different types of ANOVA:
	- p-value indicating the significance of population differentiation
	- ANOVA outputs a p-value to help decide if the differences are meaningful. If the p-value is below a certain threshold (like 0.05), it suggests that at least one group mean is different.

![[Pasted image 20241115141651.png]]

https://pmc.ncbi.nlm.nih.gov/articles/PMC1205020/pdf/ge1312479.pdf