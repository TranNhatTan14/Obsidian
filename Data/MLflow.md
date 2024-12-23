- How to use MLflow to simplify the complexities of building machine learning applications
- Explore MLflow tracking, projects, models, and model registry

Managing the end-to-end lifecycle of a Machine Learning application can be a daunting task for data scientists, engineers, and developers. Machine Learning applications are complex and have a proven track record of being difficult to track, hard to reproduce, and problematic to deploy.

- Learn what MLflow is and how it attemps to simplify the difficulties of the Machine Learning lifecycle: tracking, reproducibility, and deployment
- How to overcome the complexities of building Machine Learning application and how to navigate different stages of the Machine Learning lifecycle

# Introduction

- How it aims to assist with some difficulties of the Machine Learning lifecycle
- Four main concepts that make up MLfow with a main focus on MLflow Tracking
- Learn to create experiments and runs as well as how to track metrics, parameters, and artifacts
- Search MLflow programmatically to find experiment runs that fit certain criteria
- ==MLflow has become tool of choice by many organization across many different industries==

## MLflow experiments

- The basic concept of MLflow is an experiment - a way that MLflow organizes tracking model training runs
- MLflow provides a couple of ways to work with experiments
	- MLflow client
		- Use lower-level API for interacting directly with different aspects of MLflow
	- MLflow module
		- Use higher-level API used for starting and directly managing current training runs

![[Pasted image 20240910105342.png]]

```python
improt mlflow

# Create new experiment
mlflow.create_experiment("My experiment")

# Tag new experiment
mlflow.set_experiment_tag("scikit-learn", "lr")

# Set the experiment
mlflow.set_experiment("My experiment")
```

# MLflow Tracking

- Model engineering and evaluation are two key processes of the Machine Learning lifecycle. Most model are build and reiterated several times to ensure the best performance.

- Record metrics and parameter from training runs
- Query data from experiments
- Store models, artifacts and code

## Training runs

- MLflow Tracking is organized around a concept called "runs"
- A new run mean new model training and information about the model is logged to MLflow
- Each run is placed within an experiment

```python
import mlflow

# Set the experiment
mlflow.set_experiment("My Experiment")

# Start a run
run = mlflow.start_run()

# Print run info
run.info
```

The return value of the `start_run` function can also be set as variable to get metadata about the current active run

## Logging to MLflow Tracking

![[Pasted image 20240910110834.png]]

## MLflow UI

```bash
# Open MLflow Tracking UI in http://localhost:5000
mlflow ui
```

![[Pasted image 20240910111131.png]]

## Querying runs

We can use `search_runs` function with programmatic access runs data and is used to query runs and return the data to an output for further data analysis

- `max_results` - maximum number of results to return
- `order_by` - column(s) to sort
- `filter_string` - string based query
- `experiment_names` - name(s) of experiment to query

```python
# Create a filter string for R-squared score
r_squared_filter = "metrics.r2_score > .70"

# Search runs
mlflow.search_runs(
	experiment_names=["Unicorn Sklearn Experiments", "Unicorn Other Experiments"],
	filter_string=r_squared_filter,
	order_by=["metrics.r2_score DESC"]
)
```

# MLflow Models

- Standardlize models for deployment
- Build customized models

- MLflow Models component of MLflow plays an essential role in the Model Evaluation and Model Engineering steps of the Machine Learning lifecycle
- Learn how MLflow Models standardlizes the packaging of ML models as well as how to save, log, and load
- How to create custom MLflow Models to provide more flexibility to your use cases as well as how to evaluate model performance
- Utilize the powerful concept of "Flavors" and finally use the MLflow command line tool for model deployment

- Standardizing models allows for easy intergration between popular ML libraries and deployment tools
- Packaging models refers to the process of placing all application file and resources in a strategic way, that can distributed more easily.
- Standards are defned in a format convention used for saving models in different model "Flavors" that can be understood by different downstream tools

## Built-in Flavors

- MLflow Models use a powerful concept called Flavors
	- Write custom tools to work with models from the most popular ML libraries using MLflow
	- Simplify the process of logging, packaging, and load models minimizing the need to write custom code

## Autolog

```python
# Automacally log model and metrics
mlflow.FLAVOR.autolog()

# Scikit-learn built-in flavor
mlflow.sklearn.autolog()
```

## Storage format

![[Pasted image 20240910114457.png]]

The MLmodel is a YAML file that define important information about the model. A YAML file is a human-readable serialization format used for configuration files.

![[Pasted image 20240910114813.png]]

# MLflow Model Registry

- Store and version ML models
- Load and deploy ML models

- How the MLflow Model Registry is used to manage the lifecycle of ML model
- Create and search for models in the Model Registry
- How to register models to the Model registry and how to transition model between predefined stages
- Deploy models from Model Registry

# MLflow Projects

- Package ML code for reproducibility and repeatatability

- Gain valuable knowledge on how to streamline data science code for reusability and reproducibillity using MLflow Projects
- MLflow Projects
- How to creating ML project file
- How to run MLflow Projects through both command-line and the MLflow Projects module
- Discoverin gthe power of using parameters for added flexibility in code
- Manage steps of the machine learning lifecycle by creating a multi-step workflow using MLflow Project