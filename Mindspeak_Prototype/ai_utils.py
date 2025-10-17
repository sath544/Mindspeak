# ai_utils.py
import os
import openai
import requests

openai.api_key = os.getenv('OPENAI_API_KEY')

HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY','')}"}  # Optional

SYSTEM_CHAT = "You are Mindspeak — friendly, empathetic, and helpful."

def call_huggingface(prompt):
    try:
        payload = {"inputs": prompt}
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload)
        if response.status_code == 200:
            output = response.json()
            return output[0]['generated_text'] if isinstance(output, list) else str(output)
        else:
            return f"(HF error {response.status_code})"
    except Exception as e:
        return f"(HF exception: {e})"

def chat_with_ai(user_message: str) -> str:
    if openai.api_key:
        try:
            messages = [
                {"role": "system", "content": SYSTEM_CHAT},
                {"role": "user", "content": user_message}
            ]
            resp = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages,
                max_tokens=300
            )
            return resp['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"(OpenAI error: {e}) — fallback to Hugging Face\n" + call_huggingface(user_message)
    else:
        return call_huggingface(user_message)

def correct_english(text: str) -> str:
    prompt = f"You are an English teacher. Improve grammar and clarity:\n{text}"
    if openai.api_key:
        try:
            resp = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{"role":"user","content":prompt}],
                max_tokens=300
            )
            return resp['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"(OpenAI error: {e}) — fallback to Hugging Face\n" + call_huggingface(prompt)
    else:
        return call_huggingface(prompt)

def stress_response(user_text: str) -> str:
    prompt = (
        "You're a calm supportive companion. "
        "User shares stress or low mood. "
        "Offer empathy + 3-step breathing or journaling prompt + motivating sentence:\n" + user_text
    )
    if openai.api_key:
        try:
            resp = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{"role":"user","content":prompt}],
                max_tokens=250
            )
            return resp['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"(OpenAI error: {e}) — fallback to Hugging Face\n" + call_huggingface(prompt)
    else:
        return call_huggingface(prompt)
# AI utilities for Mindspeak
