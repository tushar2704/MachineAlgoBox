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

title_html = """
<div style="background: linear-gradient(to left, #ada996 , #f2f2f2 ); padding: 30px; border-radius: 10px;">
    <h2 style="color:  	#011f4b;">Stats Mosaic 📊</h2>
    <p style="color:  	#011f4b;">Welcome to the Stats Mosaic! Explore and visualize important statistical topics with interactive and informative visuals. Whether you're a data enthusiast, student, or professional, Stats Mosaic provides a comprehensive overview of various statistical concepts.</p>
    <p style="color:  	#011f4b;"><a href="https://tushar-aggarwal.com/" style="color:  	#011f4b; text-decoration: none;">Tushar-Aggarwal.com</a></p>

</div>
"""
# Display the custom sidebar using st.markdown
st.markdown(title_html, unsafe_allow_html=True)
st.markdown('''<style>
            div.block-container{padding-top: 0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
            </style>''',
            unsafe_allow_html=True)
# st.markdown("Welcome to the Stats Mosaic! Explore and visualize important statistical topics with interactive and informative visuals. Whether you're a data enthusiast, student, or professional, Stats Mosaic provides a comprehensive overview of various statistical concepts.")
# st.markdown("""[Tushar-Aggarwal.com](https://tushar-aggarwal.com/)""")


########################################################################################################
#Pages Structure
########################################################################################################























































































































































































