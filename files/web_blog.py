import streamlit as st
from cv import cv_page
from projects import projects_page
from certificates import certificates_page

def blog_gonderilerim():
    blog_gonderileri = [
        {
            "baslik": "İlk Gönderi",
            "yazar": "Korhan Sevinc",
            "icerik": "Bu, ilk blog gönderisidir. Streamlit ile oluşturuldu!",
            "tarih": "2023-09-24"
        },
        {
            "baslik": "İkinci Gönderi",
            "yazar": "Korhan Sevinc",
            "icerik": "İkinci gönderi burada! Streamlit harika!",
            "tarih": "2023-09-25"
        }
    ]
    for gonderi in blog_gonderileri:
        st.write(f"## {gonderi['baslik']}")
        st.write(f"**Yazar:** {gonderi['yazar']}")
        st.write(f"**Tarih:** {gonderi['tarih']}")
        st.write(gonderi['icerik'])
        st.write("---")

def sertifikalarim():
    st.sidebar.subheader("Sertifikalar")
    sertifikalar = st.sidebar.text_area("Sertifikalarınızı girin (her bir sertifika bir satırda olmalıdır):")

    if sertifikalar:
        sertifika_listesi = sertifikalar.split("\n")
        st.sidebar.success("Sertifikalar başarıyla eklendi!")
        st.sidebar.write("Sertifikalarınız:")
        for sertifika in sertifika_listesi:
            st.sidebar.write(f"- {sertifika}")            

def CV_for_sidebar():
    st.sidebar.subheader("CV")
    cv_link = st.sidebar.file_uploader("CV Yükle (PDF formatında)", type=["pdf"])

    if cv_link:
        st.sidebar.success("CV başarıyla yüklendi!")
        st.sidebar.write("CV dosyanızı buradan indirebilirsiniz:", cv_link)

def baslik():
    st.title("Benim  Web Blogum")
    st.write("Bu, Streamlit ile oluşturulan bir web blogudur.")


def profil():
     # Profil kısmı
    proflie_pic_path = "../images/profile/profile_image.png"

    st.sidebar.image(proflie_pic_path, caption="Benim Profil Resmim", use_column_width=True)
    st.sidebar.subheader("Hakkımda")
    st.sidebar.write("Merhaba! Ben  Korhan Sevinç ve bu benim web blogum. TOBB Ekonomi ve Teknoloji Üniversitesinde Bilgisayar Mühendisliği bölümü 3. sınıf öğrencisiyim.")
    st.sidebar.write("Yapay Zeka alaninda arastirma yapmak, muzik dinlemek ve gitar calmak, spor yapmak, bilgisayar oyunları ve LOTR evrenini ilgi alanlarım olarak sayabilirim.")
    st.sidebar.write("Herhangi bir ilgi alanımda sahip olduğum görüşleri veya incelemeleri gönderiler kısmında, hakkımda daha fazla bilgi için sosyal medya kısmı veya CV veya Sertifikalar'da, gelistirdigim projeleri ise Projelerim kısmında bulabilirsiniz.")
    st.sidebar.subheader("Sosyal Medya")
    st.sidebar.text_input("GitHub Profil Linki", "https://github.com/korhansevinc")
    st.sidebar.text_input("LinkedIn Profil Linki", "https://www.linkedin.com/in/korhan-sevin%C3%A7-97b03a279/")

def web_blog_home_page():    
    baslik()
    profil()
    CV_for_sidebar()
    sertifikalarim()
    blog_gonderilerim()

def pages_with_buttons():
    st.markdown(""" 
        <div style= "padding: 10px; color: white; text-align: center;">
            <h1>Üst Bilgi Çubugu </h1>
            <button style="background-color: #007BFF; color: white; border: none; padding: 10px 20px; margin-right: 10px;"> BUTON_SAMPLE_1 </button>
            <button style="background-color: #007BFF; color: white; border: none; padding: 10px 20px; margin-right: 10px;"> BUTON_SAMPLE_2 </button>
            <button style="background-color: #007BFF; color: white; border: none; padding: 10px 20px; margin-right: 10px;"> BUTON_SAMPLE_3 </button>
        </div>
        """, unsafe_allow_html=True)



def pages_with_radio():
    page = "Ana Sayfa"
    page = st.sidebar.radio("Component Secimi",("Ana Sayfa", "CV", "Projelerim","Sertifikalarim"))
    if page == "Ana Sayfa":
        web_blog_home_page()
    elif page == "CV":
        cv_page()
        profil()
    elif page == "Projelerim":
        projects_page()
        profil()
    elif page == "Sertifikalarim":
        certificates_page()
        profil()

def main():
    pages_with_radio()
    #pages_with_buttons()
    

if __name__ == "__main__":
    main()
