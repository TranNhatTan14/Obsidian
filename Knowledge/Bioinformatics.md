---
links:
  - "[[Knowledge]]"
---
### Alleles

Different versions of the same variant are called alleles. For example, a SNP may have two alternative bases, or alleles, C and T4.

### Variant

Genetic variation is the difference in DNA sequences between individuals within a population

[Type of genetic variation](https://www.ebi.ac.uk/training/online/courses/human-genetic-variation-introduction/what-is-genetic-variation/types-of-genetic-variation/)

### VCF

**VCF is the standard file format** for storing variation data. It is used by large scale variant mapping projects.

VCF is a preferred format because it is **unambiguous, scalable and flexible**, allowing extra information to be added to the info field. Many millions of variants can be stored in a single VCF file.

VCF files are tab delimited text files.

### Linkage Disequilibrium

In the genome, alleles at variants close together on the same chromosome tend to occur together more often than is expected by chance. These blocks of alleles are called haplotypes. **Linkage disequilibrium** (LD) is a measure of how often two alleles or specific sequences are inherited together, with alleles that are always co-inherited said to be in linkage disequilibrium.

- It is now standard practice to include top principal components as covariates in association analysis, to correct population stratification.
- Also, when working with unbalanced binary phenotypes, be aware that Firth regression can be similar to adding a [pseudocount](https://en.wikipedia.org/wiki/Additive_smoothing) of 0.5 to the number of case and control minor allele observations, so weird things happen when the _expected_ number of case minor allele observations is less than 0.5. You probably don't want to throw out every variant with MAC < 300 when your case:control ratio is 1:600 (you may still have excellent power to detect _positive_ association between the minor allele and case status, after all), but you shouldn't take reported odds-ratios or p-values literally for those variants.

# [Contig](https://www.genome.gov/genetics-glossary/Contig)

A contig (as related to genomic studies; derived from the word “contiguous”) is a set of DNA segments or sequences that overlap in a way that provides a contiguous representation of a genomic region. For example, a clone contig provides a physical map of a set of cloned segments of DNA across a genomic region, while a sequence contig provides the actual DNA sequence of a genomic region.

![contig](https://www.genome.gov/sites/default/files/media/images/tg/Contig.jpg)

**“Reads” are small segments of nucleic acid sequence produced by a sequencing instrument (there are many kinds).** **“Contigs” represent contiguous sequence formed by assembling the reads**

A genome is typically studied by breaking down its DNA into pieces, analyzing those pieces in the laboratory, and then computationally putting those pieces back together in a conceptual way. Years ago, before genome sequencing became routine, the pieces of DNA would first be cloned and then individual clones would be analyzed to determine which clones overlapped which other clones. A set of overlapping clones that together contain a ‘contiguous’ region of a genome is called a contig – or in this case a clone contig. Genome sequencing uses the concept of a contig, but in a different way. For genome sequencing, the pieces are not actually physical segments of DNA but rather are stretches of generated DNA sequence (often called a sequence read). By establishing the overlaps among a set of sequence reads, one can assemble a sequence contig, from which the actual sequence of the genomic region can be deduced.

https://www.quora.com/What-are-reads-and-contigs-file-formats-bioinformatics#:~:text=%E2%80%9CReads%E2%80%9D%20are%20small%20segments%20of,formed%20by%20assembling%20the%20reads.

# Terminology

### Consensus

### Composition

- The read binning tools such as OBLR employ read overlap graphs that hold neighborhood information of overlapping reads.
- The use of the read overlap graph has greatly increased the accuracy of binning yet requires effcient means to handle large overlap graphs with millions of reads.