#Authot github.com/tushar2704
##############################################################################################################
#Importing required library
##############################################################################################################
import streamlit as st
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))

##############################################################################################################
#Sidebar functions
##############################################################################################################


def sidebar_1(text):
    st.title("Testing 101")
    st.markdown(" ### Testing 102")
    st.sidebar.write(text)




















































































































































































