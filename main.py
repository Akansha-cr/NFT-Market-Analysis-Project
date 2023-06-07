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
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(to bottom right, #0080ff, #00bfff);
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
            width: 80%;
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
            color: #333;
            padding: 10px;
            border-radius: 20px;
            transition: background-color 0.3s ease;
        }

        .navbar ul li a:hover {
            background-color: #f0f0f0;
        }

        </style>
        """
        ,
        unsafe_allow_html=True
    )

    # Create the page layout
    st.markdown(
        """
        <div class="container">
            <div class="navbar">
                <h1>Logo</h1>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
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
