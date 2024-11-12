import os
import openai
import streamlit as st

# Load the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your function and app
def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI setup
st.title("ChatGPT with Streamlit")
st.write("Ask anything to ChatGPT:")

user_input = st.text_input("Enter your question here:")

if user_input:
    response = get_chatgpt_response(user_input)
    st.write("ChatGPT says:")
    st.write(response)
