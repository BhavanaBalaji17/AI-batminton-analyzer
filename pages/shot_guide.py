import streamlit as st
from ui import apply_style, title, card_start, card_end

apply_style()
title("Shot Guide")

# Dropdown
shot_type = st.selectbox(
    "Select Shot",
    ["Smash", "Drop", "Clear", "Forehand Lift", "Backhand Lift"]
)

card_start()

# ---------------- SMASH ----------------
if shot_type == "Smash":
    st.subheader("Smash Technique")

    tips = [
        "Start with a side-on stance facing sideways to the net",
        "Grip the racket firmly but stay relaxed",
        "Raise your non-racket arm for balance",
        "Bring your racket arm back with elbow high",
        "Jump or step forward to gain momentum",
        "Rotate your shoulders and hips into the shot",
        "Fully extend your arm at contact point",
        "Snap your wrist for maximum power",
        "Follow through across your body after hitting",
    ]

# ---------------- DROP ----------------
elif shot_type == "Drop":
    st.subheader("Drop Shot Technique")

    tips = [
        "Use the same preparation as a smash to disguise the shot",
        "Keep your grip relaxed for better control",
        "Position yourself behind the shuttle",
        "Slow down your swing just before contact",
        "Use a soft touch instead of power",
        "Aim just over the net for tight placement",
        "Keep your wrist flexible for control",
        "Recover quickly to the center after the shot",
    ]

# ---------------- CLEAR ----------------
elif shot_type == "Clear":
    st.subheader("Clear Shot Technique")

    tips = [
        "Stand side-on with good balance",
        "Use a forehand grip",
        "Move quickly behind the shuttle",
        "Raise your racket arm early",
        "Contact shuttle at highest point",
        "Use full arm swing for distance",
        "Rotate shoulders and hips for power",
        "Follow through completely",
        "Aim deep into opponent’s court",
    ]

# ---------------- FOREHAND LIFT ----------------
elif shot_type == "Forehand Lift":
    st.subheader("Forehand Lift Technique")

    tips = [
        "Stay low with knees slightly bent",
        "Use a forehand grip",
        "Position yourself under the shuttle",
        "Swing upward with a controlled motion",
        "Use your wrist to guide the shuttle",
        "Aim high and deep toward the backcourt",
        "Maintain balance while hitting",
        "Recover quickly after the shot",
    ]

# ---------------- BACKHAND LIFT ----------------
elif shot_type == "Backhand Lift":
    st.subheader("Backhand Lift Technique")

    tips = [
        "Use a backhand grip",
        "Keep your elbow slightly bent",
        "Position your body sideways",
        "Push the shuttle upward using wrist power",
        "Avoid excessive arm movement",
        "Aim high to gain time",
        "Stay balanced during the shot",
        "Return quickly to ready position",
    ]

# DISPLAY TIPS
for i, tip in enumerate(tips, start=1):
    st.write(f"{i}. {tip}")

card_end()
