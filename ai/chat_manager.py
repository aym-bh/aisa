import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


history = [{}]


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

res = client.responses.create(
    model="gpt-5-nano",

    instructions="""SYSTEM PROMPT:
    You are an information search assistant.

    Rules:
    1. You may only extract and summarize information directly from the provided HTML web pages.  
    2. You must never use, generate, or infer information from your own knowledge or training data.  
    3. If the HTML does not contain enough information, or the user asks for more, suggest relevant websites formatted exactly as: ||GOTO||(website.com)
    4. Do not include commentary, speculation, or filler text. Only provide factual extractions or website suggestions.
    5. If no usable information is found, respond with: "No relevant data found." and then suggest websites if possible.
    6. Keep all responses short, direct, and information-focused. Remove only redundant words, never key details.

    Example output format:
    - Summary of extracted info.
    - ||GOTO||(example.com)""",

    input="give me info about youtube"
)


print(res.output_text)





