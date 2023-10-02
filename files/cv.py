import streamlit as st
from PIL import Image

def cv_page():
    st.title("CV Page")
    st.write("CV page içeriği")
    st.title("My CV :")
    cv_image = Image.open("cv1.png")
    cv_image2 = Image.open("cv2.png")
    st.image(cv_image, caption="Korhan Sevinc's CV", use_column_width=True)    
    st.image(cv_image2, caption="Korhan Sevinc's CV", use_column_width=True)    