import streamlit as st
from PIL import Image
import time


st.title("Autobiography")


st.divider()
st.header("My Story")

st.divider()
st.header("Future Goals")

st.markdown("""
<style>
.card {
    display: flex;
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    gap: 20px;
}
.card-left {
    flex: 1;
}
.card-right img {
    width: 220px;
    border-radius: 10px;
}
</style>
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

descriptions = {
    2004: "Born in a small town. first memories of school and family.",
    2005: "Started kindergarten and learned to ride a bicycle.",
    2006: "Discovered love for reading and storytelling.",
    2007: "Discovered love for reading and storytelling.",
    2008: "Discovered love for reading and storytelling.",
    2009: "Discovered love for reading and storytelling.",
    2010: "Discovered love for reading and storytelling.",
    2011: "Discovered love for reading and storytelling.",
    2012: "Discovered love for reading and storytelling.",
    2013: "Discovered love for reading and storytelling.",
    2014: "Discovered love for reading and storytelling.",
    2015: "Discovered love for reading and storytelling.",
    2016: "Discovered love for reading and storytelling.",
    2017: "Discovered love for reading and storytelling.",
    2018: "Discovered love for reading and storytelling.",
    2019: "Discovered love for reading and storytelling.",
    2020: "Discovered love for reading and storytelling.",
    2021: "Discovered love for reading and storytelling.",
    2022: "Discovered love for reading and storytelling.",
    2023: "Discovered love for reading and storytelling.",
    2024: "Discovered love for reading and storytelling.",
    2025: "Discovered love for reading and storytelling.",
}


start_year = min(images.keys())
end_year = max(images.keys())

loaded_images = {year: Image.open(path) for year, path in images.items()}

year = st.slider("Me through the years", start_year, end_year, 2005)
current_img = loaded_images[year]
description = descriptions.get(year, "Amazing picture of ME!")

# Use Streamlit's columns INSIDE the card
col1, col2 = st.columns([1, 1])

# LEFT SIDE (text)
with col1:
    st.markdown('<div class="card-left">', unsafe_allow_html=True)
    st.markdown(f"<h3>Year {year}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p>{description}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# RIGHT SIDE (image)
with col2:
    st.markdown('<div class="card-right">', unsafe_allow_html=True)
    st.image(current_img, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


st.divider()
st.header("My Hobbies")

st.divider()
st.header("My Top 10 Movies")

st.divider()
st.header("Favorite Quote")
