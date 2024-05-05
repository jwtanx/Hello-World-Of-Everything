import os
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import (
    StreamingStdOutCallbackHandler,)  # for streaming resposne
# from langchain.llms import OpenAI

# Make sure the model path is correct for your system!
model_path = "LLM/models/llm/gguf/llama-2-7b-chat.Q4_K_M.gguf"  # <-------- enter your model path here
# model_path = "LLM/models/llm/gguf/mistral-7b-v0.1.Q4_K_M.gguf"  # <-------- enter your model path here

template = """Question: {question}

Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Uncomment the code below if you want to run inference on GPU
# n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.
# n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
# llm = LlamaCpp(model_path=model_path,
#                n_gpu_layers=n_gpu_layers,
#                n_batch=n_batch,
#                callback_manager=callback_manager,
#                verbose=True,
#                temperature=1)

llm = LlamaCpp(model_path=model_path,
               callback_manager=callback_manager,
               verbose=True)

llm_chain = LLMChain(prompt=prompt, llm=llm)
os.system("clear")

while True:
  question = input("Prompt [ENTER TO QUIT]: ")
  if question.strip() == "":
    quit()
  print(llm_chain.run(question))