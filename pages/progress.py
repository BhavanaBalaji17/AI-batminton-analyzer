import streamlit as st
import matplotlib.pyplot as plt
from ui import apply_style, title

apply_style()
title("Progress Tracker")

if "history" not in st.session_state or len(st.session_state.history) == 0:
    st.write("No data yet. Analyze videos first.")
else:
    scores = [item["score"] for item in st.session_state.history]

    # 🔥 Create clean dark graph
    fig, ax = plt.subplots()

    # Background color
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Plot line
    ax.plot(scores, marker='o', linewidth=2)

    # Remove top/right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Light borders for left/bottom
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')

    # Labels
    ax.set_xlabel("Attempt", color='white')
    ax.set_ylabel("Score", color='white')
    ax.set_title("Your Progress", color='white')

    # Tick colors
    ax.tick_params(colors='white')

    # Remove heavy grid (optional clean look)
    ax.grid(alpha=0.2)

    st.pyplot(fig)

