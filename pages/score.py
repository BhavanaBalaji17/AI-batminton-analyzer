import streamlit as st
from ui import apply_style, title, card_start, card_end

apply_style()
title("Your Scores")

if "history" not in st.session_state or len(st.session_state.history) == 0:
    st.write("No data yet. Analyze a video first.")
else:
    for item in reversed(st.session_state.history):
        card_start()
        st.write(f"### {item['shot']}")
        st.write(f"Score: {item['score']}/10")

        st.write("Feedback:")
        for f in item["feedback"]:
            st.write(f"• {f}")

        card_end()
        