import streamlit as st
from PIL import Image
import streamlit_shadcn_ui as ui

profile_pic = Image.open("assets/profile_picture.png")


ABOUT = (
    "<h3>About Me</h3>"
    "<p>Curious and driven Computer Science Student with a strong passion"
    " for building intuitive digital experiences. Blending creativity and technology."
    " I value clean design, thoughtful execution and learning by creating."
)

st.divider()
col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_pic)


with col2: 
    st.markdown(f"""
    <div>
        {ABOUT}
    </div>
    """, unsafe_allow_html=True)
    if st.button("Get to know me!"):
        st.switch_page("views/autobiography.py")



st.divider()
st.header("💡 Skills Overview")
col1, col2, col3 = st.columns(3)

col1.progress(0.7)
col1.write("Python 🐍")

col2.progress(0.80)
col2.write("Java ☕")

col3.progress(0.66)
col3.write("C++ 💻")

col1.progress(0.75)
col1.write("MySQL 🗃️")

col2.progress(0.8)
col2.write("HTML/CSS 🌐")

col3.progress(0.4)
col3.write("React Native 🧶")



# my certificate section

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
            min-height: 700;
        }
    </style>
""", unsafe_allow_html=True)

st.header("🧾 Certificate")

tabs = st.tabs(["🐍 Python", "☕ Java", "🎨 Canva", "⚙️ C"])

with tabs[0]:
    box = st.container()
    box.image("assets/python_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 200px; max-height:200px;''></div>", unsafe_allow_html=True)

with tabs[1]:
    box = st.container()
    box.image("assets/java_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 200px; max-height:200px;'></div>", unsafe_allow_html=True)

with tabs[2]:
    box = st.container()
    box.image("assets/Canva_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 200px; max-height:200px;'></div>", unsafe_allow_html=True)

with tabs[3]:
    box = st.container()
    box.image("assets/C_certificate.png", use_container_width=True)
    box.markdown("<div style='min-height: 200px; max-height:200px;'></div>", unsafe_allow_html=True)

