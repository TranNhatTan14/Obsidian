### Requirements and preparatory steps

### Step 2: Chip data validation and VCF formatting

### Step 3: Align the variants alleles to human reference genome

### Step 4: Ensure the duplicate individuals do not exist

### Step 5: Exclude rare variants

### Step 6: Generate a frequency file for the chip data and the imputation reference panel allele comparision

### Compare the chip data and the imputation reference panel allele frequencies

### Exclude the variants showing highly discordant allele frequencies

### Step 9: Chip data pre-phasing

### Step 10: Genotype imputation

### Post-imputation processing and quality assurance

### Prephasing

- Before running imputation, GWAS genotypes should be phased for each sample
	- The most likely halotypes should be estimated
	- When genotypes of unrelated individuals undergo phasing, estimated halotypes are unlikely to represent the true allelic configurations along each chromosome but may provide a fragmented "best guess" of chromosomal halotypes assuming crossover events and LD patterns across the study sample.
	- Where family data is available and LD structure and crossover events are more easily predicted, chromosomal halotypes may be longer than among unrelated samples

# Q&A

- Explain what is phased genotypes