import streamlit as st
import requests
st.header('Guess age from name')
name = st.text_input('your name = ' )
if name :
    r=requests.get(f'https://api.agify.io/?name={name}').json()
    st.write(f'Your age is predicted to be {r["age"]}')
