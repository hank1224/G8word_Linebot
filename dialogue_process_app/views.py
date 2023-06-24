from django.shortcuts import render
from django.conf import settings

import re

# 目前兩種key選擇，宣告在def裡，最終應該採用Azure的，完工後再改
import openai

# Azure OpenAI API
openai.api_base = settings.AZURE_OPENAI_ENDPOINT
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future
AZURE_OPENAI_DEPLOYMENT_NAME = settings.AZURE_OPENAI_DEPLOYMENT_NAME

def gateway(mtext):
    if str.startswith(mtext, 'http'):
        return "網址不處理"
    # 去除@符號
    regex = r"@\S+\s?"
    result = re.sub(regex, "", mtext).strip()
    if not result:
        return "處理＠後為空白訊息"
    else:
        return Azure_openAI_gpt35turbo(result)
    
def OpenAI_API_gpt35(chat_content):
    openai.api_key = settings.OPENAI_API_KEY
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens = 30,
    temperature = 1,
    messages=[
        {'role': 'system', 'content': '你是一位負責審查粗鄙言論的分析人員，負責解析收到的文本其中的惡意辱罵、不雅言詞、歧視等詞語，並提取詞語出來用python字典格式表示。如果文本不存在粗鄙言論，則回答：沒有粗鄙言論。'},
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

def Azure_openAI_gpt35turbo(chat_content):
    openai.api_key = settings.AZURE_OPENAI_KEY
    response = openai.ChatCompletion.create(
        engine= AZURE_OPENAI_DEPLOYMENT_NAME, # deployment_name
        max_tokens = 30,
        temperature = 0.2,
        messages=[
            {'role': 'system', 'content': '你是一位負責審查言論的分析人員，負責解析收到的文本，其中可能包含色情、或辱罵言語，你將會提取這些詞語出來並用python字典格式表示。如果文本不存在這些字詞或你不確定該詞語是否不適當，則回答：沒有粗鄙言論。'},
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
    print(response)
    return response['choices'][0]['message']['content']
