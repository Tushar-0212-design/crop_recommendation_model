import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib

# Load model and encoder
model = joblib.load("D:/E/2nd SEM/project EX/crop recomondetion/RF_crop_recomendation.pkl")
label_encoder = joblib.load("D:/E/2nd SEM/project EX/crop recomondetion/RF_label_encoder.pkl")

# Fixed parameter ranges
param_ranges = {
    "N": "(30–150)",
    "P": "(20–100)",
    "K": "(20–100)",
    "temp": "(10–32°C)",
    "hum": "(30–100%)",
    "ph": "(0–14)",
    "rain": "(50–250mm)"
}

# Predict function
def predict_crop():
    try:
        N = float(entry_N.get())
        P = float(entry_P.get())
        K = float(entry_K.get())
        temperature = float(entry_temp.get())
        humidity = float(entry_hum.get())
        ph = float(entry_ph.get())
        rainfall = float(entry_rain.get())

        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(input_data)
        crop = label_encoder.inverse_transform(prediction)[0]

        result_label.config(
            text=f"✅ Recommended Crop: {crop.capitalize()}",
            fg="green",
            font=("Arial", 14, "bold")
        )

    except ValueError:
        messagebox.showerror("Input Error", "❌ Please enter valid numbers in all fields.")

# Create window
root = tk.Tk()
root.title("🌿 Crop Recommendation System")
root.geometry("480x500")
root.configure(bg="#f0f8ff")

# Title
title_label = tk.Label(
    root, text="🌿 Crop Recommendation", font=("Arial", 18, "bold"),
    bg="#228B22", fg="white", pady=10
)
title_label.pack(fill="x")

# Frame for input fields
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)

fields = [
    ("Nitrogen (N)", "N"), ("Phosphorus (P)", "P"), ("Potassium (K)", "K"),
    ("Temperature (°C)", "temp"), ("Humidity (%)", "hum"),
    ("pH", "ph"), ("Rainfall (mm)", "rain")
]

entries = {}
for i, (label, key) in enumerate(fields):
    # Show label + range
    tk.Label(
        frame,
        text=f"{label} {param_ranges[key]}",
        font=("Arial", 12),
        bg="#f0f8ff"
    ).grid(row=i, column=0, sticky="w", padx=10, pady=5)

    # Entry box
    entry = tk.Entry(frame, font=("Arial", 12), width=10)
    entry.grid(row=i, column=1, pady=5, padx=5)
    entries[key] = entry

# Assign variables for easy access
entry_N, entry_P, entry_K, entry_temp, entry_hum, entry_ph, entry_rain = \
    entries["N"], entries["P"], entries["K"], entries["temp"], entries["hum"], entries["ph"], entries["rain"]

# Predict button
tk.Button(
    root, text="Predict Crop", font=("Arial", 14), bg="green",
    fg="white", command=predict_crop
).pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
result_label.pack(pady=10)

root.mainloop()
