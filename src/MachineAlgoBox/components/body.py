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
#Application Body functions
##############################################################################################################

def main_body(title=None, header=None, subheader=None, markdown=None, write=None, code=None):
    ''' 
    Displaying Main body conponents
    '''
    if title:
        st.title(title)
    
    if header:
        st.header(header)
    
    if subheader:
        st.subheader(subheader)
    
    if markdown:
        st.markdown(markdown)
    
    if write:
        st.write(write)
    
    if code:
        st.code(code)
















































































































































































































