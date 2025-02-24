# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv
from IPython.display import display, Markdown

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_gemini_api_key():
    load_env()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    return gemini_api_key

def get_activeloop_api_key():
    load_env()
    activeloop_api_key = os.getenv("ACTIVELOOP_API_KEY")
    return activeloop_api_key

def get_cohere_api_key():
    load_env()
    cohere_api_key = os.getenv("COHERE_API_KEY")
    return cohere_api_key

def get_eleven_api_key():
    load_env()
    eleven_api_key = os.getenv("ELEVEN_API_KEY")
    return eleven_api_key

def get_langchain_api_key():
    load_env()
    langchain_endpoint = os.getenv("LANGCHAIN_API_KEY")
    return langchain_endpoint

def get_langchain_tracing_v2():
    load_env()
    langchain_tracing_v2 = os.getenv("LANGCHAIN_TRACING_V2")
    return langchain_tracing_v2

def get_langchain_endpoint():
    load_env()
    langchain_endpoint = os.getenv("LANGCHAIN_ENDPOINT")
    return langchain_endpoint

def get_langchain_project():
    load_env()
    langchain_project = os.getenv("LANGCHAIN_PROJECT")
    return langchain_project

def print_response(text):
    display(Markdown(text))