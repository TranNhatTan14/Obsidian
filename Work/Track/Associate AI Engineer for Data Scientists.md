### Track Description

Train and fine-tune the latest AI models for production, including LLMs like Llama 3. Start your journey to becoming an AI Engineer today!

# [[Supervised Learning]] with scikit-learn

Grow your machine learning skills with scikit-learn in Python. Use real-world datasets in this interactive course and learn how to make powerful predictions!

Grow your machine learning skills with scikit-learn and discover how to use this popular Python library to train models using labeled data. In this course, you'll learn how to make powerful predictions, such as whether a customer is will churn from your business, whether an individual has diabetes, and even how to tell classify the genre of a song. Using real-world datasets, you'll find out how to build predictive models, tune their parameters, and determine how well they will perform with unseen data.

Naming conventions

- Feature = predictor variable = independent variable
- Target variable = dependent variable = response variable

Data Inputs

- No missing values
- Data in numeric format
- Data stored in Pandas DataFrame or Numpy array

## Classification

In this chapter, you'll be introduced to classification problems and learn how to solve them using supervised learning techniques. You'll learn how to split data into training and test sets, fit a model, make predictions, and evaluate accuracy. You’ll discover the relationship between model complexity and performance, applying what you learn to a churn dataset, where you will classify the churn status of a telecom company's customers.

# k-Nearest Neighbors

We commonly use 20-30% of our data as the test set. By setting the test_size argument to zero-point-three we use 30% here. The random_state argument sets a seed for a random number generator that splits the data. Using the same number when repeating this step allows us to reproduce the exact split and our downstream results. 

It is best practice to ensure our split reflects the proportion of labels in our data. So if churn occurs in 10% of observations, we want 10% of labels in our training and test sets to represent churn. We achieve this by setting stratify equal to y. train_test_split returns four arrays: the training data, the test data, the training labels, and the test labels. 

We unpack these into X_train, X_test, y_train, and y_test, respectively. We then instantiate a KNN model and fit it to the training data using the dot-fit method. To check the accuracy, we use the dot-score method, passing X test and y test. The accuracy of our model is 88%, which is low given our labels have a 9 to 1 ratio.

Model complexity

- Large k = less complex model = can cause underfitting
- Smaller k = more complex model = can lead to overfitting

## Regression

In this chapter, you will be introduced to regression, and build models to predict sales values using a dataset on advertising expenditure. You will learn about the mechanics of linear regression and common performance metrics such as R-squared and root mean squared error. You will perform k-fold cross-validation, and apply regularization to regression models to reduce the risk of overfitting.

- Chúng ta có danh sách rất nhiều features và cần lựa chọn những features quan trọng đem lại kết quả tốt nhất
- R2: quantifies the variance in target value explained by the features

![[Pasted image 20240922105149.png]]

## Cross- validation

If we're computing R-squared on our test set, the R-squared returned is dependent on the way that we split up the data! The data points in the test set may have some peculiarities that mean the R-squared computed on it is not representative of the model's ability to generalize to unseen data. To combat this dependence on what is essentially a random split, we use a technique called cross-validation.

Cross-validation is a vital approach to evaluating a model. It maximizes the amount of data that is available to the model, as the model is not only trained but also tested on all of the available data.

An average score of `0.75` with a low standard deviation is pretty good for a model out of the box! Now let's learn how to apply regularization to our regression models.

```python
# Print the mean
print(np.mean(cv_results))

# Print the standard deviation
print(np.std(cv_results))

# Print the 95% confidence interval
print(np.quantile(cv_results, [0.025, 0.975]))
```

## Regularization

![[Pasted image 20240922105752.png]]

### Ridge regression

![[Pasted image 20240922105854.png]]

Well done! The scores don't appear to change much as `alpha` increases, which is indicative of how well the features explain the variance in the target—even by heavily penalizing large coefficients, underfitting does not occur!

### Lasso regression

![[Pasted image 20240922110023.png]]

```python
# Import Lasso
from sklearn.linear_model import Lasso

# Instantiate a lasso regression model
lasso = Lasso(alpha=0.3)

# Fit the model to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)
plt.bar(sales_columns, lasso_coef)
plt.xticks(rotation=45)
plt.show()
```

# Evaluate

- Precision
- Recall
- Confusion matrix
- F1-score

- A model predicting the presence of cancer as the positive class.
	This model should minimize the number of false negatives, so **recall** is a more appropriate metric.
- A classifier predicting the positive class of a computer program containing malware.
	To avoid installing malware, false negatives should be minimized, hence **recall** or **F1-score** are better metrics for this model.
- A model predicting if a customer is a high-value lead for a sales team with limited capacity.
	Correct! With limited capacity, the sales team needs the model to return the highest proportion of true positives compared to all predicted positives, thus minimizing wasted effort.

### Logistic Regression

The ROC curve
The ROC AUC

## Fine-tuning model

Having trained models, now you will learn how to evaluate them. In this chapter, you will be introduced to several metrics along with a visualization technique for analyzing classification model performance using scikit-learn. You will also learn how to optimize classification and regression models through the use of hyperparameter tuning.

### Hyperparameters tuning

Grid search cross-validation
RandomizedSearchCV

```python
# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

# Set up the parameter grid
param_grid = {"alpha": np.linspace(0.00001, 1, 20)}

# Instantiate lasso_cv
lasso_cv = GridSearchCV(lasso, param_grid, cv=kf)

# Fit to the training data
lasso_cv.fit(X_train, y_train)
print("Tuned lasso paramaters: {}".format(lasso_cv.best_params_))
print("Tuned lasso score: {}".format(lasso_cv.best_score_))
```

Well done! Unfortunately, the best model only has an R-squared score of `0.33`, highlighting that using the optimal hyperparameters does not guarantee a high performing model!

## Preprocessing and Pipelines

Learn how to impute missing values, convert categorical data to numeric values, scale data, evaluate multiple supervised learning models simultaneously, and build pipelines to streamline your workflow!

### Dealing with categorical features in Python

- scikit-learn: OneHotEncoder()
- pandas get_dummies()

### Handling missing data

- Remove
- Imputing values
	- Use subject-matter expertise
	- Common to use the mean, median, ...
	- For categorical values, we typically use the most frequent value
	- Must split our data first, to avoid data leakage

### Centering and scaling

- Model affected by scaling
	- KNN
	- Linear Regression (and Ridge, Lasso)
	- Logistic Regression
	- Artificial Neural Network
- Best to scale data before evaluating models

## Evaluating multiple models

- Regression
	- RMSE
	- R2
- Classification
	- Accuracy
	- Confusion matrix
	- Precision, Recall, F1-score
	- ROC AUC

```python
models = {"Linear Regression": LinearRegression(), "Ridge": Ridge(alpha=0.1), "Lasso": Lasso(alpha=0.1)}
results = []

# Loop through the models' values
for model in models.values():
  kf = KFold(n_splits=6, random_state=42, shuffle=True)
  
  # Perform cross-validation
  cv_scores = cross_val_score(model, X_train, y_train, cv=kf)
  
  # Append the results
  results.append(cv_scores)
  
# Create a box plot of the results
plt.boxplot(results, labels=models.keys())
plt.show()

# Import mean_squared_error
from sklearn.metrics import mean_squared_error

for name, model in models.items():
  
  # Fit the model to the training data
  model.fit(X_train_scaled, y_train)
  
  # Make predictions on the test set
  y_pred = model.predict(X_test_scaled)
  
  # Calculate the test_rmse
  test_rmse = mean_squared_error(y_test, y_pred, squared=False)
  print("{} Test Set RMSE: {}".format(name, test_rmse))

# Create models dictionary
models = {"Logistic Regression": LogisticRegression(), "KNN": KNeighborsClassifier(), "Decision Tree Classifier": DecisionTreeClassifier()}
results = []

# Loop through the models' values
for model in models.values():
  
  # Instantiate a KFold object
  kf = KFold(n_splits=6, random_state=12, shuffle=True)
  
  # Perform cross-validation
  cv_results = cross_val_score(model, X_train_scaled, y_train, cv=kf)
  results.append(cv_results)
plt.boxplot(results, labels=models.keys())
plt.show()
```

```python
# Create steps
steps = [("imp_mean", SimpleImputer()), 
         ("scaler", StandardScaler()), 
         ("logreg", LogisticRegression())]

# Set up pipeline
pipeline = Pipeline(steps)
params = {"logreg__solver": ["newton-cg", "saga", "lbfgs"],
         "logreg__C": np.linspace(0.001, 1.0, 10)}

# Create the GridSearchCV object
tuning = GridSearchCV(pipeline, param_grid=params)
tuning.fit(X_train, y_train)
y_pred = tuning.predict(X_test)

# Compute and print performance
print("Tuned Logistic Regression Parameters: {}, Accuracy: {}".format(tuning.best_params_, tuning.score(X_test, y_test)))
```

Nicely done! Lasso regression is not a good model for this problem, while linear regression and ridge perform fairly equally. Let's make predictions on the test set, and see if the RMSE can guide us on model selection.
# [[Unsupervised Learning]] in [[Python]]

![[Pasted image 20240922102959.png]]

Clustering for Dataset Exploration

Visualization with Hierarchical Clustering and t-SNE

Decorrelating Data and Dimension Reduction

Discovering Interpretabe Features

# [[Deep Learning]] with [[PyTorch]]

## PyTorch

## Training Neural Network with PyTorch

Great work, the loss outputs 81, the square of 9, as expected! The MSE loss is also called L2 loss. Another common loss function for regression problem is the mean absolute error loss, also called L1 loss.

## Neural Network Architecture and Hyperparameters

Hyperparameters are parameters, often chosen by the user, that control model training. The type of activation function, the number of layers in the model, and the learning rate are all hyperparameters of neural network training. Together, we will discover the most critical hyperparameters of a neural network and how to modify them.

- Activation functions add non-linearity to models after linear transformations.
  
- **Sigmoid Function Limitations**:  
  - Output bounded between 0 and 1.  
  - Gradients (derivatives) are small and approach zero for extreme values of x, leading to **saturation**.  
  - Saturation causes **vanishing gradients**, making training difficult.

We'll add non-linearity to model using activation functions.

Limitations of the signmoid and softmax function

- The output of the signmoid function and softmax function are bounded between zero and one.
- The derivatives (gradients) of the signmoid function are always low and approach zero for extreme values of x. This behavior is called saturation, it creates a challegene during backpropagation because each local gradient is a function of the previous gradient. For extreme values of x, the gradient will be so small that it can prevent the weight from changing or updating
- Saturations cause vanishing gradients, making training difficult.

![[Pasted image 20240922211407.png]]

- **ReLU (Rectified Linear Unit)**:  
  - Outputs the maximum of input and zero.  
  - Solves vanishing gradients by allowing larger gradients for positive values.  
  - Common choice in deep learning.  
  - Can be called using the `nn` module in PyTorch.

![[Pasted image 20240922212540.png]]

```python
# Create a ReLU function with PyTorch
relu_pytorch = nn.ReLU()

# Apply your ReLU function on x, and calculate gradients
x = torch.tensor(-1.0, requires_grad=True)
y = relu_pytorch(x)
y.backward()

# Print the gradient of the ReLU function for x
gradient = x.grad
print(gradient)
```

Performing the backward pass to compute gradients:

We call the `backward()` method on `y` to compute the gradient of `y` with respect to `x`. This step calculates the derivative of the ReLU function at `x`.

Correct! A good rule of thumb is to use ReLU as the default activation function in your models (except for the last layer).

### Leaky ReLU

  - Similar to ReLU for positive inputs.  
  - For negative inputs, it multiplies by a small coefficient (default 0.01 in PyTorch), preventing zero gradients.  
  - The coefficient is controlled by the `negative_slope` parameter.

You've learned that ReLU is one of the most used activation functions in deep learning. You will find it in modern architecture. However, it does have the inconvenience of outputting null values for negative inputs and therefore, having null gradients. Once an element of the input is negative, it will be set to zero for the rest of the training. Leaky ReLU overcomes this challenge by using a multiplying factor for negative inputs.

```python
# Create a leaky relu function in PyTorch
leaky_relu_pytorch = nn.LeakyReLU(negative_slope=0.05)

x = torch.tensor(-2.0)
# Call the above function on the tensor x
output = leaky_relu_pytorch(x)
print(output)
```

That's correct! Leaky ReLU is another very popular activation function found in modern architecture. By never setting the gradients to zero, it allows every parameter of the model to keep learning.

### Updating weights with SGD

Training a neural network = solving an optimization problem

- **Learning Rate and Momentum Overview**:
    
    - The optimizer plays a critical role in training a neural network. Adjusting learning rate and momentum significantly impacts performance.
- **SGD (Stochastic Gradient Descent)**:
    
    - Updates model parameters to minimize the loss function.
    - Requires setting the **learning rate** (controls step size) and **momentum** (controls optimizer inertia).
    - Proper tuning of these parameters is essential for efficient training.
- **Impact of Learning Rate**:
    
    - **Optimal Learning Rate**:
        - Proper learning rate allows the optimizer to find the function's minimum in fewer steps.
        - As the optimizer nears the minimum, the step size naturally decreases.
    - **Small Learning Rate**:
        - A smaller learning rate leads to slow progress, requiring more steps to approach the minimum.
    - **High Learning Rate**:
        - A high learning rate causes instability, as the optimizer overshoots the minimum and oscillates without converging.

![[Pasted image 20240922213933.png]]

- **Momentum**:

![[Pasted image 20240922214015.png]]
![[Pasted image 20240922214030.png]]
    
- **Without Momentum**:
	- The optimizer can get stuck in local minima on non-convex functions.
- **With Momentum**:
	- Momentum (e.g., 0.9) helps the optimizer escape local minima by maintaining larger step sizes when the gradient is small.
- **Summary**:

![[Pasted image 20240922214055.png]]
    
- **Learning Rate**: Typically ranges from 10−210^{-2}10−2 to 10−410^{-4}10−4. A high rate leads to instability; a low rate slows training.
- **Momentum**: Typically ranges from 0.85 to 0.99. Helps avoid getting stuck in local minima by carrying forward momentum from previous large steps.

### Layer initialization

The initialization of the weights of a neural network has been the focus of researchers for many years. When training a network, the method used to initialize the weights has a direct impact on the final performance of the network.

As a machine learning practitioner, you should be able to experiment with different initialization strategies. In this exercise, you are creating a small neural network made of two layers and you are deciding to initialize each layer's weights with the uniform method.

```python
layer0 = nn.Linear(16, 32)
layer1 = nn.Linear(32, 64)

# Use uniform initialization for layer0 and layer1 weights
nn.init.uniform_(layer0.weight)
nn.init.uniform_(layer1.weight)

model = nn.Sequential(layer0, layer1)
```

Congratulations! The uniform initialization is one of the many different initialization strategies but they all tend to initialize weights with small values.
### Transfer Learning

Reusing a model trained on a first task for a second similar task, to accelerate the training process

### Fine-tuning

Fine-tuning = a type of transfer learning

- Smaller learning rate
- Not every layer is trained (we freeze some of them)
- Rule of thumb: freeze early layers of network and fine-tune layer closer to output layer

1. FInd a model trained on a similar task
2. Load pre-trained weights
3. Freeze (or not) some of the layers in the model
4. Train with a smaller learning rate
5. Look at the loss value and see if the learning rate needs to be adjusted

```python
for name, param in model.named_parameters():
  
    # Check if the parameters belong to the first layer
    if name == '0.weight' or name == '0.bias':
   
        # Freeze the parameters
        param.requires_grad = False
        
    # Check if the parameters belong to the second layer
    if name == '1.weight' or name == '1.bias':
      
        # Freeze the parameters
        param.requires_grad = False
```
## Evaluating and Improving Models

## Training Robust Neural Network

## Images and Convolutional Neural Network

## Sequences & Recurrent Neural Networks

## Multi-Input & Multi-Output Architectures

# Responsible AI Data Management

Responsible AI Data Management

Regulation Compliance and Licensing

Data Acquisition

Data Validation and Bias Mitigation Strategies

# LLMs in [[Python]]

The Large Language Models Landscape

Building a Transformer Architecture

Harnessing Pre-trained LLMs

Evaluating and Leveraging LLMs in the Real World

# Working with [[Llama 3]]

Understanding LLMs and Llama

Using Llama Locally

Finetuning Llama for Customer Service using Hugging Face & Bitext Dataset

Creating a Customer Service Chatbot with Llama and LangChain

# [[MLOps]] Concepts

MLOps

Design and Development

Deploying Machine Learning Into Production

Maintaining Machine Learning in Production

# [[MLOps]] Deployment and Life Cycling

MLOps in a Nutshell

Develop for Deployment

Deploy and Run

Monitor and Maintain

# [[Git]]

Making changes

Git workflows

Collaborating with GIt

# [[Software Engineering]] Principles in [[Python]]

Software Engineering & Data Science

Writing a Python Module

Utilizing Classes

Maintainability

# Testing in [[Python]]

Creating Tests with pytest

Pytest Fixtures

Basic Testing Types

Writing tests with unittest

# Monitoring [[Machine Learning]] Concepts

What is Machine Learning Monitoring

Theoretical Concepts of monitoring

Covariate Shift and Concept Drift Detection