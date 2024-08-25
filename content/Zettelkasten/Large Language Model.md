---
links:
  - "[[Artificial Intelligence]]"
---
- Find and filter open source models on Hugging Face Hub based on task, rankings, and memory requirements.
- Using the transformers library to perform text, audio, image, and multimodal tasks.
- Easily share your AI apps with a user-friendly interface or via API and run them on the cloud using Gradio and Hugging Face Spaces.

The availability of models and their weights for anyone to download enables a broader range of developers to innovate and create.

In this course, you’ll select open source models from Hugging Face Hub to perform NLP, audio, image and multimodal tasks using the Hugging Face transformers library. Easily package your code into a user-friendly app that you can run on the cloud using Gradio and Hugging Face Spaces.

You will:

- Use the transformers library to turn a small language model into a chatbot capable of multi-turn conversations to answer follow-up questions.
- Translate between languages, summarize documents, and measure the similarity between two pieces of text, which can be used for search and retrieval.
- Convert audio to text with Automatic Speech Recognition (ASR), and convert text to audio using Text to Speech (TTS).
- Perform zero-shot audio classification, to classify audio without fine-tuning the model.
- Generate an audio narration describing an image by combining object detection and text-to-speech models.  
- Identify objects or regions in an image by prompting a zero-shot image segmentation model with points to identify the object that you want to select.
- Implement visual question answering, image search, image captioning and other multimodal tasks.
- Share your AI app using Gradio and Hugging Face Spaces to run your applications in a user-friendly interface on the cloud or as an API. 

The course will provide you with the building blocks that you can combine into a pipeline to build your AI-enabled applications!

### Selecting models

Grab "component" 

Voice assistant

Hugging Face Hub is an open platform that hosts models, datasets, and machine learning demos that are called Hugging Face Space

###### Seach

Identifying what task you're working on

I want to do "Automatic Speech Recognition" to "transcribe speech in French"

Model card

- Model architecture
- How it was trained
- What limitation it has
- Model checkpoint refers to the save model, including the pre-trained weights and all the necessary configurations.

Rule of thumb that I use to estimate how much memory I will need for a model

Go to FIle and versions - Find "pytorch_model.bin"

Load model from Transformer library with both use a pipeline as a high-level helper or load model directly

```python
def factorial(n):
    """Return the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
print(factorial(5))  # Output: 120
```