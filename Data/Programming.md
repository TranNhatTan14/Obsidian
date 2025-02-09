---
tags:
  - Skill
---
### CUDA

### C++

### R

### JaveScript

- Delve into advanced concept such as OOP and Algorithm optimization.
- Understanding how to write efficient, scalable code is crucial since AI applications often process large amounts of data. 
- Practice by contributing to open-source projects or tackling complex problems that challenge your coding skills.
- Writing clean, efficient, and scalable code.
- Understand the principles of software engineering, including version control, testing, and debugging. 

# Python

### [[Concurrency in Python]]

- https://github.com/cline/cline
	- Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way.
- https://github.com/astral-sh/uv
	- An extremely fast Python package and project manager, written in Rust.

### Print the default value of function

https://stackoverflow.com/questions/12627118/get-a-function-arguments-default-value

Follow the OOP and code standard
# Framework

### Polars

- Pandas/Polars for data manipulation and analysis
- GPU with Polars, Daniel Warfield https://pola.rs/posts/gpu-engine-release

### LangChain

LLM Graph Transformer
### Modular

A high-performance generative AI framework

https://www.modular.com

### Pandas

```bash
first_sample_dict = df.iloc[0].to_dict()
first_sample_dict

# Print the unique values in the specific column and count how many samples fall under each unique value
unique_values = df['assembly_level'].value_counts()
print(unique_values)

# Filtet value
# Merge the dataframes on 'LID'
merged_df = pd.merge(str, ethnic[['LID', 'Dân tộc']], on='LID', how='inner')
```

### uv

https://github.com/astral-sh/uv

# Q&A

What is MAX?

[**MAX**](https://www.modular.com/max) is a free and permissive AI inference framework that enables developers and enterprises to develop and deploy AI inference workloads on any hardware type, into any type of environment (including into production). [**You can read more about MAX here**](https://docs.modular.com/max/)**.**

What is Mojo?

[**Mojo**](https://www.modular.com/mojo) is a new programming language that has the expressiveness of Python, with the performance of C. Mojo is a member of the Python family and powers critical parts of our infrastructure. Mojo is completely optional to use, as MAX supports Python, C++ and other languages natively. [**You can read more about Mojo here**](https://docs.modular.com/mojo/why-mojo)**.**