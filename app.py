import os

import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

prompt_template = """

"""

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response

prompt = st.text_input("Prompt")
if st.button("Generate"):
    reply = generate_content(prompt)
    st.write(reply)

#response = model.generate_content("Write a story about a magic backpack")
#print(response)