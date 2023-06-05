from django.shortcuts import render
from django.conf import settings

import os   
import openai
openai.api_key = settings.OPENAI_API_KEY

def chat(chat_content):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens = 80,
    temperature = 1,
    messages=[
        {"role": "system", "content": "請將以下句子翻譯成英文："},
        {"role": "user", "content": chat_content}
    ]
    )

    return completion.choices[0].message.content
