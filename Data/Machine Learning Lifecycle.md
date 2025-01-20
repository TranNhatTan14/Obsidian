# Problem and System

## Problem define

## System Design

- Đọc yêu cầu của khách hàng
- Xem tác vụ này có xử lý được bằng AI không
- Input là gì
- Output là gì
- Phân tích dữ liệu
- Bài toán thuộc dạng nào
- Tốc độ nhanh và độ chính xác cao

# Data

## Data Collection

- Collect relevant data include private data from company and public dataset
- Understand data and context, representation and measurement, potential bias.

- Tools: Apache Airflow, Luigi, AWS Glue
- Data lakes: Amazon S3, Azure Data Lake
- Databases: PostgreSQL, [[MongoDB]], Cassandra

## Data Storage

## Exploratory Data Analysis (EDA)

- Data visualization and statistical analysis
- Tools: Matplotlib, Seaborn, Plotly, Tableau

The goals of EDA are aim to understand the data and unearth patterns and detect outliers - does data fall outside acceptable ranges? **Designing hypotheses** to validate and check assumptions is vital - does what we expect line up with reality? The EDA stage often influences the choice of ML algorithm, the selection of specific features, and the need for feature engineering; these questions are vital to the future success of the project.

- Understand the data
	- Are the any patterns
- Detect outliers
	- Does any data fall outside what is acceptable
	- Are there incorrect or missing values
- Formulate hypotheses
	- What should we expect from the data
- Check assumptions
	- Does what we expect line up with reality

### Null and missing data

### Class (Im)balance

### Normalize

### Outliers

![[Pasted image 20240810173549.png]]
### Visualizing data

## Data Preparation

Data preparation is an essential part of the machine learning lifecycle, also ==often referred to as data preprocessing or data cleaning==. This step helps ensure the model is working with quality data, thereby increasing the potential accuracy of its predictions.

Deal with problem in EDA include imputation

### Data Augmentation

## Data quality

- The core of the Machine Learning model: Trash in, trash out
- Data quality can be defined along four main dimensions, namely accuracy, completeness, consistency, and timeliness.

![[Pasted image 20240810141314.png]]

## Data Ingestion

- Typically, in the design phase, we also look into how to extract and process data. This is done by using an automated data pipeline, of which we see a high-level example here. A data pipeline is often a part within the machine learning lifecycle through which data is automatically processed. 
- A common type of data ingestion process is ETL, which stands for extract, transform, and load.
- It describes the three steps gone through in an ETL pipeline. The data is extracted from the source, transformed to the required format, and loaded into some internal or proprietary database. In an ETL pipeline, we can also include automated checks, such as expectations we have about certain data columns. 

### ETL (Extract, Transform, Load) processes

ETL is ==a set of computer instructions that combine data from different systems into a single database or data store==

- Build complex ETL code

- Build complex Data Engineering workflows
- Create complex data solutions and build data pipelines
- Establish credibility and build impactful relationships with our customers to enable them to be cloud advocates
- Capture and share industry best practices amongst the community
- Attend and present valuable information at Industry Events

- Build effective, performant, and reliable data pipelines using Extract, Transform, and Load principles

- Experience in dealing with databases and building ETL pipelines
- Experience ETLing large amounts of data (preferably, with AI) in production

## Data Profiling

Within MLOps, data profiling refers to the **automated data analysis and creation of high-level summaries**, called data profiles, or expectations, which we use for validating and monitoring data in production.

# Feature

## Feature Engineering

![[Pasted image 20240810180610.png]]

Feature engineering is the process of selecting, manipulating, and transforming raw data into features. A feature is a variable, such as a column in a table. How we create features from the data is an important part of machine learning development. We can use the features as they appear in the raw data, but we can also build our own.

### Feature engineering weigh-off

More features can

- Produce a very accurate model
- Achieve more stability
- Be more expensive due to additional pre-precessing steps
- Require more maintenance
- Lead to noise, or over-engineering
### Normalization

### Standardization 

- Standardization scales features to have a mean of zero and a variance of one. Standardization benefits algorithms that assume features are centered around zero and have variance in the same order, like in Support Vector Machines (SVMs) and Linear Regression. 
- We can use the sklearn.preprocessing.StandardScaler function for standardization. Similarly to normalization, we create a standard scaler object, pass our heart disease DataFrame as an argument, and get a standardized version of the data back

## Feature Selection

## Feature Store

- The feature store is a tool through which features can be managed and easily accessed by multiple people working of different projects.
- When you want to collaborate with multiple people on multiple project that share the same feature sets, it is a great time to start using a feature store. In this way, you can avoid doing the same repeated work to get the same features.
- The benefit of feature store is **reusabiity** and **consistency**.
- Advanced features stores are implemented as so-called dual databases, one for grabbing the training data and the other for making predictions

![[Pasted image 20240810143322.png]]

# Model

## Model Selection

## Model Training

## Model Validation

## Model Optimization

# Evaluation

### Evaluation Metrics

### Cross validation

- When it comes to validating our models, cross-validation provides another robust way to estimate performance by providing an average score across different splits on our dataset. This way, we ensure our performance is not dependent on one arbitrary split. k_fold cross_validation is a resampling procedure used to evaluate models on limited data. 
- The procedure has a single parameter, k, for the number of groups that the data sample will be split into. Since our heart disease dataset is quite small, k_fold cross_validation is a good choice. Here is a visualization of k-fold cross-validation with k equals five. We partition the data into five equal groups, and for each different group, we train the model with four parts training data and one part testing data.

![[Pasted image 20240810181806.png]]

# DevOps and MLOps

## Version Control

## Containerization

[[Docker]]

## Orchestration

- Managing containerized applications
- [[Kubernetes]]

## CI/CD

Tools: Jenkins, GitLab CI, GitHub Actions

## Serving

- Deploying models as APIs
- Tools: Flask, FastAPI, TensorFlow Serving

# Production and Monitoring

## Deployment

- Integration with production systems
- Cloud platforms: AWS SageMaker, Google Cloud AI Platform, Azure Machine Learning

```bash
apt install

brew install

conda create -n

docker-compose up

kubectl apply -f
```

## Monitoring and Logging

- Tracking model performance and system health
- Tools: Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana)

## Testing

# Governance and Security

## Data Governance

- Ensuring data quality, privacy, and compliance
- Tools: Apache Atlas, Collibra

## Model Governance

- Model documentation and lineage tracking
- Tools: [[MLflow]], DVC ([[Data Version Control]])

## Security

- Securing data and model access
- Tools: HashiCorp Vault, AWS IAM