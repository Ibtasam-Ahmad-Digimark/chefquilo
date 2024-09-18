import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPEN_AI_API_KEY"))

def generate_response(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful and experienced chef named Chef-GPT, and your goal is to guide users through cooking processes as if they are beginners. 
        After explaining each step in detail, ask if they understand or have any questions. Only proceed to the next step if they confirm their understanding."""})
    response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages
            )
    return response.choices[0].message.content

def generate_stream(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful and experienced chef named Chef-GPT, and your goal is to guide users through cooking processes step by step, as if they are beginners. 
        After explaining each step, ask if they understand or have any questions. Only proceed to the next step if they confirm their understanding. 
        Make sure to break complex instructions into smaller steps."""})
    stream = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=0.1,
                stream=True,
            )
    return stream