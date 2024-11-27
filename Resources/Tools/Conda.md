---
tags:
  - Tool
  - Bioinformatics
---
# Command

```bash
# Deactivate
conda deactivate

# Remove environment
conda env remove --name env_name

conda env create --name ICLR python=3.12

# Use conda with Jupyter Notebook
conda install -c anaconda ipykernel

conda env export > environment.yml
conda env export --no-builds > environment.yml

conda env create -f environment.yml

# Rename 
conda create --name NCBI --clone NCBI_download
conda remove --name NCBI_download --all
```