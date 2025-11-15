import streamlit as st
from PIL import Image
import streamlit_shadcn_ui as ui

profile_pic = Image.open("assets/profile_picture.png")
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
st.header("Project")

# ---------- CONTACT CARD ----------
st.markdown("""
<style>
.contact-card {
    display: flex;
    flex-direction: column;
    background-color: #f8f9fa;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
.contact-card h3 {
    margin-bottom: 15px;
}
.contact-card a {
    text-decoration: none;
    color: #1a73e8;
    margin-right: 15px;
}
.contact-card a:hover {
    text-decoration: underline;
}
.contact-links {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# Prepare social links HTML
social_html = ""
for platform, link in SOCIAL_MEDIA.items():
    icon = social_icons.get(platform, "🌐")
    social_html += f"<a href='{link}' target='_blank'>{icon} {platform}</a> "

# Full card HTML
contact_card_html = f"""
<div class="contact-card">
    <h3>Contact Me</h3>
    <p>📞 <a href='tel:{PHONE.replace(' ', '')}'>{PHONE}</a></p>
    <p>✉️ <a href='mailto:{EMAIL}'>{EMAIL}</a></p>
    <div class="contact-links">
        {social_html}
    </div>
</div>
"""

# Render card
st.markdown(contact_card_html, unsafe_allow_html=True)


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

