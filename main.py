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
            flex-direction: row;
        }

        .left-section {
            flex: 1;
            background: linear-gradient(to bottom right, #0080ff, #00bfff);
            padding: 20px;
            transform: skewX(-15deg);
            color: white;
            text-align: center;
        }

        .right-section {
            flex: 1;
            padding: 20px;
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
            <div class="left-section">
                <h1>Logo</h1>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
            <div class="right-section">
                <h1>URL Analysis</h1>
                <form>
                    <label for="url">Enter URL:</label><br>
                    <input type="text" id="url" name="url"><br><br>
                    <input type="submit" value="Submit">
                </form>
            </div>
        </div>
        """
        ,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .container {
            display: flex;
            flex-direction: row;
        }

        .left-section {
            flex: 1;
        }

        .right-section {
            flex: 1;
            padding: 20px;
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
            <div class="left-section"></div>
            <div class="right-section">
                <h1>URL Analysis</h1>
                <form>
                    <label for="url">Enter URL:</label><br>
                    <input type="text" id="url" name="url"><br><br>
                    <input type="submit" value="Submit">
                </form>
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
