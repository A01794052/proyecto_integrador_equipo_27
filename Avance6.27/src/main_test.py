import os
import pandas as pd
#import dotenv
from tqdm import tqdm
from langchain_community.vectorstores import Chroma


## To run Hugging Face OpenSource models
# Needs to manually install Visual C++ Tools from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
#from InstructorEmbedding import INSTRUCTOR
#from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import Chroma
#from langchain.embeddings import HuggingFaceEmbeddings  #Deprecated
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoModel

#For some reason, "context" cant be used as input variable, it should be named as "summaries"
from langchain.chains import RetrievalQAWithSourcesChain, LLMChain
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
import warnings
from rich import print
import torch
import torch.nn as nn
from os.path import dirname, abspath
# Suppress all warnings
warnings.filterwarnings("ignore")


def extract_keywords_from_query(query):
    # Step 1: Define the keyword extraction prompt and LLMChain
    # Prompt to ask the LLM to extract relevant keywords
    keyword_extraction_template = (
        """You're a freight inspector, your job is to identify what are the most relevant keywords to identify the proper HS Code later:
        Text: {query}
        Respond ONLY with the keywords (ENGLISH or Spanish depending on your input) you think are most relevant to identify the content of that container,
        as a whole sentence, NO OTHER TEXT"""
    )

    keyword_prompt = PromptTemplate(template=keyword_extraction_template, input_variables=["query"])

    # Initialize LLM for keyword extraction
    keyword_chain = LLMChain(llm=llm_model, prompt=keyword_prompt)

    # Extract keywords by running the LLM chain
    keywords_response = keyword_chain.run({"query": query})
    return keywords_response

def translate_query(query):
    # Step 1: Define the keyword extraction prompt and LLMChain
    # Prompt to ask the LLM to extract relevant keywords
    keyword_extraction_template = (
        """You're a spanish to english translator with relevant experience on the freught business, your job is to translate the query to english:
        Text: {query}
        Respond ONLY with the trasnaltion in english, as a whole sentence, NO OTHER TEXT or polite introduction"""
    )

    keyword_prompt = PromptTemplate(template=keyword_extraction_template, input_variables=["query"])

    # Initialize LLM for keyword extraction
    keyword_chain = LLMChain(llm=llm_model, prompt=keyword_prompt)

    # Extract keywords by running the LLM chain
    keywords_response = keyword_chain.run({"query": query})
    return keywords_response

def process_with_AI(query):
    keywords_from_query = extract_keywords_from_query(query)
    #print(keywords_from_query)
    translated_to_english = translate_query(keywords_from_query)
    #print(translate_to_english)
    return translated_to_english




if __name__ == "__main__":
    # Check if CUDA is available
    print(f"CUDA Available: {torch.cuda.is_available()}")

    # Print CUDA device name
    if torch.cuda.is_available():
        print(f"Device Name: {torch.cuda.get_device_name(0)}")
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


    #Set hyperparaemters    
    index_test_name = 'Alibaba'
    LLM_model = 'Llama3.1'
    temperature_parameter=0
    retriever_matches_k = 3
    embed_model = 'Alibaba-NLP/gte-large-en-v1.5'

    ##Input method
    #-> File mode:
    #output_file_path = f'../Predicciones_{LLM_model}_{index_test_name}_k{retriever_matches_k}_Temp{temperature_parameter}.csv'
    #df = pd.read_csv('../validation_dataset/Validation data reviewed.csv', encoding='utf-8', dtype=str)

    #-> Manual input mode
    #query = "FREIGHT PREPAIDBEER IN BOTTLES  BEER IN CANS AND PROMOTIONALMATERIALHS CODE  220300  701328THIS MASTER BILL COVERS NON AUTOMATED NVOCCHOUSE BILL  IBC0752276"
    #query = "kilogram organic coffee bean certified fairtrade utz roasted usa global distribution"
    #query = "CARTULINA NEGRA BOB 170 GRS HS CODE 480258 CARTULINA BLANCA BOB 210 GRS HS CODE 480258"
    query = "said contain plastic drum h msku dry shipper seal pw plastic drum h stowed methyl butyric acid corrosive liqu"
    #query = "CARGO IS STOWED IN A REFRIGERATED CONTAINER SETAT THE SHIPPER S REQUESTED CARRYING TEMPERATUREOF  22 DEGREES CELSIUSFREIGHT COLLECTFROZEN BREAD AND PASTRIES HS CODE 190590FROZEN BREAD AND PASTRIES HS CODE 190590FROZEN BREAD AND PASTRIES HS CODE 19059"
    #query = "HERRAJES PARA MUEBLES HS CODE 83024200 EMAIL G.GIACOMO RAGO-GROUP.COM"


    #script_dir =  os.getcwd()     #Set current path -> Jupyter
    script_dir = abspath(dirname(__file__))    #Set current path -> .py file
    
    persistent_dir = os.path.abspath(os.path.join(script_dir,'..' ,'index', index_test_name))

    model = AutoModel.from_pretrained(embed_model, trust_remote_code=True) 
    model_name = embed_model
    model_kwargs = {'device': 'cuda:0', 'trust_remote_code':True}
    encode_kwargs = {'normalize_embeddings': True}

    embedding_model_via_Transformers_class = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )


    ##### RAG template
    # loading the Llama3 model from local
    llm_model = OllamaLLM(model=LLM_model,
                    temperature=temperature_parameter,
                    num_thread=8,
                    )
    # loading the vectorstore
    vectorstore = Chroma(persist_directory=persistent_dir, embedding_function=embedding_model_via_Transformers_class)
    # casting  the vectorstore as the retriever, taking the best k similarities
    retriever = vectorstore.as_retriever(search_kwargs={"k":retriever_matches_k})

    ###########################################################################################################################################################
    template = """ You must strictly respond with the HS code that matches the information contained in the 'source' 
    field of the metadata from the source_documents provided. You are not allowed to respond with any HS code from your own knowledge. 
    Do not invent or guess. Only respond with one HS code from the provided metadata that has the highest relevance score from the retriever, 
    and it must be from the 'source' field.

    For example, if the source document mentions 'Potato starch' with 'source': '1108.13', your answer must be '1108.13'.

    Avoid responding with any other text.Respond only with 1 HS code, the one with better score from the retriever.

    context:
    {summaries}

    Question:
    {question}
    """
    ###########################################################################################################################################################
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
    ###########################################################################################################################################################

    # Define the LL; type (Q&A type)
    llm_chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm_model,
        chain_type='stuff',
        retriever=retriever,
        return_source_documents=True,  # To get both the answer and source docs
        chain_type_kwargs={
                "prompt": PromptTemplate(
                    template=template,
                    #For some reason, "context" cant be used as input variable, it should be named as "summaries"
                    input_variables=["question", "summaries"],
                ),
            },
    )

    ## Run prediction
    result = llm_chain({"question": process_with_AI(query), "summaries": context})
    print(f"[bold yellow]The requested item's description CLEANED to search HTS code is:[/bold yellow]\n{process_with_AI(query)}")
    print(f"[bold green]The response of the LLM is:[/bold green]\n{result['answer']}")  