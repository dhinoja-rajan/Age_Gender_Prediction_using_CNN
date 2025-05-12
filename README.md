# 🧠 Age and Gender Prediction Project using CNN, FastAPI, and Streamlit

---

## 📁 Project Structure

```
📁 Age-Gender-Prediction-Project (Root)
│
├── 📂 backend         → FastAPI backend server
│   └── main.py
│
├── 📂 frontend        → Streamlit frontend interface
│   └── app.py
│
├── 📂 model           → Training and preprocessing scripts
│   ├── preprocess.py
│   └── train_model.py
│
├── 📂 output          → Model and .npy dataset files
│   ├── age_gender_model.h5
│   ├── pretrained_age_model.h5
│   ├── X_train.npy, X_test.npy
│   ├── y_age_train.npy, y_age_test.npy
│   ├── y_gender_train.npy, y_gender_test.npy
│
├── requirements.txt
└── README.md
```

---

## ✅ Step-0: Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔹 Step 1: Dataset Collection & Preprocessing

### Tasks:

✅ Load images  
✅ Resize to (224x224)  
✅ Normalize  
✅ Extract age and gender  
✅ Train-test split

📂 Script: `model/preprocess.py`

```
cd model
python preprocess.py
```

### Output:

- ✅ Image samples previewed
- ✅ Preprocessed data saved to `output/`:
  - `X_train.npy`, `X_test.npy`
  - `y_age_train.npy`, `y_age_test.npy`
  - `y_gender_train.npy`, `y_gender_test.npy`

---

## 🔹 Step 2: Train the CNN Model

### Tasks:

✅ Define a CNN for dual output  
✅ Train on preprocessed data  
✅ Save model

📂 Script: `model/train_model.py`

```
cd model
python train_model.py
```

### Output:

- ✅ Training progress printed
- ✅ Model saved as `output/age_gender_model.h5`

---

## 🔹 Step 3: Backend with FastAPI

📂 File: `backend/main.py`

```
cd backend
uvicorn main:app --reload
```

### API Test(Postman):

- Endpoint: `POST http://127.0.0.1:8000/predict`
- Form-data:
  - Key: `file` (type: File)
- Returns:

```json
{
  "predicted_age": 26,
  "predicted_gender": "Female"
}
```

---

## 🔹 Step 4: Frontend with Streamlit

📂 File: `frontend/app.py`

```
cd frontend
streamlit run app.py
```

### Output:

- ✅ Upload an image
- ✅ See predicted **Age** and **Gender** displayed

---

## ✅ Final Notes

- Model trained on UTKFace
- Prediction includes both age (regression) and gender (classification)
- Data and models saved in `output/` directory
