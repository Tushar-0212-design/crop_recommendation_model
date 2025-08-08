import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import joblib

# Load dataset
data = pd.read_csv("D:/E/2nd SEM/project EX/crop recomondetion/Crop_recommendation.csv")  # Replace with your actual CSV file name

# Features and Target
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = data['label']

# Encode target labels (crops)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Predict on test set
y_pred_rf = rf_model.predict(X_test)

# Accuracy and classification report
print("✅ Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print("📋 Classification Report:\n", classification_report(y_test, y_pred_rf, target_names=le.classes_))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_rf)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
disp.plot(cmap='Blues', xticks_rotation=90)
plt.tight_layout()
plt.show()

# Save model and label encoder
#joblib.dump(rf_model, "RF_crop_recomendation.pkl")
#joblib.dump(le, "label_encoder_RF.pkl")

print("✅ Model and label encoder saved successfully.")
