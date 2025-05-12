import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping

print("📥 Loading preprocessed data...")
X_train = np.load("../output/X_train.npy")
X_test = np.load("../output/X_test.npy")
y_age_train = np.load("../output/y_age_train.npy")
y_age_test = np.load("../output/y_age_test.npy")
y_gender_train = np.load("../output/y_gender_train.npy")
y_gender_test = np.load("../output/y_gender_test.npy")
print("✅ Data loaded.")

print("📦 Loading MobileNetV2...")
base_model = MobileNetV2(
    input_shape=(224, 224, 3), include_top=False, weights="imagenet"
)
base_model.trainable = False

print("🔧 Building multi-output model...")
x = base_model.output
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(128, activation="relu")(x)
x = layers.Dropout(0.3)(x)

# Two outputs
age_output = layers.Dense(1, name="age")(x)
gender_output = layers.Dense(1, activation="sigmoid", name="gender")(x)

model = models.Model(inputs=base_model.input, outputs=[age_output, gender_output])

model.compile(
    optimizer="adam",
    loss={"age": "huber", "gender": "binary_crossentropy"},
    metrics={"age": "mae", "gender": "accuracy"},
)

early_stop = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)

print("🚀 Training model...")
history = model.fit(
    X_train,
    {"age": y_age_train, "gender": y_gender_train},
    validation_data=(X_test, {"age": y_age_test, "gender": y_gender_test}),
    epochs=20,
    batch_size=32,
    callbacks=[early_stop],
)

print("💾 Saving model...")
model.save("../output/age_gender_model.h5")
print("✅ Model saved.")
