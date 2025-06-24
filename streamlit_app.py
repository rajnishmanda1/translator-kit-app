import streamlit as st
from googletrans import Translator

def translate_en_to_hi(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return translated.text

st.title("Translate from English to Hindi")

user_input = st.text_input("Enter some text:")

if user_input:
    st.write("In English: ", user_input)
    hindi_translation = translate_en_to_hi(user_input)
    st.write("In Hindi: ", hindi_translation)
