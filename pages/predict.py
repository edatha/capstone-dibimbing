import streamlit as st
import requests
import io
from PIL import Image

from config import config

st.title("🖼️ Model Prediction")
st.divider()

# Upload Gambar
uploaded_file = st.file_uploader("Upload an image for segmentation", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Konversi gambar ke byte array
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format="JPEG")
    img_byte_array = img_byte_array.getvalue()
    
    # Kirim gambar ke FastAPI
    api_url = config["API_URL"]
    files = {"file": ("image.jpg", img_byte_array, "image/jpeg")}
    response = requests.post(api_url, files=files)
    
    if response.status_code == 200:
        img_result = Image.open(io.BytesIO(response.content))
        
        st.image(img_result, caption="Segmented Image", use_container_width=True)
    else:
        st.error("Failed to get prediction. Please try again.")
