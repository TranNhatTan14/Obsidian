---
links:
  - "[[Research]]"
  - "[[Genome-Wide Association Study|GWAS]]"
  - "[[Biology]]"
tags:
  - Project
description: Think of NSAID as transfer learning of Machine Learning
---
# Stats

https://www.cog-genomics.org/plink/2.0/basic_stats
https://www.cog-genomics.org/plink/2.0/ld

# Quality Control

### Imputation quality

https://www.cog-genomics.org/plink/2.0/filter

- **--mach-r2-filter** excludes variants where the MaCH Rsq imputation quality metric (frequently labeled as 'INFO') is outside [0.1, 2.0]; change the bounds by providing parameters. Monomorphic variants, where Rsq == nan, are not excluded by this filter: the problem with them isn't imputation quality.

- Similarly, **--minimac3-r2-filter** excludes variants where [Minimac3's imputation quality metric](https://genome.sph.umich.edu/wiki/Minimac3_Info_File#Rsq) is outside the given range. **Note that this metric assumes that phased dosages have been imported with e.g. [--vcf's dosage=HDS option](https://www.cog-genomics.org/plink/2.0/input#vcf)**; the computation still proceeds when unphased dosages are present, but the results will be underestimates. If you don't need phased dosages for any other reason, [--{extract,exclude}-if-info](https://www.cog-genomics.org/plink/2.0/filter#extract_if_info) is usually a more efficient way to do this properly.

- minimac3-r2-filter 1" can be used to keep only perfectly-imputed-and-phased variants.
- Lựa chọn tham số dựa trên dữ liệu

# Outline

- Describe the general workflow of GWAS in 1 slide. (1 min)
- Summarize QC steps in 1 slide (1 min)
- Summarize PCA in 1 slide (1 min)
    - explain the aims and major steps
- Show your 1000 genome PCA results (~2 slides): (~4 min)
    - explain what tool and data you use.
    - explain what kind of analysis you performed.
    - show your results and explain the scatter plot.
- Association analysis (1-2 slides) : (2 min)
    - explain the variables in the regression and the header of your GWAS results.
    - explain your manhattan plot and qq plot.
- Post GWAS analysis (~6 min)
    - explain what kind of post-GWAS analysis you perform.
    - explain the aim for each post-GWAS analysis.
    - explain the results of LDSC.
    - explain the annotated results

# Resources

- [Genome-wide association studies](https://www.nature.com/articles/s43586-021-00056-9)
	- Genome-wide association studies (GWAS) aim to identify associations of genotypes with phenotypes by testing for differences in the allele frequency of genetic variants between individuals who are ancestrally similar but differ phenotypicall
	- GWAS can consider copy-number variants or sequence variations in the human genome, although the most commonly studied genetic variants in GWAS are single-nucleotide polymorphisms (SNPs).

- [Benefits and limitations of genome-wide association studies](https://www.nature.com/articles/s41576-019-0127-1)

## HLA

[Axiom Analysis Suite v5.4 User Guide](https://assets.thermofisher.com/TFS-Assets/GSD/brochures/axiom-analysis-suite-user-guide.pdf)
[Axiom HLA Analysis v1.2 User Guide](https://assets.thermofisher.com/TFS-Assets/LSG/manuals/axiom_hla_analysis_user_guide.pdf)