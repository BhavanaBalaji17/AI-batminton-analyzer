import streamlit as st
from ui import apply_style, title, card_start, card_end
from pose_detection import analyze_video

apply_style()

title("🏸 AI Badminton Training Assistant")
st.markdown("""
### 🎯 What this app does  
This app analyzes your badminton shots using AI-based pose detection to evaluate your technique, provide instant feedback, and track your improvement over time.

### ⚙️ How it works  
Upload a video of your shot, and the system uses pose estimation to detect key body joints like your elbow, wrist, and shoulder. It then analyzes your movement patterns to generate a score and personalized feedback.

""")

st.info("Tip: Record your video from the side for better accuracy")

# Upload + Shot Selection
card_start()
video_file = st.file_uploader("Upload your badminton shot")
shot_type = st.selectbox(
    "Select Shot Type",
    ["Smash", "Drop", "Clear", "Forehand Lift", "Backhand Lift"]
)
card_end()


# SIDE BY SIDE LAYOUT
col1, col2 = st.columns(2)

with col1:
    card_start()
    st.subheader("Your Video")
    if video_file:
        st.video(video_file)
    card_end()

with col2:
    card_start()
    st.subheader("Ideal Shot")

    if shot_type == "Smash":
        st.video("smash.mp4")
    elif shot_type == "Drop":
        st.video("drop.mp4")
    elif shot_type == "Clear":
        st.video("clear.mp4")
    elif shot_type == "Forehand Lift":
        st.video("forehand_lift.mp4")
    elif shot_type == "Backhand Lift":
        st.video("backhand_lift.mp4")

    card_end()


# ANALYZE BUTTON
if st.button("Analyze"):
    if video_file:
        st.success("Analyzing...")

        feedback, score = analyze_video(video_file, shot_type)

        # 👉 STORE DATA
        if "history" not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append({
            "shot": shot_type,
            "score": score,
            "feedback": feedback
        })

        # 👉 DISPLAY
        card_start()
        st.subheader("Score")
        st.write(f"### {score}/10")

        st.subheader("Feedback")
        for f in feedback:
            st.write(f"• {f}")
        card_end()
        