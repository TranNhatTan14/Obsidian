- ==Understand development steps==, from evaluation, through prompting, self-reflection, and fine-tuning, to improve your model’s reliability and accuracy.
- Learn how ==memory tuning can increase your model performance== by embedding facts into your model to reduce hallucination.
- Use the Llama 3-8b model to build an LLM application that ==converts text to SQL with a custom schema.==

## What you’ll learn in this course

Join our new short course, Improving Accuracy of LLM Applications with Lamini and Meta. Learn from Sharon Zhou, Co-founder & CEO of Lamini, and Amit Sangani, Senior Director of Partner Engineering, Meta.

Many developers have ==experienced frustration with inconsistent results when working with LLM applications==. This course offers a ==systematic approach== to enhance the accuracy and reliability of your LLM applications.

You will ==build an SQL agent==, add evaluation metrics to measure performance, and ==use prompt engineering and self-reflection to make the model perform better==. Finally, you will fine-tune the model with techniques like ==LoRA and memory tuning== that embeds facts in model weights to reduce hallucinations.

In this course, you’ll ==use Llama’s family of open-source models.==

What you’ll do: 

- ==Build a text to SQL agent== and simulate situations where it hallucinates to begin the evaluation process.
- Build an ==evaluation framework to systematically measure performance==, including criteria for good evaluations, best practices, and how to develop an evaluation score.
- Learn how ==instruction fine-tuning enhances pre-trained LLMs== to follow instructions, and how memory fine-tuning embeds facts to reduce hallucinations. 
- Break fine-tuning myths and see how ==Performance-Efficient Fine-tuning (PEFT)== techniques like ==Low-Rank Adaptation(LoRA)== reduce training time by 100x and ==Mixture of Memory Experts (MoME)== reduces it even further. 
- Go through an iterative process of generating training data and fine-tuning, learning practical tips such as adding examples, generating variations, and filtering generated data to increase model accuracy.

---

What is schema?

---

Learn a framework for a set of development steps

Instruction Fine-tuning

How to deal with hallucinations

- Prompt Engineering -> 25%
- Self-reflection -> 25-40%
- RAG -> 50%
- Instruction Fine-tuning -> 40-60%
- Memory Tuning -> 95%

How can fine-tuning reduce hallucination?

- Embed facts into the model
- Howerver, instruction fine-tuning isn't the tool to remove hallucinations (and can be costly)
- Memory Tuning (invented by Lamini) allows the model to recall a lot of facts precisely

![[Pasted image 20240817015132.png]]

Iteration, Iteration, Iteration

Iteration 3x on eval, data generation, & fine-tuning (using Memory Tuning)

![[Pasted image 20240817015613.png]]

Create the function to generate prompt

```python
def make_llama_3_prompt(user, system=""):
    system_prompt = ""
    if system != "":
        system_prompt = (
            f"<|start_header_id|>system<|end_header_id|>\n\n{system}"
            f"<|eot_id|>"
        )
    prompt = (f"<|begin_of_text|>{system_prompt}"
              f"<|start_header_id|>user<|end_header_id|>\n\n"
              f"{user}"
              f"<|eot_id|>"
              f"<|start_header_id|>assistant<|end_header_id|>\n\n"
         )
    return prompt

system_prompt = user_prompt = "You are a helpful assistant."
user_prompt = "Please write a birthday card for my good friend Andrew"
prompt3 = make_llama_3_prompt(user_prompt, system_prompt)
print(prompt3)
```

1. Start with prompt engineering: give example of input data, structured output