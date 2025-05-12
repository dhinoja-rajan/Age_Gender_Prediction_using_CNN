from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image, ImageOps
from io import BytesIO

app = FastAPI()
model = load_model("../output/age_gender_model.h5")
IMG_SIZE = (224, 224)


def preprocess_image(image_bytes):
    try:
        img = Image.open(BytesIO(image_bytes)).convert("RGB")
        img = ImageOps.exif_transpose(img)  # ⬅️ FIX: Correct orientation using EXIF
    except Exception as e:
        print("❌ Error opening image:", e)
        raise
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array.astype(np.float32), axis=0)


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = preprocess_image(contents)
    age, gender = model.predict(img)
    gender_label = "Female" if gender[0][0] >= 0.8 else "Male"
    return {
        "predicted_age": round(float(age[0][0]), 2),
        "predicted_gender": gender_label,
    }
