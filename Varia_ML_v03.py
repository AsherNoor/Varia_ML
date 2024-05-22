# Varia ML : A local GPT for that old PC.
# Platform: Llama Index + Ollama
# Model/LLM : TinyLlama
# Created by : Ash Noor (www.AshNoor.me)
# VERSION 003: Addeded Streaming response and the Varia variable.

"""
----------------------
Quick Notes for set up (Windows)
----------------------
- Download and Install Ollama ( https://ollama.com/ ).
- (optional) create a python virtual environment.
- Activate said environment.

- Install the following Python Libraries:
pip install ollama, llama-index-llms-ollama

- Use ollama to pull the "tinyLlama" model.
ollama pull tinyllama

IMPORTANT:
Make sure to Run the Ollama.exe on your local machine.

Now, you should be able to import and run this code.
Enjoy.
"""

# Activate enviornment: varia_ml\Scripts\activate
# REMEMBER: Run Ollama in your python environment.




# Imports : General
import os # <-- used for the command to clean the screen.

# Imports : Llama Index
from llama_index.llms.ollama import Ollama  # <-- this has a "streaming" feature


# initialize the LLM
my_llm = 'tinyllama' # Model name to use.
llm=Ollama(model=my_llm)

# -- On Screen Name -- #
ai_name = "Varia"

# The Ask Function : query
def ask(query):
    # -- The Query Prompt -- #
    query = f'{query} -- answer in 15 words or fewer', # <-- our prompt injection

    # -- The Streamed Response -- #
    response = llm.stream_complete(f'{query}')
    print(f"\n{ai_name} ~ ", end="")
    for r in response:
        print(r.delta, end="")

    return response
# -- end of Ask function



# Clear Screen
os.system("cls" if os.name == "nt" else "clear")

# -- The While True prompt loop -- #
while True:
    query = input(f'\n\n{ai_name} : How can I help you? \n')

    # Clear Screen
    os.system("cls" if os.name == "nt" else "clear")

    # Answer : Queried by the agent.
    answer = ask(query)

# End of The While True loop









