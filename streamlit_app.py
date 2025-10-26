import streamlit as st

st.set_page_config(page_title="ブロック崩し", layout="wide")
st.title("ブロック崩し（Web版）")

url = "https://honohanahonobono-art.github.io/block_game1/"  # ← あなたのURL
st.components.v1.iframe(url, height=700)
