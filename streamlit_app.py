import streamlit as st
import openai
"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


# Set OpenAI API key
openai.api_key = st.secrets["OPENAI_KEY"]
# Define prompt and parameters
prompt = "Hello, can you introduce yourself?"
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 100
# Send request to the API
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
)
# Print response text
st.write(response.choices[0].text.strip())
