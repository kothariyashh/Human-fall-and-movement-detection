import streamlit as st
from ultralytics import YOLO
import tempfile
import os
import cv2

class YOLOProcessor:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        
    def detect_fall(self, image):
        result = self.model.predict(image, conf=0.5)
        result_image = result[0].plot()
        result_image = cv2.cvtColor(result_image,cv2.COLOR_BGR2RGB)
        return result_image

    def process_video(self, input_path, output_path):
        vid = cv2.VideoCapture(input_path)
        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(vid.get(cv2.CAP_PROP_FPS))
        output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while vid.isOpened():
            ret, frame = vid.read()

            if ret:
                result = self.model.predict(frame, conf=0.5)
                processed_frame = result[0].plot()
                output.write(processed_frame)
            else:
                break

        vid.release()
        output.release()

