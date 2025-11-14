import streamlit as st

project_1_page = st.Page(
    page="views/autobiography.py",
    title="Autobiography",
    icon="🍒",
    default=True,
)

project_2_page = st.Page(
    page="views/portfolio.py",
    title="Portfolio",
    icon="🍕",
)

st.sidebar.text("made with 🤍 by gianna")
pg = st.navigation(pages=[project_1_page, project_2_page])