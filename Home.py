import streamlit as st
import pandas

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

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:1].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")

with col4:
    for index, row in df[1:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")