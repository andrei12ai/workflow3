import os
import openai
import streamlit as st

# Set your API key (from environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to get a response from ChatGPT using the latest API
def get_chatgpt_response(prompt):
    try:
        # Ensure the latest API syntax is used
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        # Access the response content
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app setup
st.title("ChatGPT with Streamlit")
st.write("Ask anything to ChatGPT:")

# Input text box for user prompt
user_input = st.text_input("Enter your question here:")

# Display ChatGPT response when there's input
if user_input:
    response = get_chatgpt_response(user_input)
    st.write("ChatGPT says:")
    st.write(response)
