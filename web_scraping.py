import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def show_web_scraping():
    st.title("Web Scraping Page")

    # Input URL
    url = st.text_input("Enter the URL of a webpage to scrape:", "https://example.com")

    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Display Webpage Title
            st.write("### Webpage Title")
            if soup.title:
                st.write(soup.title.string)
            else:
                st.write("No title found.")

            # Display First Paragraph
            st.write("### First Paragraph")
            first_p = soup.find('p')
            if first_p:
                st.write(first_p.get_text())
            else:
                st.write("No paragraph found.")

            # Display First 5 Images
            st.write("### First 5 Images")
            images = soup.find_all('img', src=True)
            
            if images:
                # Get the base URL to resolve relative image URLs
                base_url = "{0.scheme}://{0.netloc}".format(requests.utils.urlparse(url))
                
                # Extract the first 5 image sources
                image_urls = []
                for img in images[:5]:
                    img_src = img['src']
                    # Resolve relative URLs
                    img_url = urljoin(base_url, img_src)
                    image_urls.append(img_url)
                
                # Display images using Streamlit
                for idx, img_url in enumerate(image_urls, start=1):
                    st.write(f"**Image {idx}:**")
                    st.image(img_url, use_column_width=True)
            else:
                st.write("No images found on this webpage.")
        
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the URL: {e}")
