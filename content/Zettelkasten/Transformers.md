How to use the [pipeline()](https://huggingface.co/docs/transformers/v4.44.0/en/main_classes/pipelines#transformers.pipeline) for inference, load a pretrained model and preprocessor with an [AutoClass](https://huggingface.co/docs/transformers/en/model_doc/auto), and quickly train a model with PyTorch or TensorFlow

Before you begin, make sure you have all the necessary libraries installed:

```python
!pip install transformers datasets evaluate accelerate

!pip install torch
```

You’ll also need to install your preferred machine learning framework:

### [Pipeline](https://huggingface.co/docs/transformers/en/quicktour#pipeline)

### [AutoClass](https://huggingface.co/docs/transformers/en/quicktour#autoclass)

Under the hood, the [AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/v4.44.0/en/model_doc/auto#transformers.AutoModelForSequenceClassification) and [AutoTokenizer](https://huggingface.co/docs/transformers/v4.44.0/en/model_doc/auto#transformers.AutoTokenizer) classes work together to power the [pipeline()](https://huggingface.co/docs/transformers/v4.44.0/en/main_classes/pipelines#transformers.pipeline) you used above. An [AutoClass](https://huggingface.co/docs/transformers/en/model_doc/auto) is a shortcut that automatically retrieves the architecture of a pretrained model from its name or path. You only need to select the appropriate `AutoClass` for your task and it’s associated preprocessing class.

encoding = tokenizer("We are very happy to show you the 🤗 Transformers library.")
print(encoding)