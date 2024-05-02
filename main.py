import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/picture.png")

with col2:
    st.title("Kyle Sumners")
    content = """"
    Hi, I'm Kyle! I've just completed my Sophomore year at Baylor university in Waco. I know Java, C++, Assembly,
    postgreSQL, Javascript, and CSS/HTML, and I am currently learning React and Python. I love learning new 
    programming languages and technologies in order to expand my skills. When I'm not at my computer coding I
    like to workout, read, play video games, and spend time with friends and family.
    """
    st.info(content)