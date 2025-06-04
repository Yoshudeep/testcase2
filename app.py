import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("Real-time Webcam Feed with STUN")

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(img, format="bgr24")

RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
}

webrtc_streamer(
    key="emotion-spoof-stream",
    video_transformer_factory=EmotionSpoofDetector,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
