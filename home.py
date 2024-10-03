import streamlit as st
def show_home():
    st.title("Welcome to My APP")
    st.write("This is a app which show spotify data visualization")
    logo_path = "D:\VIT\Programming for DataScience\Lab_work\APP deployment using streamlit\images.png"  

    # Display the image
    st.image(logo_path, width=200)


    st.write("Page 3 will Make your webscraping Easy")
    logo_path2 = "D:\VIT\Programming for DataScience\Lab_work\APP deployment using streamlit\images (1).png"  

    # Display the image
    st.image(logo_path2, width=200)
