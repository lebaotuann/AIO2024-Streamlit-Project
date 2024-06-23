import cv2
import numpy as np
import streamlit as st
from PIL import Image

from constants import DATA_DIRECTORY_PATH

MODEL = DATA_DIRECTORY_PATH + "/model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = DATA_DIRECTORY_PATH + "/model/MobileNetSSD_deploy.prototxt.txt"


class ObjectDetection:

    @staticmethod
    def process_image(image):
        """Processes an image for object detection using a MobileNet SSD model

        Args:
            image (np.ndarray): A NumPy array representing the image to be processed. Expected format is (height, width, channels) (e.g., RGB).
        Returns:
            np.ndarray: A list of dictionaries containing detection information.
        """
        blob = cv2.dnn.blobFromImage(
            cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
        )
        net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
        net.setInput(blob)
        detections = net.forward()
        return detections

    @staticmethod
    def annotate_image(image, detections, confidence_threshold=0.5):
        """Annotates an image with bounding boxes for detected objects.

        Args:
            image (np.ndarray): A NumPy array representing the image to be annotated. Expected format is (height, width, channels) (e.g., RGB).
            detections (np.ndarray): A list of dictionaries containing detection information.
            confidence_threshold (float): The minimum confidence score required for a detection to be included in the annotation (default: 0.5)

        Returns:
            np.ndarray: A new NumPy array representing the annotated image with bounding boxes. The format remains the same as the input image.
        """
        # loop over the detections
        h, w = image.shape[:2]
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > confidence_threshold:
                # extract the index of the class label from the 'detections',
                # then compute the (x, y)-coordinates of the bounding box for the object
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(image, (startX, startY), (endX, endY), 70, 2)
        return image

    def run(self):
        """Run object detections"""
        st.title("Object Detection for Images")
        file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        if file is not None:
            st.image(file, caption="Uploaded Image")
            image = Image.open(file)
            image = np.array(image)
            try:
                detections = self.process_image(image)
                processed_image = self.annotate_image(image, detections, 0.7)
                st.image(processed_image, caption="Processed Image")
            except Exception:
                st.text("Cannot detect the object.")


if __name__ == "__main__":
    ObjectDetection().run()
