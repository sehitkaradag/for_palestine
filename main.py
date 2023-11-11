import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title = "Palestine starterkit")
image = Image.open(Flag_of_Palestine.svg.png)
st.write("This will be for Palestine!")
