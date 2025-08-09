from google import genai
import os
from IPython.display import display, Markdown, Latex

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="AI是如何工作的(請使用繁體中文回答)?"
)

display(Markdown(response.text))