# Stats

https://www.cog-genomics.org/plink/2.0/basic_stats
https://www.cog-genomics.org/plink/2.0/ld

# Quality Control

### Imputation quality

https://www.cog-genomics.org/plink/2.0/filter

--mach-r2-filter [min] [max]  
--minimac3-r2-filter <min> [max]

**--mach-r2-filter** excludes variants where the MaCH Rsq imputation quality metric (frequently labeled as 'INFO') is outside [0.1, 2.0]; change the bounds by providing parameters. Monomorphic variants, where Rsq == nan, are not excluded by this filter: the problem with them isn't imputation quality.

Similarly, **--minimac3-r2-filter** excludes variants where [Minimac3's imputation quality metric](https://genome.sph.umich.edu/wiki/Minimac3_Info_File#Rsq) is outside the given range. **Note that this metric assumes that phased dosages have been imported with e.g. [--vcf's dosage=HDS option](https://www.cog-genomics.org/plink/2.0/input#vcf)**; the computation still proceeds when unphased dosages are present, but the results will be underestimates. If you don't need phased dosages for any other reason, [--{extract,exclude}-if-info](https://www.cog-genomics.org/plink/2.0/filter#extract_if_info) is usually a more efficient way to do this properly.

"--minimac3-r2-filter 1" can be used to keep only perfectly-imputed-and-phased variants.

Lựa chọn tham số dựa trên dữ liệu

# Associate

https://www.cog-genomics.org/plink/2.0/assoc

- Phân tích với dữ liệu bệnh và VN1K
- Bệnh và sub VN1K có giới tính và độ tuổi tương đồng
- Bệnh và VN1K imputed trên 1KGP

- Phân tích cho rare variant

```bash
# Association Test - Additive Model with Firth fallback
plink2 \
    --bfile $OUTPUT/QC/S11_QC_clean \
    --glm no-x-sex firth-fallback hide-covar \
    --covar $OUTPUT/PCA/S12_GWAS.covar \
    --covar-variance-standardize \
    --out firth_fallback_additive

# Association Test - Additive Model with Firth residualize
plink2 \

    --bfile $OUTPUT/QC/S11_QC_clean \
    --glm no-x-sex hide-covar firth firth-residualize \
    --covar $OUTPUT/PCA/S12_GWAS.covar \
    --covar-variance-standardize \
    --out firth_residualize_additive
```

Input file is QC_clean

### Firth

Also, when working with unbalanced binary phenotypes, be aware that Firth regression can be similar to adding a [pseudocount](https://en.wikipedia.org/wiki/Additive_smoothing) of 0.5 to the number of case and control minor allele observations, so weird things happen when the _expected_ number of case minor allele observations is less than 0.5. You probably don't want to throw out every variant with MAC 300 when your case:control ratio is 1:600 (you may still have excellent power to detect _positive_ association between the minor allele and case status, after all), but you shouldn't take reported odds-ratios or p-values literally for those variants.

To trade off some accuracy for speed:

- You can use the '**single-prec-cc**' modifier to request use of single-precision instead of double-precision floating-point numbers during logistic and Firth regression.
- You can use the '**firth-residualize**' or '**cc-residualize**' modifier, which implements the shortcut described in [Mbatchou J et al. (2021) Computationally efficient whole genome regression for quantitative and binary traits](https://www.nature.com/articles/s41588-021-00870-7) to just Firth, or both Firth and logistic, regression respectively. 
- Similarly, you can use '**qt-residualize**' to regress out covariates upfront for quantitative traits. (These must be used with 'hide-covar', disable some other --glm features, and are not recommended if you have a significant number of missing genotypes or have any other reason to expect covariate betas to change in a relevant way between variants.)

### Sex

For binary phenotypes, --glm fits a logistic or Firth regression model instead, with the same **G**βG + **X**βX terms.

First, sex (as defined in the .fam/.psam input file) is normally included as an additional covariate. If you don't want this, add the '**no-x-sex**' modifier. Or you can add the '**sex**' modifier to include .fam/.psam sex as a covariate everywhere. 

> [!warning]
> Don't include sex from the .fam/.psam file and the --covar file at the same time; otherwise the duplicated column will cause the regression to fail.

### Hide covariate

By default, for every variant, this file contains a line for each genotype column _and a line for each non-intercept covariate column_. If you're not actually using any information in the covariate lines, the '**hide-covar**' modifier can greatly reduce file sizes. (See also [--pfilter](https://www.cog-genomics.org/plink/2.0/assoc#pfilter) below.) Or, going in the other direction, the '**intercept**' modifier lets you also see the intercept-column fit.
































































### Alleles

Different versions of the same variant are called alleles. For example, a SNP may have two alternative bases, or alleles, C and T4.

###### Variant

Genetic variation is the difference in DNA sequences between individuals within a population

[Type of genetic variation](https://www.ebi.ac.uk/training/online/courses/human-genetic-variation-introduction/what-is-genetic-variation/types-of-genetic-variation/)

###### VCF

**VCF is the standard file format** for storing variation data. It is used by large scale variant mapping projects.

VCF is a preferred format because it is **unambiguous, scalable and flexible**, allowing extra information to be added to the info field. Many millions of variants can be stored in a single VCF file.

VCF files are tab delimited text files.

###### Linkage Disequilibrium

In the genome, alleles at variants close together on the same chromosome tend to occur together more often than is expected by chance. These blocks of alleles are called haplotypes. **Linkage disequilibrium** (LD) is a measure of how often two alleles or specific sequences are inherited together, with alleles that are always co-inherited said to be in linkage disequilibrium.

---
- It is now standard practice to include top principal components as covariates in association analysis, to correct population stratification.
- Also, when working with unbalanced binary phenotypes, be aware that Firth regression can be similar to adding a [pseudocount](https://en.wikipedia.org/wiki/Additive_smoothing) of 0.5 to the number of case and control minor allele observations, so weird things happen when the _expected_ number of case minor allele observations is less than 0.5. You probably don't want to throw out every variant with MAC < 300 when your case:control ratio is 1:600 (you may still have excellent power to detect _positive_ association between the minor allele and case status, after all), but you shouldn't take reported odds-ratios or p-values literally for those variants.