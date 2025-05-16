import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split


def parse_filename(filename):
    parts = filename.split("_")
    age = int(parts[0])
    gender = int(parts[1])  # 0: Male, 1: Female
    return age, gender


print("🔄 Starting preprocessing...")
IMG_SIZE = (224, 224)
dataset_path = "D:/AI ENGINEERING/Datasets/CNN/UTKFace_Age_Gender"
images, ages, genders = [], [], []

files = os.listdir(dataset_path)
print(f"📂 Found {len(files)} files.")

MAX_IMAGES = 15000  # Limit for memory efficiency

for i, file in enumerate(files):
    if file.endswith(".jpg") and i < MAX_IMAGES:
        try:
            age, gender = parse_filename(file)
            path = os.path.join(dataset_path, file)
            img = cv2.imread(path)
            if img is not None:
                img = cv2.resize(img, IMG_SIZE)
                img = img / 255.0
                images.append(img)
                ages.append(age)
                genders.append(gender)
        except Exception as e:
            print(f"⚠️ Skipping {file}: {e}")

X = np.array(images, dtype=np.float32)
y_age = np.array(ages, dtype=np.float32)
y_gender = np.array(genders, dtype=np.float32)

print("✅ Loaded and processed images.")

X_train, X_test, y_age_train, y_age_test, y_gender_train, y_gender_test = (
    train_test_split(X, y_age, y_gender, test_size=0.2, random_state=42)
)

os.makedirs("../output", exist_ok=True)
np.save("../output/X_train.npy", X_train)
np.save("../output/X_test.npy", X_test)
np.save("../output/y_age_train.npy", y_age_train)
np.save("../output/y_age_test.npy", y_age_test)
np.save("../output/y_gender_train.npy", y_gender_train)
np.save("../output/y_gender_test.npy", y_gender_test)

print("📁 Data saved in 'output/' folder.")
print("✅ Preprocessing complete.")
