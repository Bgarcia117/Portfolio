import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("files/images/photo.png")
    # width= allows us to adjust the size of the image

with col2:
    st.title("Bryant Garcia")
    content = """
    Hello!
    """
    st.info(content)
    # Use info instead of write to change the text format