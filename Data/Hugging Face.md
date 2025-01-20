---
tags:
  - Framework
---

https://huggingface.co

###### [Hugging Face Chat](https://huggingface.co/chat)

Test new chatbot model

https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard

https://huggingface.co/welcome

### Build the `chatbot` pipeline using 🤗 Transformers Library

```python
from transformers.utils import logging
logging.set_verbosity_error()

from transformers import Conversation

chatbot = pipeline(task="conversational",
                   model="./models/facebook/blenderbot-400M-distill")
user_message = """
What are some fun activities I can do in the winter?
"""

conversation = Conversation(user_message)
conversation = chatbot(conversation)

# Include prior conversations
conversation.add_message(
    {"role": "user",
     "content": """
What else do you recommend?
"""
    })
```

### Example of Translation and Summarization

```python
from transformers.utils import logging
logging.set_verbosity_error()

import torch

# Translation
translator = pipeline(task="translation",
                      model="./models/facebook/nllb-200-distilled-600M",
                      torch_dtype=torch.bfloat16) 
text = """\
My puppy is adorable, \
Your kitten is cute.
Her panda is friendly.
His llama is thoughtful. \
We all have nice pets!"""

text_translated = translator(text,
                             src_lang="eng_Latn",
                             tgt_lang="fra_Latn")

# Free up some memory before continuing
# In order to have enough free memory to run the rest of the code, please run the following to free up memory on the machine.

import gc

del translator

gc.collect()

# Summary
summarizer = pipeline(task="summarization",
                      model="./models/facebook/bart-large-cnn",
                      torch_dtype=torch.bfloat16)
text = """Paris is the capital and most populous city of France, with
          an estimated population of 2,175,601 residents as of 2018,
          in an area of more than 105 square kilometres (41 square
          miles). The City of Paris is the centre and seat of
          government of the region and province of Île-de-France, or
          Paris Region, which has an estimated population of
          12,174,880, or about 18 percent of the population of France
          as of 2017."""

summary = summarizer(text,
                     min_length=10,
                     max_length=100)
```

### Deploy ML models on Hugging Face Hub using Gradio

Host a model as an API on Hugging Face Hub and call that API through a command.

If you want to deploy a larger model or what if I don't want to deploy that model locally on my local computer

1. Work locally
2. Export that app directly into the created Hugging Face Spaces

Alternatively, you can git clone the space locally and do everything through git

Use space as an external API

Host a private model

Hugging Face ecosystem feature: GPU Zero space

```python
from transformers.utils import logging
logging.set_verbosity_error()

import warnings
warnings.filterwarnings("ignore", 
                        message="Using the model-agnostic default `max_length`")

import os
import gradio as gr
from transformers import pipeline

pipe = pipeline("image-to-text",
                model="./models/Salesforce/blip-image-captioning-base")

def launch(input):
    out = pipe(input)
    return out[0]['generated_text']

iface = gr.Interface(launch,
                     inputs=gr.Image(type='pil'),
                     outputs="text")

iface.launch(share=True, 
             server_port=int(os.environ['PORT1']))

iface.close()
```

Go to [Hugging Face Spaces](https://huggingface.co/spaces)

```Python
from gradio_client import Client

client = Client("eddyS/blip-image-captioning-2",
                hf_token=hf_access_token
               )
result = client.predict(
        "kittens.jpg",
        api_name="/predict"
)
print(result)
# client = Client("abidlabs/whisper-large-v2", 
)
```

https://huggingface.co/zero-gpu-explorers