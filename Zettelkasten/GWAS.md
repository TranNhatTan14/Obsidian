# Definition

- A genome-wide association study (==abbreviated== GWAS) is a research approach used to ==identify genomic variants that are statistically associated with a risk for a disease or a particular trait==.
- The method involves surveying the genomes of many people, l==ooking for genomic variants that occur more frequently in those with a specific disease or trait== compared to those without the disease or trait. Once such genomic variants are identified, they are typically used to ==search for nearby variants that contribute directly to the disease or trait.==

- Genome-Wide Association Study, GWAS. The goal of genome-wide association studies, or GWAS as we call them, is to ==screen the entire genome of large numbers of individuals to look for associations between millions of genetic variants within those individuals and their disease outcomes== or sometimes for associations between the variants and non-disease trait such as height. 
- The first GWAS was published in 2005 and after that, the study approach just took off exponentially. Over time, GWAS have grown significantly both in terms of ==sample size== going from initial sample sizes of several thousand individuals to current sample sizes of tens and hundreds of thousands of individuals and in terms of the ==number of disease studied== as well as the associated variants that have been discovered. 
- ==Results from GWAS have been curated in the NHGRI-EBI GWAS catalog==. The methods and results of GWAS have informed other applications in applied epidemiologic research such as gene environment studies, ==Mendelian randomization studies, and polygenic risk score== approaches. As I noted, ==GWAS focus on statistical associations==. They inform us of correlation not causation. A major challenge posed by GWAS is the exploration of the functional consequences of identified variants which will provide insights into the biology of disease.

# Workflow

The primary ==output of a GWAS analysis is a list of P values, effect sizes and their directions generated from the association tests of all tested genetic variants with a phenotype of interest==. These data are routinely visualized using Manhattan plots and quantile–quantile plots (Fig. 2), generated using software tools such as R or web platforms such as FUMA88 or LocusZoom89.

==Further analysis is then needed to interpret this list of P values==, determining the ==most likely causal variants==, their functional interpretation and ==possible convergence in meaningful biological pathways== (Fig. 3). We discuss these post-GWAS analyses below.

Illustration of functional follow-up of GWAS

1. Genome-wide association studies (GWAS) are conducted to identify associated variants, often visualized as a Manhattan plot to show their genomic positions and strength of association. 
2. To ==prioritize likely causal variants, statistical fine-mapping is applied to identify a set of variants that are likely to include the causal variant== (blue box) as well as the most likely causal variant (rs12345; blue dot). Massively parallel reporter assays can be used to measure whether alleles differ in their ability to drive gene expression or other molecular activity for each variant (not shown). 
3. ==Functional annotations of the genome== can be integrated with GWAS data to ==identify epigenetic mechanisms that may be perturbed by the causal variant==, including enhancers, promoters or other functional elements. Additional approaches include mapping molecular quantitative trait loci (molQTL) or in vitro assays (not shown). 
4. ==Target gene for a GWAS locus can be prioritized by mapping expression quantitative trait loci== (eQTLs) (left) and ==their co-localization== (right) to ==identify loci where the causal variant from GWAS== is also a causal variant affecting gene expression. For GWAS variants in enhancers, high-throughput chromosome conformation capture (Hi-C) data and maps of enhancer target genes can be used together with simple prioritization by distance to identify genes affected by the causal variant (below). 
5. To identify pathways whose perturbation may mediate the trait in question (red box), one can analyse the enrichment of multiple GWAS-implicated genes in predefined pathways. Additional approaches include trans-eQTL mapping and CRISPR perturbation of GWAS loci/genes followed by cellular phenotyping (not shown). For these analyses, the context of a relevant tissue, cell type and cell state needs to be carefully considered and analysed. ATAC-seq, assay for transposase-accessible chromatin using sequencing; H3K27Ac, histone H3 acetylated at K27; SNP, single-nucleotide polymorphism.

**Data collection**

Data can be collected from study cohorts or available genetic and phenotypic information can be used from biobanks or repositories. Confounders need to be carefully considered and recruitment strategies must not introduce biases such as collider bias.

**Genotyping**

Genotypic data can be collected using microarrays to capture common variants, or next-generation sequencing methods for whole-genome sequencing (WGS) or whole-exome sequencing (WES). 

**Quality control**

Quality control includes steps at the wet-laboratory stage, such as genotype calling and DNA switches, and dry-laboratory stages on called genotypes, such as deletion of bad single-nucleotide polymorphisms (SNPs) and individuals, detection of population strata in the sample and calculation of principle components. Figure depicts clustering of individuals according to genetic substrata.

**Imputation**

Genotypic data can be phased, and untyped genotypes imputed using information from matched reference populations from repositories such as 1000 Genomes Project or TopMed. In this example, genotypes of SNP1 and SNP3 are imputed based on the directly assayed genotypes of other SNPs.

## Pre-GWAS
### ==Quality Control==

Data processing. Input files for a GWAS include anonymized individual ID numbers, coded family rela- tions between individuals, sex, phenotype information, covariates, genotype calls for all called variants and information on the genotyping batch. Following input of the data, generating reliable results from GWAS requires careful quality control. Some example steps include removing rare or monomorphic variants, removing variants that are not in Hardy–Weinberg equilibrium, filtering SNPs that are missing from a fraction of individ- uals in the cohort, identifying and removing genotyping errors, and ensuring that phenotypes are well matched with genetic data, often by comparing self-reported sex versus sex based on the X and Y chromosomes. Software tools such as PLINK have been specifically designed to analyse genetic data and can be used to conduct many of these quality control steps 20 (further software for quality control analysis and other stages of GWAS are summarized in Table 1). Once sample and variant quality control have been performed on GWAS array data, variants usually undergo phasing and are imputed using

### Phasing

### ==Imputation==

### PCA

## GWAS

**Association testing**

==Genetic association tests are run for each genetic variant==, using an appropriate model (for example, additive, non-additive, linear or logistic regression). Confounders are corrected for, including population strata, and multiple testing needs to be controlled. Output is inspected for unusual patterns and summary statistics are generated.

The output of a GWAS analysis is a list of P values, effect sizes and their directions generated from the association tests of all tested genetic variants with a phenotype of interest.

Statistics check
Harmonization

Assign rsID

Extract lead variants
Extract novel variants

https://cloufield.github.io/gwaslab/reserved_header/

### Visualization

These data are routinely visualized using Manhattan plots and quantile–quantile plots.

### ==Variant annotation==

- Extract lead variants
- Extract novel variants
- Convert heritability
- Per-SNP R2 and F

List of tools: ANNOVAR, VEP, GWASLab

### Optional

- Linear Mixed Model
- Whole Genome Regression

## Post-GWAS

Further analysis is then needed to interpret this list of P values, ==determining the most likely causal variants, their functional interpretation== and possible ==convergence in meaningful biological pathways==.

Illustration of functional follow-up of GWAS.

**What are the associated loci?**

GWAS are conducted to identify associated variants, often visualized as a Manhattan plot to show their genomic positions and strength of association.

**What are the likely causal variants?**

==To prioritize likely causal variants, statistical fine-mapping is applied to identify a set of variants that are likely to include the causal variant== (blue box) as well as the most likely causal variant (rs12345; blue dot). Massively parallel reporter assays can be used to measure whether alleles differ in their ability to drive gene expression or other molecular activity for each variant (not shown). 

**What are the epigenomic effects of variants?**

==Functional annotations of the genome== can be integrated with GWAS data to identify epigenetic mechanisms that may be perturbed by the causal variant, including ==enhancers, promoters or other functional elements==. Additional approaches include mapping molecular quantitative trait loci (molQTL) or in vitro assays (not shown).

**What are the target genes in the locus?**

==Target gene for a GWAS locus can be prioritized by mapping expression quantitative trait loci== (eQTLs) (left) and their ==co-localization== (right) to identify loci where the causal variant from GWAS is also a causal variant affecting gene expression. For GWAS variants in enhancers, high-throughput chromosome conformation capture (Hi-C) data and maps of enhancer target genes can be used together with simple prioritization by distance to identify genes affected by the causal variant (below).

What are the affected pathways?

To ==identify pathways whose perturbation may mediate the trait in question== (red box), one can analyse the enrichment of multiple GWAS-implicated genes in predefined pathways. Additional approaches include trans-eQTL mapping and CRISPR perturbation of GWAS loci/genes followed by cellular phenotyping (not shown). For these analyses, the context of a relevant tissue, cell type and cell state needs to be carefully considered and analysed. ATAC-seq, assay for transposase-accessible chromatin using sequencing; H3K27Ac, histone H3 acetylated at K27; SNP, single-nucleotide polymorphism.

---

### Statistical fine-mapping

Fine-mapping aims to identify the causal variants with a locus for a disease, given the evidence of the significant association of the locus (or genomic region) in GWAS of a disease.

Credible sets

A **credible set** refers to the minimum set of variants that contains all causal SNPs with probability α. (Under the single-causal-variant-per-locus assumption, the credible set is calculated by ranking variants based on their posterior probabilities, and then summing these until the cumulative sum is >α). We usually report 95% credible sets (α=95%) for fine-mapping analysis.

---

Many non-causal variants are significantly associated with a trait of interest owing to linkage disequilibrium; whether these reach the significance threshold depends on their level of correlation with and the strength of association of the causal variant. The output of GWAS is therefore clustered in risk loci — sets of correlated variants that all show a statistically significant association with the trait of interest — and ==linkage disequilibrium typically prevents pinpointing causal variants without further analysis.==

Fine-mapping is an in silico process designed to prioritize the set of variants that are most likely to be causal to the target phenotype within each of the genetic loci identified by GWAS, based on observed patterns of linkage disequilibrium and association statistics. The set of variants that most parsimoniously explain regional association signals are defined as credible variants. The lead variant with the most significant association would be expected to be the most credible causal variant, although there are several situations where the most significant association may be non-causal. For example, where multiple independent risk variants are present in a locus, the combination of multiple signals can shift the most significant association from causal variants to a neighbouring non-causal variant. This can also occur owing to heterogeneity in variant genotype imputation quality, which induces fluctuations in the association signal statistics among neighbouring variants in linkage disequilibrium.

==The simplest fine-mapping analysis is a conditional association analysis of the regional variants==, which adjusts the regional association signals according to the set of variants in the locus by including the lead variant as a covariate in genotype–phenotype regression models.

When multiple association signals exist, forward stepwise selection is commonly used until no associations remain. This method, known as ==stepwise conditional analysis==, is limited to searching all of the combinatory patterns of potential credible variants. This is because the variant search pattern in each iterative step is strongly dependent on the previously selected variant sets and the lead initial step often includes the lead variant. When full genotype data are not available, conditional association analyses can be conducted on summary statistics using GCTA-COJO software.

Several sophisticated fine-mapping approaches are based on Bayesian models, including CAVIAR93, FINEMAP94, PAINTOR95 and SuSIE96. These approaches optimize the selection of variables for a regression model by using a prior probability distribution, or prior, to estimate a posterior probability distribution, or posterior. An advantage of using Bayesian models over conditional association analysis is that priors can consider additional information such as imputation accuracy in addition to association signals; ==however, sets of credible variants output using Bayesian modelling are generally not consistent across different methods==, especially when multiple independent association signals exist within a locus. In general, the statistical power to correctly detect credible variant sets declines as the number of independent signals increases.

- The purpose of fine-mapping is to ==identify the specific genetic variants within a genomic region (locus) that are directly responsible for a disease or trait==. 
- While GWAS can highlight regions of the genome associated with a disease, these regions often contain many variants. ==Fine-mapping narrows down this list to pinpoint the causal variant(s)==, which can then be studied further to understand the biological mechanisms underlying the disease, potentially leading to new diagnostic tools, therapies, or preventive strategies.

### Meta-analysis

Results from multiple smaller cohorts are combined using standardized statistical pipelines.

### ==Enrichment or gene-set analysis==

- Gene / Gene-set analysis by MAGMA

**MAGMA**

==Gene-based and gene-set analysis== using competitive testing with a regression framework; allows ==testing of custom gene sets== and includes options for ==conditional and interaction testing between gene sets==

https://ibg.colorado.edu/cdrom2021/Day10-posthuma/magma_session/manual_v1.09a.pdf

---

### Heritability

SNP heritability: the proportion of phenotypic variance explained by tested SNPs in a GWAS

Common methods to estimate SNP heritability includes:

- GCTA-GREML (based on Genome-based Restricted Maximum Likelihood)
- LDSC (based on LD score regression)

---

**LD score regression (univariate, cross-trait and partitioned) by LDSC**

https://cloufield.github.io/GWASTutorial/08_LDSC

LDSC is one of the most commonly used command line tool to estimate inflation, hertability, genetic correlation and cell/tissue type specificity from GWAS summary statistics.

Linkage disequilibrium (LD) : non-random association of alleles at different loci in a given population



Partitioned SNP-based heritability analyses showing enrichment in sets of functionally related SNPs

==Partitioned SNP-based heritability analysis is like breaking down a complex recipe into its ingredients to see which parts contribute most to the final flavor.==

In this case, the "recipe" is the heritability of a trait, which is the proportion of variation in that trait that can be attributed to genetic differences. The "ingredients" are SNPs (single nucleotide polymorphisms), which are individual variations in the DNA sequence.

The analysis works by dividing SNPs into different "sets" based on their functional roles (like grouping ingredients by type, such as spices, vegetables, etc.). For example, some SNPs might be in regions of the genome that regulate gene expression, while others might be in coding regions that directly affect proteins.

By analyzing these sets separately, researchers can determine which groups of SNPs (which "ingredients") contribute more to the heritability of a trait. If a particular set of functionally related SNPs shows "enrichment," it means that set has a larger-than-expected impact on heritability, similar to how a certain spice might dominate the flavor of a dish.

This helps pinpoint which biological processes are most important for the trait in question.

- Load LDSC log with GWASLab

https://cloufield.github.io/gwaslab/LDSCinGWASLab

---

**Heritability Concepts, SNP-Heritability estimation by GCTA-GREML**



---

### QTL analysis

### Genetic correlations

### Causality

### ==PRS analysis==

### TWAS

What are transcriptome-wide association studies?

Transcriptome-wide association study (TWAS) is **an instrumental post-analysis to detect significant gene-trait associations focusing on modeling transcription-level regulations**, which has made numerous progresses in recent years

What is the difference between GWAS and TWAS?

However, GWAS faces challenges like multiple testing corrections and difficulties in pinpointing causal variants. Conversely, **TWAS offers higher gene resolution and the potential for deeper insights into genetic mechanisms**.

TWAS is a method to identify significant expression-trait associations using expression imputation from genetic data or summary statistics.

- Individual-level TWAS uses individual-level genotype and phenotype for expression prediction and association test
- Now mind don't remove any sample, what is the best value for mind

- [Transcriptome-wide association studies: recent advances in methods, applications and available databases](https://doi.org/10.1038/s42003-023-05279-y)
- [Genome-wide versus transcriptome-wide association studies: Prospects and limitations](https://doi.org/10.1016/j.egg.2024.100221)

### Optional

- Colocalization
- Fine-mapping by SUSIE

---

# Resources

- [Genome-wide association studies](https://www.nature.com/articles/s43586-021-00056-9)

- Genome-wide association studies (GWAS) aim to identify associations of genotypes with phenotypes by testing for differences in the allele frequency of genetic variants between individuals who are ancestrally similar but differ phenotypicall
- GWAS can consider copy-number variants or sequence variations in the human genome, although the most commonly studied genetic variants in GWAS are single-nucleotide polymorphisms (SNPs).

- [Benefits and limitations of genome-wide association studies](https://www.nature.com/articles/s41576-019-0127-1)

---

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