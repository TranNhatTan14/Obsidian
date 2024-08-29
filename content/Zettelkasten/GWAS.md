- A genome-wide association study (==abbreviated== GWAS) is a research approach used to ==identify genomic variants that are statistically associated with a risk for a disease or a particular trait==.
- The method involves surveying the genomes of many people, l==ooking for genomic variants that occur more frequently in those with a specific disease or trait== compared to those without the disease or trait. Once such genomic variants are identified, they are typically used to ==search for nearby variants that contribute directly to the disease or trait.==

- Genome-Wide Association Study, GWAS. The goal of genome-wide association studies, or GWAS as we call them, is to ==screen the entire genome of large numbers of individuals to look for associations between millions of genetic variants within those individuals and their disease outcomes== or sometimes for associations between the variants and non-disease trait such as height. 
- The first GWAS was published in 2005 and after that, the study approach just took off exponentially. Over time, GWAS have grown significantly both in terms of ==sample size== going from initial sample sizes of several thousand individuals to current sample sizes of tens and hundreds of thousands of individuals and in terms of the ==number of disease studied== as well as the associated variants that have been discovered. 
- ==Results from GWAS have been curated in the NHGRI-EBI GWAS catalog==. The methods and results of GWAS have informed other applications in applied epidemiologic research such as gene environment studies, ==Mendelian randomization studies, and polygenic risk score== approaches. As I noted, ==GWAS focus on statistical associations==. They inform us of correlation not causation. A major challenge posed by GWAS is the exploration of the functional consequences of identified variants which will provide insights into the biology of disease.

# Workflow

1. Data can be collected from study cohorts or available genetic and phenotypic information can be used from biobanks or repositories. Confounders need to be carefully considered and recruitment strategies must not introduce biases such as collider bias.
2. Genotypic data can be collected using microarrays to capture common variants, or next-generation sequencing methods for whole-genome sequencing (WGS) or whole-exome sequencing (WES). 
3. Quality control includes steps at the wet-laboratory stage, such as genotype calling and DNA switches, and dry-laboratory stages on called genotypes, such as deletion of bad single-nucleotide polymorphisms (SNPs) and individuals, detection of population strata in the sample and calculation of principle components. Figure depicts clustering of individuals according to genetic substrata.
4. Genotypic data can be phased, and untyped genotypes imputed using information from matched reference populations from repositories such as 1000 Genomes Project or TopMed. In this example, genotypes of SNP1 and SNP3 are imputed based on the directly assayed genotypes of other SNPs.
5. ==Genetic association tests are run for each genetic variant==, using an appropriate model (for example, additive, non-additive, linear or logistic regression). Confounders are corrected for, including population strata, and multiple testing needs to be controlled. Output is inspected for unusual patterns and summary statistics are generated.
6. Results from multiple smaller cohorts are combined using standardized statistical pipelines.
7. Results can be replicated using internal replication or external replication in an independent cohort. For external replication, the independent cohort must be ancestrally matched and not share individuals or family members with the discovery cohort.
8. In silico analysis of genome-wide association studies (GWAS), using information from external resources. This can include in silico fine-mapping, SNP to gene mapping, gene to function mapping, pathway analysis, genetic correlation analysis, Mendelian randomization and polygenic risk prediction. After GWAS, functional hypotheses can be tested using experimental techniques such as CRISPR or massively parallel reporter assays, or results can be validated in a human trait/disease model (not shown).

The primary ==output of a GWAS analysis is a list of P values, effect sizes and their directions generated from the association tests of all tested genetic variants with a phenotype of interest==. These data are routinely visualized using Manhattan plots and quantile–quantile plots (Fig. 2), generated using software tools such as R or web platforms such as FUMA88 or LocusZoom89.

==Further analysis is then needed to interpret this list of P values==, determining the ==most likely causal variants==, their functional interpretation and ==possible convergence in meaningful biological pathways== (Fig. 3). We discuss these post-GWAS analyses below.

Illustration of functional follow-up of GWAS

1. Genome-wide association studies (GWAS) are conducted to identify associated variants, often visualized as a Manhattan plot to show their genomic positions and strength of association. 
2. To ==prioritize likely causal variants, statistical fine-mapping is applied to identify a set of variants that are likely to include the causal variant== (blue box) as well as the most likely causal variant (rs12345; blue dot). Massively parallel reporter assays can be used to measure whether alleles differ in their ability to drive gene expression or other molecular activity for each variant (not shown). 
3. ==Functional annotations of the genome== can be integrated with GWAS data to ==identify epigenetic mechanisms that may be perturbed by the causal variant==, including enhancers, promoters or other functional elements. Additional approaches include mapping molecular quantitative trait loci (molQTL) or in vitro assays (not shown). 
4. ==Target gene for a GWAS locus can be prioritized by mapping expression quantitative trait loci== (eQTLs) (left) and ==their co-localization== (right) to ==identify loci where the causal variant from GWAS== is also a causal variant affecting gene expression. For GWAS variants in enhancers, high-throughput chromosome conformation capture (Hi-C) data and maps of enhancer target genes can be used together with simple prioritization by distance to identify genes affected by the causal variant (below). 
5. e | To identify pathways whose perturbation may mediate the trait in question (red box), one can analyse the enrichment of multiple GWAS-implicated genes in predefined pathways. Additional approaches include trans-eQTL mapping and CRISPR perturbation of GWAS loci/genes followed by cellular phenotyping (not shown). For these analyses, the context of a relevant tissue, cell type and cell state needs to be carefully considered and analysed. ATAC-seq, assay for transposase-accessible chromatin using sequencing; H3K27Ac, histone H3 acetylated at K27; SNP, single-nucleotide polymorphism.

## Pre-GWAS
### ==Quality Control==

### ==Imputation==

## GWAS

### ==Association==

## Post-GWAS

### Statistical fine-mapping

### Meta-analysis

### ==Variant annotation==

### Enrichment or gene-set analysis

### QTL analysis

### Genetic correlations

### Causality

### ==PRS analysis==

### TWAS

---

# Resources

- [Genome-wide association studies](https://www.nature.com/articles/s43586-021-00056-9)

- Genome-wide association studies (GWAS) aim to identify associations of genotypes with phenotypes by testing for differences in the allele frequency of genetic variants between individuals who are ancestrally similar but differ phenotypicall
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