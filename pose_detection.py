def analyze_video(video_file, shot_type):
    import cv2
    import mediapipe as mp
    import tempfile
    import numpy as np

    mp_pose = mp.solutions.pose

    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    cap = cv2.VideoCapture(tfile.name)
    pose = mp_pose.Pose()

    elbow_vals = []
    wrist_vals = []
    shoulder_vals = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark

            elbow = lm[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y
            shoulder = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
            wrist = lm[mp_pose.PoseLandmark.RIGHT_WRIST.value].y

            elbow_vals.append(elbow - shoulder)
            wrist_vals.append(wrist - elbow)
            shoulder_vals.append(shoulder)

    cap.release()

    # ❌ no detection case
    if len(elbow_vals) == 0:
        return ["No body detected"], 0

    # ✅ stats
    avg_elbow = np.mean(elbow_vals)
    std_elbow = np.std(elbow_vals)

    avg_wrist = np.mean(wrist_vals)
    std_wrist = np.std(wrist_vals)

    score = 10
    feedback = []

    # ---------------- UNIVERSAL RULES ----------------
    if std_elbow > 0.15:
        feedback.append("Inconsistent arm movement")
        score -= 2

    if std_wrist > 0.15:
        feedback.append("Wrist control inconsistent")
        score -= 1

    # ---------------- SHOT-SPECIFIC RULES ----------------

    if shot_type == "Smash":
        if avg_elbow > 0.05:
            feedback.append("Elbow too low during smash")
            score -= 3
        elif avg_elbow < -0.35:
            feedback.append("Overextension in smash")
            score -= 2
        else:
            feedback.append("Good smash form")

    elif shot_type == "Drop":
        if avg_elbow < -0.3:
            feedback.append("Too much power for drop shot")
            score -= 2
        else:
            feedback.append("Controlled drop technique")

    elif shot_type == "Clear":
        if avg_elbow > 0:
            feedback.append("Incomplete swing for clear")
            score -= 3
        else:
            feedback.append("Good clear technique")

    elif shot_type in ["Forehand Lift", "Backhand Lift"]:
        if std_elbow > 0.2:
            feedback.append("Unstable lift motion")
            score -= 2
        else:
            feedback.append("Stable lift execution")

    # ---------------- FINAL ----------------
    score = max(score, 0)

    return feedback, score