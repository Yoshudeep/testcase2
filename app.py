import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np

st.title("Real-time Webcam Feed with STUN")

class EmotionSpoofDetector:
    def __init__(self):
        # Initialize any models, variables, or state here
        pass
    
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")

        # Here, you can add your emotion detection or spoof detection logic.
        # For now, just draw a simple text on the frame as a placeholder.
        cv2.putText(img, "EmotionSpoofDetector running...", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Return the modified frame
        return av.VideoFrame.from_ndarray(img, format="bgr24")

RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
}

webrtc_streamer(
    key="emotion-spoof-stream",
    video_transformer_factory=EmotionSpoofDetector,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
    rtc_configuration=RTC_CONFIGURATION,
)
