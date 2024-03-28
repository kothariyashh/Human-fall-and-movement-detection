# Fall Detection using YOLO with Streamlit Interface

## Description:
The main goal of this research is to create a system that can recognize falls in pictures and movies automatically. Such fall detection systems can be useful in many different applications, such as security surveillance, healthcare monitoring, senior care, and more. The system can instantly detect falls and initiate appropriate responses to guarantee people's safety and well-being.

## Functionality:

Image and Video Fall Detection: Users can upload either an image or a video file.

Automatic Detection: The uploaded image or video undergoes automatic fall detection using the YOLO object detection model.

User Interface: Streamlit provides an intuitive and interactive interface where users can seamlessly upload files and view the results.

Result Presentation: Detected falls are highlighted in the output, providing visual cues to the user.

Download Option: Users have the option to download the processed image or video for further analysis or storage.

## Installation:
List the dependencies required to run your project. For example:
- numpy
- opencv-python
- Pillow
- streamlit
- ultralytics
- dill

Install the required dependencies by running the following command in the terminal:

    pip install -r requirements.txt


## Usage:
Explain how to use your application. Provide step-by-step instructions if necessary. Mention the options available (Image or Video) and how users can upload files for fall detection.

## Run the Streamlit app:

    streamlit run app.py

Choose between detecting a fall in an image or a video, and follow the on-screen instructions to upload the file and view the results.

## File Structure:
Briefly describe the structure of your project's files and directories. 
For example

├── app.py

├── utils

│   └── yolo_processor.py

├── assets

│   └── best.pt

└── README.md

## Credits:
Give credit to any external libraries, resources, or datasets you've used in your project.

# SCREENSHOTS:

![image](https://github.com/kothariyashh/Human-fall-and-movement-detection/assets/95516314/5701fd7e-27c1-48fb-9935-d4464c5cd5d1)

![image](https://github.com/kothariyashh/Human-fall-and-movement-detection/assets/95516314/1838f618-b3bb-4c2c-9883-bf43c456b745)

![image](https://github.com/kothariyashh/Human-fall-and-movement-detection/assets/95516314/b421317a-2c3e-439e-8ccd-09f9d63047d1)





