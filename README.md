# politik-nlp
This repo is for exploring **language datasets and models on German politics**. Built as part of Data Science Retreat (DSR) Berlin.

Python version: `3.10.13`

Install requirements:
```
pip install -r requirements.txt
```

## Contents
So far, this repo includes the following:
1. `get_bundestag_protocols.ipynb`: Pulling parliament protocols via the Bundestag API.
2. `get_party_manifestos.ipynb`: Extracting the **raw text from party manifestos** ("Parteiprogramme) in PDF format.
3. `get_wahlomat_responses.ipynb`: Extracting the **statements and responses from the "Wahl-O-Mat" tool** for voter decision-making. Potentially useful for generating prompts and for a "ground truth" response of a party.
4. `rag.ipynb`: A basic exploration of **retrieval-augmented generation (RAG)** within this context.