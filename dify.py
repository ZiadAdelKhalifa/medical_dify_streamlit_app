import streamlit as st

# Set page config
st.set_page_config(page_title="💎 Dify AI Magic Chat 💬", page_icon="💎", layout="centered")

# Custom CSS for styling 🌈
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        color: #ffffff;
    }
    .title {
        font-size: 60px;
        font-weight: 800;
        text-align: center;
        color: #fff;
        text-shadow: 2px 2px #333;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #e0e0e0;
        margin-bottom: 30px;
    }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin: auto;
        width: 750px;
    }
    iframe {
        border: none;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Subtitle
st.markdown('<div class="title">💎 Welcome to Dify AI Magic Chat 💬</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Talk to your AI assistant in style ✨</div>', unsafe_allow_html=True)

# Embed your Dify chat app inside a styled card
st.markdown('<div class="card">', unsafe_allow_html=True)

dify_url = "https://udify.app/chat/l6QTK6ceAC7TbgkT"
st.components.v1.iframe(dify_url, width=700, height=800)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align:center; margin-top: 30px; color:#fff;">
        Made with ❤️ by <b>Ziad</b> — Powered by <a style="color:#fff; text-decoration:underline;" href="https://udify.app/" target="_blank">Dify AI</a>
    </div>
""", unsafe_allow_html=True)
