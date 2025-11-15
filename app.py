import streamlit as st

#Include CSS into the page
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

project_1_page = st.Page(
    page="views/portfolio.py",
    title="Portfolio",
    icon="🍒",
    default=True,
)

project_2_page = st.Page(
    page="views/autobiography.py",
    title="Autobiography",
    icon="🍕",
)

st.markdown("""
<div class='hero'>
    <h1 class='hero-title'>Welcome to My Portfolio</h1>
    <p class='hero-sub'>A collection of my projects, stories, and creative work.</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.text("made with 🤍 by gianna")
pg = st.navigation(pages=[project_1_page, project_2_page])
pg.run()


#--- GENERAL SETTINGS ---
PAGE_TITLE = "About Gianna"
PAGE_ICON = "📋"

NAME = "Gianna Carreon"
FULL_NAME = "Gianna Katrin D. Carreon"
JOB_TITLE = "BS Computer Science Student"

EMAIL = "giannakatrin.carreon@cit.edu"
PHONE = "+63 946 3734 128"

SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/share/1BE8BrwBP9/?mibextid=wwXIfr",
    "Instagram": "https://www.instagram.com/giannaktrn_/",
    "LinkedIn": "https://www.linkedin.com/in/gk-carreon-53752a21a/",
    "GitHub": "https://github.com/giannakat"
}

social_icons = {
    "Facebook": "📘",
    "Instagram": "📸",
    "LinkedIn": "🔗",
    "GitHub": "💻",
}


# --- FOOTER ---
st.divider()
footer_cols = st.columns([1, 1, 1])
with footer_cols[0]:
    st.write("📞 Contact")
    st.write(f"[{PHONE}](tel:{PHONE.replace(' ', '')})")
    st.write(f"[{EMAIL}](mailto:{EMAIL})")
with footer_cols[1]:
    st.write("🔗 Connect")
    for platform, link in SOCIAL_MEDIA.items():
        icon = social_icons.get(platform, "🌐")
        st.markdown(f"<a href='{link}' target='_blank' class='footer-social-link'>{icon} {platform}</a>", unsafe_allow_html=True)
with footer_cols[2]:
    st.write("📄 Resources")
    # st.download_button(
    #     label="📄 Download Resume",
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime="application/octet-stream",
    # )
    st.write(f"© {NAME} | {JOB_TITLE}")


