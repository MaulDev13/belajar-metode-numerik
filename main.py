import streamlit as st

# App title
st.title("Metode Numerik App")

# Input field
name = st.text_input("Enter your name:")

# Button
if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name} 👋")
    else:
        st.warning("Please enter your name.")