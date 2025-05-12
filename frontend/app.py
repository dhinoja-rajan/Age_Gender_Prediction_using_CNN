import streamlit as st
import requests
from PIL import Image, ImageOps

st.set_page_config(page_title="Age & Gender Prediction")
st.title("🧠 Age & Gender Prediction App")

st.markdown("Upload a face image below:")

file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"]
)

if file:
    image = Image.open(file)
    image = ImageOps.exif_transpose(image)  # ⬅️ FIX: Correct orientation using EXIF
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Sending to model..."):
            res = requests.post(
                "http://127.0.0.1:8000/predict/", files={"file": file.getvalue()}
            )
            if res.status_code == 200:
                result = res.json()
                st.success(f"🎯 Age: {result['predicted_age']} years")
                st.success(f"👤 Gender: {result['predicted_gender']}")
            else:
                st.error("❌ Failed to connect to backend.")
