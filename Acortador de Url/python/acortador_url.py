import pyshorteners
import streamlit as st

def shortened_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

# Creando la Web con Streamlit

st.set_page_config(page_title="Url Shortener", page_icon="👍", layout="centered")
st.image("https://i.pinimg.com/originals/84/55/d7/8455d7d01d2ac76fb8402daaa7b24612.jpg")
st.title("URL SHORTENER :D")
url = st.text_input("Enter the url: ")
if st.button("Generate the url: "):
    st.write("Url shortened: ", shortened_url(url))