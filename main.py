import streamlit as st
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import io
from PIL import Image
import base64

def main():
    # Add navigation bar
   st.markdown(
        """
        <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 15px;
            background: linear-gradient(to bottom right, #0080ff, #00bfff);
            border-radius: 0 0 15px 15px;
            color: white;
        }

        .navbar ul {
            list-style: none;
            display: flex;
            gap: 20px;
        }

        .navbar ul li {
            font-size: 18px;
        }

        .navbar ul li a {
            text-decoration: none;
            color: white;
            padding: 10px;
            border-radius: 20px;
            transition: background-color 0.3s ease;
        }

        .navbar ul li a:hover {
            background-color: #f0f0f0;
            color: #333;
        }

        </style>
        """
        ,
        unsafe_allow_html=True
    )

    # Create the page layout
   st.markdown(
        """
        <div class="navbar">
            <h1>Logo</h1>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
        """
        ,
        unsafe_allow_html=True
    )


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
add_bg_from_local('Untitled design.png')
