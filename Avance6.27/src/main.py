import os
import pandas as pd
from tqdm import tqdm
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain, LLMChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
import warnings
from rich import print
import torch
from os.path import dirname, abspath

# Suppress all warnings
warnings.filterwarnings("ignore")

def extract_keywords_from_query(query):
    keyword_extraction_template = (
        """You're a freight inspector, your job is to identify what are the most relevant keywords to identify the proper HS Code later:
        Text: {query}
        Respond ONLY with the keywords (ENGLISH or Spanish depending on your input) you think are most relevant to identify the content of that container,
        as a whole sentence, NO OTHER TEXT"""
    )
    keyword_prompt = PromptTemplate(template=keyword_extraction_template, input_variables=["query"])
    keyword_chain = LLMChain(llm=llm_model, prompt=keyword_prompt)
    keywords_response = keyword_chain.run({"query": query})
    return keywords_response

def translate_query(query):
    keyword_extraction_template = (
        """You're a Spanish-to-English translator with relevant experience in the freight business. Your job is to translate the query to English:
        Text: {query}
        Respond ONLY with the translation in English, as a whole sentence, NO OTHER TEXT or polite introduction"""
    )
    keyword_prompt = PromptTemplate(template=keyword_extraction_template, input_variables=["query"])
    keyword_chain = LLMChain(llm=llm_model, prompt=keyword_prompt)
    keywords_response = keyword_chain.run({"query": query})
    return keywords_response

def process_with_AI(query):
    keywords_from_query = extract_keywords_from_query(query)
    translated_to_english = translate_query(keywords_from_query)
    return translated_to_english

if __name__ == "__main__":
    print(f"CUDA Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Device Name: {torch.cuda.get_device_name(0)}")
        device = torch.device("cuda")

    # Set hyperparameters
    index_test_name = 'Alibaba'
    LLM_model = 'Llama3.1'
    temperature_parameter = 0
    retriever_matches_k = 3
    embed_model = 'Alibaba-NLP/gte-large-en-v1.5'

    script_dir = abspath(dirname(__file__))    # Set current path -> .py file
    persistent_dir = os.path.abspath(os.path.join(script_dir, '..', 'index', index_test_name))

    model_name = embed_model
    model_kwargs = {'device': 'cuda:0', 'trust_remote_code': True}
    encode_kwargs = {'normalize_embeddings': True}

    embedding_model_via_Transformers_class = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    llm_model = OllamaLLM(model=LLM_model,
                          temperature=temperature_parameter,
                          num_thread=8)

    vectorstore = Chroma(persist_directory=persistent_dir, embedding_function=embedding_model_via_Transformers_class)
    retriever = vectorstore.as_retriever(search_kwargs={"k": retriever_matches_k})

    template = """ You must strictly respond with the HS code that matches the information contained in the 'source' 
    field of the metadata from the source_documents provided. You are not allowed to respond with any HS code from your own knowledge. 
    Do not invent or guess. Only respond with one HS code from the provided metadata that has the highest relevance score from the retriever, 
    and it must be from the 'source' field.

    For example, if the source document mentions 'Potato starch' with 'source': '1108.13', your answer must be '1108.13'.

    Avoid responding with any other text. Respond only with 1 HS code, the one with better score from the retriever.

    If for some reason, you can't find any match, suggest 3 possible matches with their corresponnding descriptions.

    context:
    {summaries}

    Question:
    {question}
    """

    context = """As a logistics shipping arrival inspector, your primary responsibility is to inspect incoming shipments and accurately classify goods 
    using the Harmonized System (HS) code based on the descriptions provided in the shipping manifests. You will thoroughly review the manifest details, 
    including product type, material composition, function, and intended use, to determine the correct HS code. 

    Your task is to:
    Carefully read and analyze the product descriptions from the manifest.
    Identify key characteristics of the goods, such as 
    type (e.g., electronics, textiles, machinery), 
    material (e.g., plastic, metal, organic), 
    and usage (e.g., household, industrial, medical).
    Use your knowledge of the HS code classification system to assign the most appropriate HS code for each product based on its description.
    Ensure compliance with international trade regulations by selecting precise codes to avoid delays or penalties.
    Remember to be thorough and accurate in your classification, as this impacts customs processing, tariffs, and legal requirements."""

    llm_chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm_model,
        chain_type='stuff',
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={
            "prompt": PromptTemplate(
                template=template,
                input_variables=["question", "summaries"],
            ),
        },
    )

    # Start interactive console
    print("Type your query to retrieve an HS Code (type 'exit' to quit):")
    while True:
        query = input("Enter query: ")
        if query.lower() == "exit":
            print("Exiting console.")
            break

        # Run prediction
        processed_query = process_with_AI(query)
        result = llm_chain({"question": processed_query, "summaries": context})
        print(f"[bold yellow]The requested item's description CLEANED to search HTS code is:[/bold yellow]\n{processed_query}")
        print(f"[bold green]The response of the LLM is:[/bold green]\n{result['answer']}")
