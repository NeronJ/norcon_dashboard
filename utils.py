import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://images.squarespace-cdn.com/content/v1/5dd3cc5b7fd99372fbb04561/11220443-3caa-4681-9e3c-b518097ea2d0/Official+logo_fullname_fullcolour_for+dark+bg+-+no+outline%40FFNPT.png?format=100w',use_column_width='auto', width=200,)
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
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