import streamlit as st
import pandas
# pandas can read csv data

st.set_page_config(layout="wide")
# configures page settings such as the width

col1, col2 = st.columns(2)
# .columns returns two column instances

with col1:
    st.image("files/images/photo.png")
    # adding width= allows us to adjust the size of the image

with col2:
    st.title("Bryant Garcia")
    content = """
    Hello!
    """
    st.info(content)
    # Use info instead of write to change the text format
    
content2 = """
Below you can find some of the apps I have build in Python. Feel free to contact me. 
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("files/data.csv", sep=";")
# the default "sep" is a comma

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
# Splits the list into two columns based on their index. 