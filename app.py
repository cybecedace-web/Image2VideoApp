import streamlit as st
from moviepy.editor import ImageSequenceClip
import os

st.title("Image2VideoApp")
st.write("Upload images to convert them into a video.")

uploaded_files = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
if uploaded_files:
    image_paths = []
    for file in uploaded_files:
        path = os.path.join("temp", file.name)
        os.makedirs("temp", exist_ok=True)
        with open(path, "wb") as f:
            f.write(file.getbuffer())
        image_paths.append(path)

    if st.button("Create Video"):
        clip = ImageSequenceClip(image_paths, fps=2)
        clip.write_videofile("output.mp4")
        st.success("Video created: output.mp4")
        with open("output.mp4", "rb") as f:
            st.download_button("Download Video", f, file_name="output.mp4")
