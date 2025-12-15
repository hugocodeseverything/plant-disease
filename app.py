import streamlit as st


hide_style = """
<style>
    section[data-testid="stSidebar"] .css-1oe5cao, 
    section[data-testid="stSidebar"] .css-1v0mbdj {
        display: none !important;
    }
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

st.switch_page("pages/1_Prediction Machine.py")
