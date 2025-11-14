import streamlit as st

st.title("Gianna's Portfolio")

st.markdown("""
    <style>
        .stTabs [data-baseweb="tab-list"] {
            justify-content: space-between;
        }
        .stTabs [data-baseweb="tab"] {
            flex-grow: 1;
            text-align: center;
        }
        .tab-content {
            min-height: 1500px;
        }
    </style>
""", unsafe_allow_html=True)

tabs = st.tabs(["🐍 Python", "☕ Java", "🎨 Canva", "⚙️ C"])

with tabs[0]:
    box = st.container()
    box.image("assets/python_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 700px'></div>", unsafe_allow_html=True)

with tabs[1]:
    box = st.container()
    box.image("assets/java_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 700px'></div>", unsafe_allow_html=True)

with tabs[2]:
    box = st.container()
    box.image("assets/Canva_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 700px'></div>", unsafe_allow_html=True)

with tabs[3]:
    box = st.container()
    box.image("assets/C_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 700px'></div>", unsafe_allow_html=True)



