# Import required libraries
import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define a function to get a response from ChatGPT
def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose the model, e.g., 'gpt-4' for GPT-4, 'gpt-3.5-turbo' for GPT-3.5
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150  # Adjust token count based on your needs
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit interface
st.title("ChatGPT with Streamlit")
st.write("Ask anything to ChatGPT:")

# Input text box for user prompt
user_input = st.text_input("Enter your question here:")

# Display ChatGPT response when there's input
if user_input:
    response = get_chatgpt_response(user_input)
    st.write("ChatGPT says:")
    st.write(response)
