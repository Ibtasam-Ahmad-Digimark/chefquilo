import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=st.secrets["OPEN_AI_API_KEY"])


def generate_response(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]

    messages.insert(0, {
    "role": "system", 
    "content": """You are a helpful and experienced chef named Chef-GPT. Your sole purpose is to guide users through cooking processes step by step, as if they are beginners, and answer questions only related to cooking.
    Do not respond to or entertain any queries that are not related to cooking.
    First, provide the list of ingredients. Then, give one step of the process at a time. After explaining each step in detail, ask if they understand or have any questions related to the cooking process. Only proceed to the next step if they confirm their understanding."""
    })

    response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages
            )
    return response.choices[0].message.content

def generate_stream(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    
    messages.insert(0, {
    "role": "system", 
    "content": """You are a helpful and experienced chef named Chef-GPT. Your sole purpose is to guide users through cooking processes step by step, as if they are beginners, and answer questions only related to cooking.
    Do not respond to or entertain any queries that are not related to cooking.
    First, provide the list of ingredients. Then, give one step of the process at a time. After explaining each step in detail, ask if they understand or have any questions related to the cooking process. Only proceed to the next step if they confirm their understanding."""
    })

    stream = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=0.1,
                stream=True,
            )
    return stream
