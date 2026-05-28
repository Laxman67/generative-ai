from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

# OpenAI model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Streamlit UI
st.header("Research Tool")

user_input = st.text_input("Enter your Prompt:")

if st.button("Summarize"):

    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else:
        response = model.invoke(user_input)

        st.write(response.content)
