---
tags:
  - Tool
  - Bioinformatics
URL: https://bactopia.github.io
---
# Definition

Can use with [[Nextflow]], [[Conda]], [[Docker]]

REMEMBER to remove work folder it can cause 500 Gb for only 50 Gb data

# Accession

An accession is an identifier assigned to a genetic sequence or dataset when it is submitted to a public database, such as GenBank, ENA (European Nucleotide Archive), or DDBJ (DNA Data Bank of Japan). For example:

A DNA sequence submitted to GenBank might receive an accession number like NC_000001.11, which corresponds to a specific version of human chromosome 1.
Accession numbers help ensure that researchers can reliably locate and refer to sequences or datasets for their studies.

```bash
bactopia prepare

bactopia seach

bactopia atb-formatter
```

[Run from GitHub Repository](https://bactopia.github.io/v3.1.0/quick-start/#run-from-github-repository)

Missing out on helper commands

The Conda install of Bactopia comes with a few helper commands that are not available when running directly with Nextflow. These include commands to help prepare sample sheets, search public databases, pre-build environments, among other helper tools.

# Resources

https://datasets.bactopia.com/media/2024-asmngs-bactopia.pdf
https://datasets.bactopia.com/media/2024-bactopia-toast.pdf