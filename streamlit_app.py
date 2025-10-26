import streamlit as st
from pathlib import Path

st.set_page_config(page_title="ブロック崩し（Web版）", layout="wide")
st.title("ブロック崩し（Web版）")

# GitHub Pages 上の公開URL（末尾スラッシュ必須！）
PAGES_BASE = "https://honohanahonobono-art.github.io/block_game1/"

# リポジトリ内の docs/index.html を読み込む
html = Path("docs/index.html").read_text(encoding="utf-8")

# <head> 直後に <base> を差し込んで、相対パスを GitHub Pages に向ける
html = html.replace("<head>", f"<head><base href='{PAGES_BASE}'>")

# HTMLをそのまま描画（外部URLの iframe ではなく、ローカルHTMLを描く）
st.components.v1.html(html, height=700, scrolling=False)
