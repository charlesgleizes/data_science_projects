import streamlit as st
from PIL import Image
import base64
import streamlit as st
import base64

"""
    add_logo(): 
        Usecase: CSS code that changes layout of the sidebar, puts a logo and a title in place.
        Input: ____
        Output: Returns markdown with Logo and Company Name above pages

"""



def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/298/ear-of-corn_1f33d.png);
                background-repeat: no-repeat;
                padding-top: 60px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Foodix";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

import base64
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="50% 10%",
    margin_top="0%",
    image_width="60%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo2(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

