from openai import OpenAI

# 这一行必须顶格写，前面不能有空格
client = OpenAI(
    base_url="http://127.0.0.1:8045/v1",
    api_key="sk-37b1eb56041a481e9a97483a0edfd90d"
)

# 这一行也必须顶格写
response = client.chat.completions.create(
    model="gemini-3-pro-high",
    messages=[{"role": "user", "content": "Hello! 这是一个测试。"}]
)

print(response.choices[0].message.content)