import streamlit as st

def projects_page():
    st.title("Projects Page")
    st.write("Projects page içeriği: Burayı projelerimi github'a yükledikce düzenleyecegim.")
    projects()

def projects():
    # Projeler
    st.subheader("Projelerim")
    projeler = [
        {
            "baslik": "Proje 1",
            "aciklama": "Bu, projenin kısa açıklamasıdır. Projemizin amacı...",
            "github_url": "https://github.com/korhansevinc",
            "dokuman": "Proje1_Dokuman.pdf"
        },
        {
            "baslik": "Proje 2",
            "aciklama": "Bu, projenin kısa açıklamasıdır. Projemizin amacı...",
            "github_url": "https://github.com/korhansevinc",
            "dokuman": "Proje2_Dokuman.docx"
        },
        {
            "baslik": "Proje 3: Streamlit ile Hazirlanmis Kisisel Web Sayfasi",
            "aciklama": "Bu, bir kisiel web blogu sayfasidir. Streamlit ile web-sayfasi yapimi ogrenimi icin yapilmis ornek bir web-blogudur.",
            "github_url": "https://github.com/korhansevinc/web_blog_with_streamlit",
            "dokuman": "Proje3_Dokuman.docx"
        }
    ]

    for proje in projeler:
        st.write(f"## {proje['baslik']}")
        st.write(proje['aciklama'])
        st.write(f"GitHub: [{proje['baslik']}]({proje['github_url']})")
        if proje['dokuman']:
            st.write(f"Dokümantasyon: [Doküman]({proje['dokuman']})")
        st.write("---")

