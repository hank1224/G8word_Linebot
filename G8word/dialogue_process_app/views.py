from django.shortcuts import render
from django.conf import settings

import re

import os   
import openai
openai.api_key = settings.OPENAI_API_KEY

def gateway(mtext):

    if str.startswith(mtext, 'http'):
        return "網址不處理"

    # 去除@符號
    regex = r"@\S+\s?"
    result = re.sub(regex, "", mtext).strip()
    if not result:
        return "處理＠後為空白訊息"
    else:
        return chat(result)
    

def chat(chat_content):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens = 30,
    temperature = 1,
    messages=[
        {'role': 'system', 'content': '你是一位負責審查粗鄙言論的分析人員，你將會解析收到的文本其中的惡意辱罵、不雅言詞、歧視等詞語，並提取詞語出來用python字典格式表示。如果文本不存在粗鄙言論，則回答：沒有粗鄙言論。'},
        {'role': 'user', "content": '"你幫我素完再幫我打手槍"'},
        {'role': 'assistant', 'content': '{"幫我素", "打手槍"}'},
        {'role': 'user', "content": '"要先把楊芷昀叫進來"'},
        {'role': 'assistant', 'content': '沒有粗鄙言論。'},
        {'role': 'user', "content": '"他媽的祖墳燒起來了"'},
        {'role': 'assistant', 'content': '{"他媽的", "祖墳"}'},
        {'role': 'user', "content": '"你直播吃ㄐㄐ比較快"'},
        {'role': 'assistant', 'content': '{"ㄐㄐ"}'},
        {'role': 'user', 'content': '"' + chat_content + '"'}
    ]
    )

    return completion.choices[0].message.content
