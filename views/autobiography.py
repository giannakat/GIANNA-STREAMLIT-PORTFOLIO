import streamlit as st
from PIL import Image
import time

st.title("Autobiography")


st.markdown("""
<style>
.card {
    display: flex;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
.card img {
    width: 200px;
    height: auto;
    border-radius: 8px;
    margin-right: 20px;
}
.card-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="card-content">
        <h3>Project Name</h3>
        <p>This is a description of the project. It can include bullets, links, and more.</p>
    </div>
</div>
""", unsafe_allow_html=True)

images = {
    2004: "assets/2004.png",
    2005: "assets/2005.png",
    2006: "assets/2006.png",
    2007: "assets/2007.png",
    2008: "assets/2008.png",
    2009: "assets/2009.png",
    2010: "assets/2010.png",
    2011: "assets/2011.png",
    2012: "assets/2012.png",
    2013: "assets/2013.png",
    2014: "assets/2014.png",
    2015: "assets/2015.png",
    2016: "assets/2016.png",
    2017: "assets/2017.png",
    2018: "assets/2018.png",
    2019: "assets/2019.png",
    2020: "assets/2020.png",
    2021: "assets/2021.png",
    2022: "assets/2022.png",
    2023: "assets/2023.png",
    2024: "assets/2024.png",
    2025: "assets/2025.png",

}
start_year = min(images.keys())
end_year = max(images.keys())

loaded_images = {year: Image.open(path) for year, path in images.items()}

year = st.slider("Choose a year", start_year, end_year, start_year)

st.image(loaded_images[year], width=400, use_container_width=True)

# if st.button("▶ Play Timeline"):
#     for y in range(start_year, end_year + 1):
#         with placeholder.container():
#             st.markdown(f"### Year: **{y}**")
#             st.image(images[y], width=400)
#             st.session_state.year = y
#         time.sleep(0.6)   # adjust speed
#     year = st.slider("Choose a year", start_year, end_year, start_year)
#     st.image(images[year], width=400)


