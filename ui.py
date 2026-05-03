import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    /* MAIN BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        color: white;
    }

    /* TEXT */
    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
    }

    /* CARDS */
    .card {
        background: rgba(30, 41, 59, 0.9);
        padding: 20px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }

    /* BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        border: none;
        font-weight: bold;
    }

    /* DROPDOWN + UPLOAD */
    .stSelectbox, .stFileUploader {
        background-color: #1e293b !important;
        border-radius: 10px;
        padding: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


def title(text):
    st.markdown(f"<h1 style='color:white'>{text}</h1>", unsafe_allow_html=True)


def card_start():
    st.markdown("<div class='card'>", unsafe_allow_html=True)


def card_end():
    st.markdown("</div>", unsafe_allow_html=True)
    