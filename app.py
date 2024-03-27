import streamlit as st
from PIL import Image
import os
from utils.yolo_processor import YOLOProcessor
import tempfile
import numpy as np 
import base64
import cv2 

processed_image = None
processed_video_path = None

def detect_fall(image, model_path):
    model = YOLOProcessor(model_path)
    result_image = model.detect_fall(image)
    return result_image

def main():
    global processed_image, processed_video_path

    st.title("Fall Detection with YOLO")
    st.markdown("---")
    option = st.sidebar.selectbox("Choose an option", ["Image", "Video"])

    if option == "Image":
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            st.markdown("---")
            st.subheader("Detecting Fall...")

            if processed_image is None:  # Process the image only if it hasn't been processed before
                with st.spinner('Detecting fall...'):
                    processed_image = detect_fall(image, "assets/best.pt")
            st.image(processed_image, caption='Result', use_column_width=True)

            # Download button for the result image
            if st.button('Download Result Image'):
                download_image(processed_image, filename='result_image.png')

    elif option == "Video":
        st.subheader("Upload Video")
        uploaded_file = st.file_uploader("Choose a video", type=["mp4"])

        if uploaded_file is not None:
            st.markdown("---")
            st.subheader("Processing and Detecting Fall...")

            temp_dir = tempfile.TemporaryDirectory()
            temp_file_path = os.path.join(temp_dir.name, "uploaded_video.mp4")
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.read())

            output_path = os.path.join(temp_dir.name, "processed_video.mp4")

            if processed_video_path is None:  
                with st.spinner('Processing and detecting fall...'):
                    yolo_processor = YOLOProcessor("assets/best.pt")
                    yolo_processor.process_video(temp_file_path, output_path)
                processed_video_path = output_path

            st.subheader("Result Video")
            st.video(processed_video_path)
            
            if st.button('Download Result Video'):
                download_file(processed_video_path, filename='processed_video.mp4')

            temp_dir.cleanup()

def download_image(image, filename):
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    image.save(filename)
    with open(filename, "rb") as f:
        image_bytes = f.read()
    b64 = base64.b64encode(image_bytes).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="{filename}">Click here to download {filename}</a>'
    st.markdown(href, unsafe_allow_html=True)

def download_file(file_path, filename):
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/mp4;base64,{b64}" download="{filename}">Click here to download {filename}</a>'
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

