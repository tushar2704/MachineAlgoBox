#Authot github.com/tushar2704





##############################################################################################################
#Importing required library
##############################################################################################################
import streamlit as st






##############################################################################################################
#Streamlit page config
##############################################################################################################
st.set_page_config(page_title="Stats Mosaic 📊",
                   page_icon=":📊:",
                   layout='wide')
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


##############################################################################################################
#Home page
##############################################################################################################
with open('custom_styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
#title
st.title("Stats Mosaic 📊")
st.markdown('''<style>
            div.block-container{padding-top: 0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
            </style>''',
            unsafe_allow_html=True)
st.markdown("Welcome to the Stats Mosaic! Explore and visualize important statistical topics with interactive and informative visuals. Whether you're a data enthusiast, student, or professional, Stats Mosaic provides a comprehensive overview of various statistical concepts.")
st.markdown("""[Tushar-Aggarwal.com](https://tushar-aggarwal.com/)""")