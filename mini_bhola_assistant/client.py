# from openai import OpenAI

# client = OpenAI()



import google.generativeai as genai

genai.configure(api_key="AIzaSyCuCDbiaVbSgIOYs0KZNCwJ8BcGg-0S_Sg")

model = genai.GenerativeModel(model_name="gemini-pro")

response = model.generate_content("What's the latest news today?")
print(response.text)
