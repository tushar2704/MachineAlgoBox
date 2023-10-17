#Authot github.com/tushar2704





##############################################################################################################
#Importing required library
##############################################################################################################
import streamlit as st






##############################################################################################################
#Streamlit page config
##############################################################################################################
st.set_page_config(page_title="MachineAlgoBox🤖",
                   page_icon=":🤖:",
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
st.title("Measrure of Spread📊")
st.markdown('''<style>
            div.block-container{padding-top: 0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
            </style>''',
            unsafe_allow_html=True)
