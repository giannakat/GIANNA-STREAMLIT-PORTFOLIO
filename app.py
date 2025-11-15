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




