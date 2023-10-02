import streamlit as st

def certificates_page():
    st.title("Certificates Page")
    st.title("My Certificates :")
    certificate_pic_path_one = "../images/certificates/cer1.png"
    certificate_pic_path_two = "../images/certificates/cer2.png"
    st.image(certificate_pic_path_one, caption="Sertifikam 1 ", use_column_width=True)
    st.image(certificate_pic_path_two, caption="Sertifikam 2", use_column_width=True)