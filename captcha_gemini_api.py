from google import genai

client = genai.Client(api_key="API KEY HERE")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="how to use this very api to solve an easy numeric captcha "
)
print(response.text)