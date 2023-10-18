#Authot github.com/tushar2704





##############################################################################################################
#Importing required library
##############################################################################################################
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))


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
st.title("Stats Mosaic 📊")
st.markdown('''<style>
            div.block-container{padding-top: 0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
            </style>''',
            unsafe_allow_html=True)










# ##############################################################################################################
# #Body for What is
# ##############################################################################################################

# st.write("Stats Mosaic is a data-driven application that provides interactive visualizations "
#          "for exploring important statistical concepts.")

# # Create a sample visualization (you can replace this with your own)
# st.header("Sample Visualization: Distribution Plot")
# st.write("Let's start with a simple example. Below is a distribution plot of a random dataset:")

# # Create a sidebar with interactive controls
# st.sidebar.header("Histogram Controls")
# num_bins = st.sidebar.slider("Number of Bins", min_value=1, max_value=50, value=20)
# data_mean = st.sidebar.slider("Mean of Data", min_value=-10.0, max_value=10.0, value=0.0)
# data_std = st.sidebar.slider("Standard Deviation", min_value=0.1, max_value=5.0, value=1.0)

# # Generate random data based on user input
# data = np.random.normal(loc=data_mean, scale=data_std, size=1000)

# # Create the histogram based on user-selected number of bins
# fig, ax = plt.subplots()
# ax.hist(data, bins=num_bins, color='b', alpha=0.7)
# ax.set_xlabel('Value')
# ax.set_ylabel('Frequency')
# ax.set_facecolor('none')
# # Set the background color to transparent (alpha=0)
# fig.patch.set_facecolor('none')

# # Save the figure with a transparent background
# st.pyplot(fig)


# # Create a button to download the figure
# if st.button("Download Histogram"):
#     # Save the figure to a BytesIO buffer
#     buffer = BytesIO()
#     plt.savefig(buffer, format="png")
#     buffer.seek(0)
    
#     # Trigger the download
#     st.download_button(
#         label="Click to Download",
#         data=buffer,
#         file_name="histogram.png",
#         key="download_histogram"
#     )

text= "testing sidebar"

from src.MachineAlgoBox.components.siderbar import *


sidebar_1(text)







































