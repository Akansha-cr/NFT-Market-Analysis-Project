import streamlit as st
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import io
from PIL import Image
import base64

import streamlit as st
def main():
    # Add navigation bar
    st.markdown(
        """
        <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1px 60px;
            backdrop-filter: blur(10px);
            background-color: transparent;
            color: white;
            border-radius: 10px;
            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.1), -4px -4px 10px rgba(255, 255, 255, 0.5);
        }

        .navbar ul {
            list-style: none;
            display: flex;
            gap: 20px;
        }

        .navbar ul li {
            font-size: 15px;
        }

        .navbar ul li a {
            text-decoration: none;
            color: white;
            padding: 10px;
            border-radius: 20px;
            transition: background-color 0.3s ease;
            background-color: rgba(255, 255, 255, 0.5);
            box-shadow: inset 4px 4px 6px rgba(0, 0, 0, 0.1), inset -4px -4px 6px rgba(255, 255, 255, 0.5);
        }

        .navbar ul li a:hover {
            background-color: #f0f0f0;
            color: #333;
            box-shadow: inset 2px 2px 4px rgba(0, 0, 0, 0.1), inset -2px -2px 4px rgba(255, 255, 255, 0.5);
        }

        .main-section {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            height: calc(100vh - 100px); /* Subtracting the navbar height */
            padding: 20px;
        }

        .url-uploader {
            background-color: transparent;
            padding: 1px 30px;
            border-radius: 10px;
            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.1), -4px -4px 10px rgba(255, 255, 255, 0.5);
        }

        .url-uploader h2 {
            color: white;
        }

        .image-section {
            margin-right: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the page layout
    st.markdown(
        """
        <div class="navbar">
            <h1 style="margin-right: auto;">Analysis</h1>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#">About</a></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    first_section,main_section = st.columns(2)
    with first_section:
        image = Image.open("NFT-rafiki.png")
        st.image(image, width=300)
    # Create the main section layout
    with main_section:
        with st.container():
            st.markdown("<h2>Upload Url of any NFT Collection</h2>", unsafe_allow_html=True)

            url_input = st.text_input("Enter URL:")
            submit_button = st.button("Submit")

            if submit_button:
                st.write("Entered URL:", url_input)


if __name__ == "__main__":
    main()

#background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Untitled design (3).png')

