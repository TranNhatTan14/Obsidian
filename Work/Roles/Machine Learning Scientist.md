---
URL: https://app.datacamp.com/learn/career-tracks/machine-learning-scientist-with-python
---
## Winning a Kaggle Competition in Python

Yauhen Babakhin - Kaggle competitions Grandmaster

Kaggle benefits

1. Get practicial experience on the real-world data
2. Develop portfolio projects
3. Meet a great Data Science cominity
4. Try new domain or model type
5. Keep up-to-date with the best performing methods

### Determine the problem type

### Understand the problem

![[Pasted image 20240825170840.png]]

That's correct! This competition contains a mix of various structured and unstructured data.

Great! You see that your functions work the same way that built-in `sklearn` metrics. Knowing the problem type and evaluation metric, it's time to start Data Analysis. Let's move on to the next lesson on EDA!
### EDA

Goals of EDA

- SIze of the data
- Propeties of the target variable
- Propeties of the features
- ==Generate ideas for feature engineering==

```python
# Sizr of the data
print("Train shape: ", train.shape)
print("Test shape: ", test.shape)
print(train.columns.tolist())

train.<label>.value_counts()

# Descrive the train data
train.describe()
```

### Visualize

```python
# Visualize the data
import matplotlib.pylot as plt

plt.style.use('ggplot')
```

scatterplot

### Local Validation

### Competition metric

- AUC
- F1
- Mean Log Loss
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Mean Average Precision at K (MAPK, MAP@K)

### Public vs Private leaderboard

### Training

Firstly, let's train multiple XGBoost models with different sets of hyperparameters using XGBoost's learning API. The single hyperparameter you will change is:

- `max_depth` - maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit.

```python
import xgboost as xgb

# Create DMatrix on train data
dtrain = xgb.DMatrix(data=train[['store', 'item']],
                     label=train['sales'])

# Define xgboost parameters
params = {'objective': 'reg:linear',
          'max_depth': 2,
          'verbosity': 0}

# Train xgboost model
xg_depth_2 = xgb.train(params=params, dtrain=dtrain)

from sklearn.metrics import mean_squared_error

dtrain = xgb.DMatrix(data=train[['store', 'item']])
dtest = xgb.DMatrix(data=test[['store', 'item']])

# For each of 3 trained models
for model in [xg_depth_2, xg_depth_8, xg_depth_15]:
    # Make predictions
    train_pred = model.predict(dtrain)     
    test_pred = model.predict(dtest)          
    
    # Calculate metrics
    mse_train = mean_squared_error(train['sales'], train_pred)                  
    mse_test = mean_squared_error(test['sales'], test_pred)
    print('MSE Train: {:.3f}. MSE Test: {:.3f}'.format(mse_train, mse_test))
```

### Explore overfitting XGBoost

Having trained 3 XGBoost models with different maximum depths, you will now evaluate their quality. For this purpose, you will measure the quality of each model on both the train data and the test data. As you know by now, the train data is the data models have been trained on. The test data is the next month sales data that models have never seen before.

The goal of this exercise is to determine whether any of the models trained is overfitting. To measure the quality of the models you will use Mean Squared Error (MSE). It's available in `sklearn.metrics` as `mean_squared_error()` function that takes two arguments: true values and predicted values.

`train` and `test` DataFrames together with 3 models trained (`xg_depth_2`, `xg_depth_8`, `xg_depth_15`) are available in your workspace.

### Validation

Before we start, let's discuss the motivation for local validation. Recall the plot with possible overfitting to Public test data. The problem we observe here is that we can't detect the moment when our model starts overfitting by looking only at the Public Leaderboard. That's where local validation comes into play. ==Using only train data, we want to build some kind of an internal, or local, approximation of the model's performance on a Private test data.==

The question is: how do we build such an approximation of the model's performance? The simplest way is to use a holdout set. We split all train data (in other words, all the observations we know the target variable for) into train and holdout sets.

We then build a model using only the train set and make predictions on the holdout set. So, the holdout is similar to the usual test data, but the target variable is known. It allows to compare predictions with the actual values and gives us a fair estimate of the model's performance. However, such an approach is similar to just looking at the results on the Public Leaderboard. We always use the same data for model evaluation and could potentially overfit to it. A better idea is to use cross-validation.

![[Pasted image 20240825172544.png]]

## K-fold cross-validation

Then train a model K times on all the data except for a single fold. Each time, we also measure the quality on this single fold the model has never seen before. K-fold cross-validation gives our model the opportunity to train on multiple train-test splits instead of using a single holdout set. ==This gives us a better indication of how well our model will perform on unseen data.==

Now, we need to train K models for each cross-validation split. To obtain all the splits we call the split() method of the KFold object with a train data as an argument. It returns a list of training and testing observations for each split. The observations are given as numeric indices in the train data. These indices could be used inside the loop to select training and testing folds for the corresponding cross-validation split. For pandas DataFrame it could be done using the iloc operator, for example.

![[Pasted image 20240825172715.png]]

```python
# Import KFold
from sklearn.model_selection import KFold

# Create a KFold object
kf = KFold(n_splits=3, shuffle=True, random_state=123)

# Loop through each split
fold = 0
for train_index, test_index in kf.split(train):
    # Obtain training and testing folds
    cv_train, cv_test = train.iloc[train_index], train.iloc[test_index]
    print('Fold: {}'.format(fold))
    print('CV train shape: {}'.format(cv_train.shape))
    print('Medium interest listings in CV train: {}\n'.format(sum(cv_train.interest_level == 'medium')))
    fold += 1
```

So, we see that the number of observations in each fold is almost uniform. It means that we've just splitted the train data into 3 equal folds. ==However, if we look at the number of medium-interest listings, it's varying from 162 to 175 from one fold to another.== To make them uniform among the folds, let's use Stratified K-fold!

## Stratified K-fold

Another approach for cross-validation is stratified K-fold. It is the same as usual K-fold, but creates stratified folds by a target variable. These folds are made by preserving the percentage of samples for each class of this variable. As we see on the image, each fold has the same classes distribution as in the initial data. ==It is useful when we have a classification problem with high class imbalance in the target variable or our data size is very small.==

![[Pasted image 20240825173542.png]]

Stratified K-fold is also located in sklearn's model_selection module. It has the same parameters as the usual KFold: n_splits, shuffle and random_state. The only difference is that on top of the train data, we should also pass the target variable into the split() call in order to make a stratification.

```python
# Import StratifiedKFold
from sklearn.model_selection import StratifiedKFold

# Create a StratifiedKFold object
str_kf = StratifiedKFold(n_splits=3, shuffle=True, random_state=123)

# Loop through each split
fold = 0
for train_index, test_index in str_kf.split(train, train['interest_level']):
    # Obtain training and testing folds
    cv_train, cv_test = train.iloc[train_index], train.iloc[test_index]
    print('Fold: {}'.format(fold))
    print('CV train shape: {}'.format(cv_train.shape))
    print('Medium interest listings in CV train: {}\n'.format(sum(cv_train.interest_level == 'medium')))
    fold += 1
```

As you've just noticed, you have a pretty different target variable distribution among the folds due to the random splits. It's not crucial for this particular competition, but could be an issue for the classification competitions with the highly imbalanced target variable.

To overcome this, let's implement the stratified K-fold strategy with the stratification on the target variable. `train` DataFrame is already available in your workspace.

Great! Now you see that both size and target distribution are the same among the folds. ==The general rule is to prefer Stratified K-Fold over usual K-Fold in any classification problem==. Move to the next lesson to learn about other cross-validation strategies!

## Data leakage

To start with, let's introduce a new term called 'data leakage'. ==Leakage causes a model to seem accurate until we start making predictions in a real-world environment==. We then realize that the model is of low quality and becomes absolutely useless. There are different types of data leakage. 

1. Leak in the features. It means that we're using data that will not be available in the production setting. For example, predicting sales in US dollars, while having exactly the same sales in UK pounds as a feature.  ^40291f
2. Leak in the validation strategy. It occurs when the validation strategy does not replicate the real-world situation. We will see an example in the next slide.