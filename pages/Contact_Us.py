import streamlit as st

st.header("Contact Me") 

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    # Allows us to enter multiple lines of text 
    button = st.form_submit_button("Submit")
    if button:
        print("I was pressed!")