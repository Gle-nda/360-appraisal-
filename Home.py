from pathlib import Path
import streamlit as st
from PIL import Image

# STREAMLIT PAGE CONFIG.

st.set_page_config(page_title='360° Appraisal System', page_icon='⚖️⭐', layout="centered",
                   initial_sidebar_state="collapsed")

hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CSS.

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# LOGO.

logo = current_dir / "assets" / "logo.jpg"
logo = Image.open(logo)

st.title("360° Appraisal System.")
st.image(logo, use_column_width=True)
