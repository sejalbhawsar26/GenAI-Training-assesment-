import streamlit as st
import os
from backend import apply_style, change_pitch_and_speed

st.title("🎤 AI-Driven Voice Style Transfer")
st.write("Upload a voice file and apply style transformations.")

uploaded_file = st.file_uploader("Upload a .wav file", type=["wav"])

style = st.selectbox("Choose a style", ["chipmunk", "deep", "robotic", "vibrato", "slow", "fast"])

manual_pitch = st.slider("Manual pitch shift (steps)", -12, 12, 0)
manual_speed = st.slider("Manual speed (stretch factor)", 0.5, 2.0, 1.0)

if uploaded_file is not None:
    input_path = os.path.join("assets", uploaded_file.name)
    output_path = os.path.join("assets", "processed_" + uploaded_file.name)

    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Process"):
        if manual_pitch != 0 or manual_speed != 1.0:
            success, error = change_pitch_and_speed(input_path, output_path, manual_pitch, manual_speed)
        else:
            success, error = apply_style(input_path, output_path, style)

        if success:
            st.success("Processing complete!")
            st.audio(output_path)
            with open(output_path, "rb") as f:
                st.download_button("Download Processed File", f, file_name="output.wav")
        else:
            st.error(f"Processing failed: {error}")
