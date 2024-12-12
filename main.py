import streamlit as st
import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special):
    characters = ""

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        return "Select at least one character type"

    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit application
st.title("🔑 Password Generator")
st.markdown("""
<style>
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
    }
    div.stButton > button:hover {
        background-color: #45a049;
    }
    .stMarkdown {
        font-family: Arial, sans-serif;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# Input fields
st.markdown("### Select Options:")
length = st.number_input("Length of password:", min_value=4, max_value=128, value=12, step=1)
include_uppercase = st.checkbox("Include uppercase letters")
include_lowercase = st.checkbox("Include lowercase letters", value=True)
include_numbers = st.checkbox("Include numbers", value=True)
include_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special)
    if password == "Select at least one character type":
        st.error(password)
    else:
        st.success("Generated Password:")
        st.code(password, language='text')
