import streamlit as st

def cv_page():
    st.title("CV Page")
    st.write("CV page içeriği")
    st.title("My CV :")
    cv_pic_one = "../images/cv/cv1.png"
    cv_pic_two = "../images/cv/cv2.png"
    st.image(cv_pic_one, caption="cv part 1 ", use_column_width=True)
    st.image(cv_pic_two, caption="cv part 2", use_column_width=True)