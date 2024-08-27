import litellm

## SET MAX TOKENS - via completion()
response = litellm.completion(
    model='glm-4',
    messages=[{'content': 'Hello, how are you?', 'role': 'user'}],
    api_key='1c3d05f2c36b6baf3657418f04d8b2fd.jUaotVKj6jLLJtVu',
)

print(response)
