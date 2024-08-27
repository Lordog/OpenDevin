# http://dify.wangyulong.io:3000/app/9f825857-942c-410f-941f-cf10ae7f9b5b/develop
import re

import requests


def gpt_completion_helper(prompt, conversation_id=''):
    url = 'http://dify.wangyulong.io:5001/v1/chat-messages'
    api_key = 'app-HJYTmx932Mk1ZC348g7VoHkG'  #'app-5OocbNmeFzKruQAp1euOp99a'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    request = {
        'inputs': {},
        'query': f'{prompt}',
        'response_mode': 'blocking',
        'conversation_id': conversation_id,
        'user': 'yuantx',
    }
    response = requests.post(url, headers=headers, json=request)
    s = response.content.decode('utf-8')
    if conversation_id == '':
        conversation_id = extract_conversation_id(s)
    content = extract_resp(s)
    return content, conversation_id


def extract_resp(s):
    pattern = r'"answer": "(.*?)"'
    matches = re.findall(pattern, s)
    content = ''
    for match in matches:
        content += match
    return content


def extract_conversation_id(s):
    pattern_conversation = r'"conversation_id": "(.*?)"'
    matches_conversation = re.findall(pattern_conversation, s)
    conversation_id = matches_conversation[0]
    return conversation_id


"""
def gpt_completion(model, messages):
    conversation_id = ''
    query = messages[-1]
    for query in messages: # 倒序调用
        if query['role'] == 'user':
            conversation_id = gpt_completion_helper(query['content'], conversation_id)
        elif query['role'] == 'assistant':
            return



prompt = "hello, print '20240630' please."
content, conversation_id = gpt_completion_helper(prompt)
print(content)
prompt = "hello, print '15:22', and attach the last sentence i ask you to print."
content, conversation_id = gpt_completion_helper(prompt, conversation_id)
print(content)
"""

"""
{"event": "message",
"task_id": "97bcf1a2-6795-4c2c-aeca-5ef993096d59",
"id": "0599ef72-beae-428a-b700-c1b7be2086f0",
"message_id": "0599ef72-beae-428a-b700-c1b7be2086f0",
"conversation_id": "da541854-2899-40a0-9bb9-fda3e25d42e7",
"mode": "advanced-chat",
"answer": "Your configuration is correct",
"metadata": {"usage": {"prompt_tokens": 18, "prompt_unit_price": "0.03", "prompt_price_unit": "0.001", "prompt_price": "0.0005400", "completion_tokens": 11, "completion_unit_price": "0.06", "completion_price_unit": "0.001", "completion_price": "0.0006600", "total_tokens": 29, "total_price": "0.0012000", "currency": "USD", "latency": 0.916656875051558}}, "created_at": 1717573770}

"""
