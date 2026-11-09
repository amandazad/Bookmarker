import streamlit as st

from ui_dashboard import open_dashboard

def verify_login(username: str, password: str):
    if username and password:
        st.success("Credential received successfully!", width="stretch")
        open_dashboard()
    else:
        st.warning("Empty credentials are not allowed. Please try again!", width="stretch")
        
st.title("Welcome to the bookmarker app! The place where your favorite books are.")
st.header("Before we start, please enter your credentials to login.")

with st.form(key="my_form"):
    username = st.text_input("Enter your username: ", placeholder="Your username here")
    password = st.text_input("Enter your password: ", type="password", placeholder="Your secret password here")
    if st.form_submit_button("Submit"):
        verify_login(username, password)