from zhipuai import ZhipuAI

client = ZhipuAI(api_key='1c3d05f2c36b6baf3657418f04d8b2fd.jUaotVKj6jLLJtVu')
messages = (
    [
        {'role': 'user', 'content': '你好！你叫什么名字'},
    ],
)
response = client.chat.completions.create(
    model='glm-4',  # 填写需要调用的模型名称
    messages=messages,
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].message)
