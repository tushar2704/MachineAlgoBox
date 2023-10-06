#Authot github.com/tushar2704





##############################################################################################################
#Importing required library
##############################################################################################################
import streamlit as st
import pandas as pd
import  streamlit_toggle as tog
import  streamlit_toggle as tog



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
st.title("About📊")
st.markdown('''<style>
            div.block-container{padding-top: 0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
            </style>''',
            unsafe_allow_html=True)
##############################################################################################################
#Data integration
##############################################################################################################



general_terms = {
    "Data": {
        "Definition": "Data refers to raw facts, numbers, or information that can be collected, measured, and analyzed. It can be in various formats, such as numbers, text, images, or more complex structures.",
        "Example": "In a retail business, sales data might include daily transaction records, customer information, and product inventory details."
    },
    "Population": {
        "Definition": "Population refers to the entire group or set of individuals, objects, or observations about which you want to draw conclusions. It represents the full scope of the study.",
        "Example": "If you are conducting a survey to understand the preferences of all residents in a city, the entire city's population would be your population."
    },
    "Sample": {
        "Definition": "A sample is a subset of the population that is selected for analysis or study. It should ideally represent the characteristics of the larger population.",
        "Example": "To estimate the average income of all households in a country, you might survey a random sample of 1,000 households."
    },
    "Variable": {
        "Definition": "A variable is a characteristic, property, or quantity that can take on different values or states in a study or experiment. Variables are used to measure, analyze, and understand data.",
        "Example": "In a health study, variables can include age, gender, blood pressure, and cholesterol levels."
    },
    "Discrete Variable": {
        "Definition": "A discrete variable is a type of variable that can only take on distinct, separate values. It usually involves counting and often has finite possibilities.",
        "Example": "The number of cars in a parking lot is a discrete variable because it can only be whole numbers like 0, 1, 2, and so on."
    },
    "Continuous Variable": {
        "Definition": "A continuous variable is a type of variable that can take on any value within a given range. It typically involves measurement and has an infinite number of possible values.",
        "Example": "Height, weight, and temperature are continuous variables because they can have values like 170.5 cm, 65.3 kg, or 23.6°C."
    },
    "Categorical Variables": {
        "Definition": "Categorical variables, also known as nominal variables, represent data that can be divided into distinct categories or groups with no inherent order or ranking.",
        "Example": "Colors (e.g., red, green, blue) and animal types (e.g., cat, dog, bird) are examples of categorical variables."
    },
    "Ordinal Variables": {
        "Definition": "Ordinal variables are categorical variables that have a specific order or ranking among their categories, but the differences between the categories are not necessarily uniform or measurable.",
        "Example": "Educational levels (e.g., high school, bachelor's degree, master's degree) are ordinal variables because there is an order, but the difference in education level may not be the same between categories."
    },
    "Independent and Dependent Variables": {
        "Definition": "In experimental research, the independent variable is the factor that is manipulated or changed to observe its effect on the dependent variable. The dependent variable is the outcome being measured.",
        "Example": "In a drug trial, the independent variable may be the dosage of a medication, and the dependent variable is the patient's health improvement."
    }
}




# Create a DataFrame from the dictionary
general_terms = pd.DataFrame(general_terms).T.reset_index()

# Rename the columns
general_terms.columns = ["Term", "Definition", "Example"]










##############################################################################################################
#Utils
##############################################################################################################
# Display the selected term and its definition


def write():
    st.write(f"**Definition:** {general_terms.loc[general_terms['Term'] == selected_term, 'Definition'].values[0]}")
    st.write(f"**Example:** {general_terms.loc[general_terms['Term'] == selected_term, 'Example'].values[0]}")



































##############################################################################################################
#Body
##############################################################################################################

selected_term = st.selectbox("Select a Term:", general_terms["Term"],key="definations",
                             placeholder="Choose an option",label_visibility="visible")
if selected_term:
    write()

















































































































































































































































