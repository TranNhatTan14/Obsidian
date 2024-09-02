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