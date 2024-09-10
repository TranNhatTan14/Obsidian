---
links:
  - "[[Machine Learning Lifecycle]]"
description: Machine Learning Operations is an extension of the DevOps framework, not a subset or alternative.
---
Model build pipiline > Model pipeline
### Data Engineer

- Extract raw data from different sources and store in a centrailized place
- **Design and maintain data pipelines** to ensure efficient data flow and accessibility for analysis.
- Make sure that incoming data is validated according to data quality requirements.

### Machine Learning Engineer

That's correct! The machine learning engineer is responsible for deploying the model. Having clear roles and responsibilities leaves no confusion as to who does what, which can greatly speed up the lifecycle.

### Data Scientist

- Assess the performance of the machine learning model according to the performance requirements
- Develop and implement ML model to solve specific bussiness problems
- Perform hyperparameter tuning to make sure the model training process is optimized

Understanding Machine Learning Operations (MLOps) is essential for any data scientist, engineer, or leader to ==take machine learning models from a local notebook to a functioning model in production==. This course introduces you to the key processes, phases, and levels of MLOps, including ==design, development, deployment, and monitoring==. You'll discover how ==automation== enables organizations to efficiently launch, monitor, and update their machine learning models.

# Design

The design phase is the most important phase within the machine learning lifecycle. Without a decent objective and high-quality data, the other two phases might fail

![[Pasted image 20240810150942.png]]

###### Added value

### Business requiremets

### Key metrics

# Development

![[Pasted image 20240810151023.png]]

## Data

## Feature


### Feature selection

### Feature Store

## Model

### Model Selection

### Model Training

### Model Evaluation

- Accuracy
- Confusion matrix

### Model registry

Just as it is important to manage and store the features as model inputs, it is crucial to manage and store the models' outputs themselves - our patients need timely, accurate, and persistent access to their diagnoses as they become available. Model registries are a form of version control system for machine learning models. They help us manage and keep track of different versions of our machine learning models. Model registries allow us to annotate our models with rich metadata, compare different models, and track their performance over time. This not only makes our work more organized but it also increases transparency and reproducibility in our machine learning workflows. We have already been exposed to model registries in the form of MLflow. Remember that MLflow allows us to manage and track machine learning experiments, log model performance metrics, and even store trained model artifacts for cross-comparison.

Formart of the output model in PyTorch or pickle or what

![[Pasted image 20240810182432.png]]
# Experiment tracking

### Logging experiments on MLFlow

![[Pasted image 20240810181223.png]]

Why is experiment tracking important?

During machine learning experiments, we can configure different machine learning models, for example, linear regression or deep neural networks. We can alter the model hyperparameters, like the number of layers in a neural network. We could use different versions of the data and different scripts to run the experiment. We can also use different environment configuration files per experiment, like what version of Python or R are used and what libraries. When altering each of these factors during experiments, the amount of different configurations can become huge. Each experiment also has a different outcome. This is why it is a good idea to track the configurations and the results of each experiment.

You want to find and log what algorithms works best on this data in multiple configuration.

So working with model and configuration file about what use with date

1. Fomulate a hypothesis
2. Gather data
3. Define experiments: type of models, hyperparameters, datasets
4. Setup experiment tracking
5. Train the model
6. Evaluate the model
7. Register the most suitable model
8. Visualize and report back to team and determine next steps

###### Hyperparameter tuning

### Metadata store

###### Data Versioning

Purpose for Reproducibility

Tool can use is DVC, which stand for Data, Version, Control

# Model Serving

### Model-as-a-service

Up until now, we have operated under the assumption that our stakeholders or model users will access the model over the internet. This architecture is usually called model-as-a-service; essentially, after deployment, we surface the model to the users through some secure portal. They would then post their queries and/or patient data, and receive diagnosis predictions back over the internet. However, what if our clinic was rural? What if, for some reason, they did not have access to the internet? We could also imagine, for example, that our stakeholders had to operate in a highly secure environment, and that model predictions or patient data was sensitive, and could not be passed over the internet for security reasons. This is very common in healthcare especially, considering that patient data is highly sensitive and personal.

### On-device serving

![[Pasted image 20240810183652.png]]

- In this case, it might make more sense to serve the model on-device, or as a part of a given application, instead of an external service to be queried. In this type of serving architecture, the model is integrated into the device or application itself. This is often done for edge computing applications, where the model needs to run on a device without a reliable network connection.
- On device model serving has a number of benefits. 
	- For example, on-device models often have faster response times as they don't have to rely on an external server. This is particularly useful for applications that require real-time predictions. 
	- Additionally, as mentioned before, on-device serving means internet access is not required. This minimizes the risk of data breaches, especially with sensitive information. 
- Offline access also allows for a wider range of applications, especially in remote or disconnected areas.
- Edge devices, however, can have limited memory and processing power. This means the model has to be optimized and lightweight, potentially compromising accuracy for speed. On-device models might not benefit from the kind of scalability cloud infrastructure offers. If an application with an on-device model becomes popular, it won't face the traditional server-side scaling issues but might face challenges related to diverse device capabilities and OS versions. Without a connection to a central server, pushing model updates now poses a challenge. There might be a need for physical updates or limited periodic connectivity to fetch updates. It's also harder to aggregate usage statistics, performance metrics, and potential model drift when the model is on a device. Special strategies must be in place for this.

### Implementation strategies

As with model-as-a-service, on-device model serving also involves many different deployment and implementation techniques. For example, pruning parts of a large model can make the model lighter and faster. Instead of training a big model from scratch, we can leverage pre-trained models and fine-tune them for specific tasks - this is called transfer learning. There are also many machine learning frameworks tailored for on-device and edge deployment, such as TensorFlow Lite, Core ML (for Apple devices), and ONNX Runtime. We won't go into detail on these techniques! However, feel free to research them further on your own time.

### Prediction

### Batch prediction

### On-demand prediction

Also online or dynamic prediction

![[Pasted image 20240811153806.png]]

Near-real time prediction a.k.a. Stream processing
Real-time prediction

![[Pasted image 20240811153956.png]]

# Deployment

### Model deployment strategies

### Bluen/Green deployment

The choice of the deployment strategy is always a compromise between speed and risk. When risk is virtually nonexistent, we should opt for the simplest and fastest strategy: the blue/green deployment.

### Canary deployment

### Shadow deployment

Define the target infrastructure

### Transparency and Reproducibility

Who trained the model, when, which script is used, which metadata

![[Pasted image 20240810151045.png]]

### Testing

![[Pasted image 20240811154637.png]]



### Runtime environment

![[Pasted image 20240810145013.png]]

### Microservices architecture

Using a microservices architecture allows multiple teams to work on isolated parts of the application since problems in one microservice won't affect other microservices. This also helps to scale up different services in your application since they function independently.

The microservice architecture structures an application as a collection of separate services. This enables **fast, continuous, and reliable delivery** of big, complex applications.

![[Pasted image 20240810145627.png]]

###### Application Programming Interface (API)

![[Pasted image 20240810145648.png]]

![[Pasted image 20240811154424.png]]
#### Intergration

After the model has been deployed as a microservice and the API allows us to inference the model, one last step is required. The last step is to integrate the model within the business process. This is different for each business, but most of the time involves connecting the API with the system that is already in place. Before we actually use the machine learning model in production, it is common practice to first test the model with a sample of the data to make sure everything works as expected.

### Packagaing and Containerization

Containerization can be a great way to structure your application and therefore improve the processes in your machine learning lifecycle.

Pros and Cons

Low maintainance
Can be moved to where you want
Short startup times, don't requires separate machine and own operating systems
Make applications run faster

### CI/CD pipeline

The CI/CD pipeline provides automation such that new changes can be made easily and always go through thorough automated checks.

Multiple people want to work on the same code and each time we develop and deploy new code we have to do the same repetitive tasks.

Setting up a CI/CD pipeline can be tedious at the start, but it can greatly speed up the deployment process. It is like having a list of checks to do before the launch of a new recipe in a restaurant. We can easily make a new recipe, make changes to the recipe, and check whether it is in accordance with the current processes. To summarize, continuous integration is a set of practices while the code for running the machine learning model is being written. Continuous deployment is a set of practices after the code is completed.

![[Pasted image 20240810150044.png]]

###### Continous Integration

Continuous integration is the practice where code changes are continuously integrated quickly and frequently. Each change is automatically tested when these are committed and merged. In this way, we can identify errors and bugs easily and make sure that many developers can work together on the same code.

###### Continous Deployment

Continuous deployment works together with continuous integration by automating the release of the code that was validated during the continuous integration process. The goal of the practice of continuous deployment is to always have production-ready code.

###### Deployment strategies

We have three deployment strategies

1. Basic deployment
2. Shadow deployment
3. Canary deployment

![[Pasted image 20240810150332.png]]

![[Pasted image 20240810150405.png]]

###### CI/CD with AWS Elastic Beanstalk

While AWS Elastic Beanstalk provides a great platform for deploying machine learning models, many alternatives exist, especially if you're working in a different cloud environment. For instance, **Azure Machine Learning** provides similar functionality for deploying ML models. It has tools to create real-time scoring services for models, manage compute resources for training, and monitor the performance of models in production.

Google Cloud Platform also has a similar solution called **App Engine**, which can be used as an alternative.

###### Kubernetes

Another option is Kubernetes, an open-source container orchestration system for automating the deployment, scaling, and management of containerized applications. Kubernetes works on many cloud platforms, including GCP, Microsoft Azure, and AWS. Kubernetes might have a steeper learning curve than some platform-specific tools, but it offers much flexibility and control over your deployments.

# Monitoring and Maintenance

###### Types of monitoring

Monitoring the machine learning performance in production is one of the key aspects of maintaining the model in the long term. A combination of statistical and computational metrics will help to have a sustainable machine learning model.

###### Visualization

###### Data drift and concept drift and variate drift

Data drift describes a change in the input data. Over time, we could get customers of different ages or customers from different regions. Changes in the input data might affect the performance of the machine learning model, but since data inherently changes, this is not necessarily the case.

Concept drift describes a change in the relationship between the input data and the target variable. This could be the case when our customer's behavior changes. This would, for instance, happen when the same input data causes a customer to not churn instead of churn. In that case, the relationship between the input and output data has changed. Concept drift could cause our model performance to deteriorate because the patterns that the model was previously trained on do not hold anymore.

### Feedback loop

![[Pasted image 20240810183352.png]]
### Retraining

When we retrain, a new model is obtained by using new data. We could either use a model that only uses new data, such that there is a separate model trained on old data and a model trained on new data.

We could also combine new and old data to develop a new model. This will also depend on the domain, cost, and required model performance.

### Automation and scalability

ML workflow automation == MLOps maturity

Being aware of the different levels of MLOps maturity shows in what areas the machine learning pipeline can be improved, which enables you to speed up MLOps processes in your company.

We can look at a machine learning lifecycle and determine how mature its MLOps practices are. The MLOps maturity is about the automation, collaboration, and monitoring within machine learning and operations processes in a business. It does not necessarily mean that a higher level of MLOps maturity is better.

The levels mostly apply to the development and deployment phase. The design phase cannot be fully automated since it requires human input from multiple different roles, but templates can be used in order for the phase to progress more quickly and smoothly.

![[Pasted image 20240810155734.png]]