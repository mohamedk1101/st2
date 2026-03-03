import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit UI
st.title("Gemini AI + Streamlit Demo")
st.write("Ask anything and Gemini will respond.")

user_input = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        st.subheader("Response:")
        st.write(response.text)
