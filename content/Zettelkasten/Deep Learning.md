DL is a subset of Machine Learning

- Traditional ML relies on hand-crafted **feature engineering**
- Deep Learning enables **feature learning** from raw data

Note that deep learning does not replace machine learning; both have their strengths and weaknesses. One of the core skills of the machine learning practitioner is to determine when to use one versus the other.

### PyTorch: Deep Learning framework

```python
import torch

# For image, audio and text data
import torchvision
import torchaudio
import torchtext
```

###### Tensor

Tensors is the building block of networks in PyTorch

```python
import torch

# Load data from NumPy array
np_array = np.array(array)

tensor = torch.from_numpy(np_array)

tensor.shape
tensor.dtype

# Tensor device
tensor.device
# OUTPUT: device(type='cpu') 
```

The fundamental data structure in PyTorch is called a tensor. A tensor is essentially an array, which can support many mathematical operations, and will form a building block for our neural networks. Tensors can be created from Python lists by using the torch.tensor() class. PyTorch also supports tensor creation directly from NumPy arrays, using torch.from_numpy(). torch.tensor() will work directly on NumPy arrays too. Like NumPy arrays, tensors are multidimensional, representing a collection of elements arranged in a grid with multiple dimensions.

### Neural Network

###### Using derivatives to update model parameters

![[Pasted image 20240812182941.png]]
###### Convex and non-convex functions

Before we learn PyTorch functions that can automatically update model parameters for us, let's take a step back. Some functions, such as the one on the left, have one minimum and one only, called the "global" minimum. These functions are "convex". Some, "non-convex" functions have more than one "local" minimum. At a local minimum, the function value is lowest compared to nearby points, but points further away may be even lower. When minimizing loss functions, our goal is to find the global minimum of the non-convex function, here, when x is approximately one.

Spoiler alert: loss functions used in deep learning are not convex! To find global minima of non-convex functions, we use a mechanism called "gradient descent". PyTorch does this for us using "optimizers". The most common optimizer is stochastic gradient descent (SGD). We use optim to instantiate SGD as shown. .parameters() returns an iterable of all model parameters, which we pass to the optimizer. We use a standard learning rate, "lr", here, but this is tunable. The optimizer calculates gradients for us, and updates model parameters automatically, by calling .step(). Magic!

![[Pasted image 20240812183141.png]]

# Gradient Descent

Gradient descent is an iterative optimization algorithm for finding the minimum of an objective function (loss function of the network).

The gradient descent algorithm works in two steps that are performed continuously for a specific number of iterations.