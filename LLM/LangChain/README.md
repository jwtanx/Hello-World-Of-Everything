# Langchain

## Setting max new tokens
https://api.python.langchain.com/en/latest/llms/langchain.llms.huggingface_pipeline.HuggingFacePipeline.html
```py
from langchain.llms import HuggingFacePipeline
hf = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 10},
)
```

```py
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10
)
hf = HuggingFacePipeline(pipeline=pipe)
```

## Using GPU to run LLM
https://python.langchain.com/docs/integrations/llms/huggingface_pipelines
```py
gpu_llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    device=0,  # replace with device_map="auto" to use the accelerate library.
    pipeline_kwargs={"max_new_tokens": 10},
)

gpu_chain = prompt | gpu_llm

question = "What is electroencephalography?"

print(gpu_chain.invoke({"question": question}))
```

## Binding new stop characters
```py
gpu_llm = HuggingFacePipeline.from_model_id(
    model_id="bigscience/bloom-1b7",
    task="text-generation",
    device=0,  # -1 for CPU
    batch_size=2,  # adjust as needed based on GPU map and model size.
    model_kwargs={"temperature": 0, "max_length": 64},
)

gpu_chain = prompt | gpu_llm.bind(stop=["\n\n"])

questions = []
for i in range(4):
    questions.append({"question": f"What is the number {i} in french?"})

answers = gpu_chain.batch(questions)
for answer in answers:
    print(answer)
```

## Document loader for JSON
https://python.langchain.com/docs/modules/data_connection/document_loaders/json
```py

```