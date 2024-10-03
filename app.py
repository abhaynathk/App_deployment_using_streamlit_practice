import streamlit as st
from home import show_home
from data_analysis import show_data_analysis
from web_scraping import show_web_scraping


st.sidebar.title("Navigation")
pages= {
    "Home": show_home,
    "Data Analyis": show_data_analysis,
    "Web Scraping": show_web_scraping
}


selection =st.sidebar.radio("Go to",list(pages.keys()))

#show the selected page
pages[selection]()
