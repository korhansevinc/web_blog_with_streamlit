import streamlit as st
from PIL import Image

def certificates_page():
    st.title("Certificates Page")
    st.write("Certificates page içeriği")
    st.title("My Certificates :")
    cer_image = Image.open("https://github.com/korhansevinc/web_blog_with_streamlit/blob/main/images/cer1.png")
    cer_image2 = Image.open("https://github.com/korhansevinc/web_blog_with_streamlit/blob/main/images/cer2.png")
    st.image(cer_image, caption="MERN STACK PROJECT", use_column_width=True)    
    st.image(cer_image2, caption="JAVA PROGRAMMING", use_column_width=True)    
