import streamlit as st 


import google.generativeai as genai

genai.configure(api_key="AIzaSyD0AJ42-kPJkv_dueFv8wS2xoXpOvnOtmU")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# text = "what is ml"
st.title("sivaraj" )
text = st.text_input("enter your prompt")
# st.write("The current movie title is", text)
if st.button("2 mark"):
    response = chat.send_message(f"{text} answer the question short as possible and easy understandable way ")
    res = response.text
    st.write("The current movie title is", res)

if st.button("16 mark"):
    response = chat.send_message(f"{text} answer the question briefly for 16 mark question ")
    res = response.text
    st.write("The current movie title is", res)