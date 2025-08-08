#  Crop Recommendation Using Machine Learning

##  Overview
Agriculture plays a crucial role in the Indian economy, and selecting the right crop is essential for maximizing yield and sustainability.  
This project uses **Machine Learning** to recommend the most suitable crop for cultivation based on **soil and environmental parameters** such as Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.

##  Purpose
The goal is to build an **intelligent crop recommendation system** that provides accurate suggestions using real-time data, helping farmers make informed decisions and improve productivity.

##  Objectives
- Develop a machine learning model for crop recommendation.
- Compare multiple ML models and select the most accurate one.
- Create a **Tkinter GUI** for user-friendly interaction.
- Provide recommendations among **22 crop types**.

##  Technology Stack

### **Software**
- **Front-end:** Python (Tkinter)
- **Back-end:** Naive Bayes Classifier (Random Forest also tested)
- **Programming Language:** Python
- **Libraries:** `scikit-learn`, `pandas`, `numpy`, `tkinter`
- **OS:** Windows 11

### **Hardware**
- **Processor:** AMD Ryzen 7 5800HS @ 3.20 GHz
- **RAM:** 16 GB

##  Features
### **Admin Module**
- Train and update ML models.
- Compare performance metrics (Accuracy, F1 Score, Precision, Recall, Training Time).
- View and manage prediction history.

**Model Performance:**
| Model               | Accuracy | F1 Score | Precision | Recall | Training Time (s) |
|---------------------|----------|----------|-----------|--------|-------------------|
| Naive Bayes         | 0.9955   | 0.9954   | 0.9958    | 0.996  | 0.0051            |
| Random Forest       | 0.9932   | 0.9932   | 0.9937    | 0.993  | 0.6674            |
| Decision Tree       | 0.9841   | 0.9841   | 0.9845    | 0.984  | 0.0260            |
| SVM                 | 0.9682   | 0.9680   | 0.9715    | 0.968  | 0.1327            |
| Logistic Regression | 0.9636   | 0.9635   | 0.9644    | 0.964  | 0.1151            |
| KNN                 | 0.9568   | 0.9567   | 0.9629    | 0.957  | 0.0421            |

**Selected Models:** Naive Bayes & Random Forest (best accuracy and low training time)

### **User Module**
- Input soil & weather parameters.
- Get instant crop recommendations.

##  Dataset Description
| Feature     | Description |
|-------------|-------------|
| N           | Nitrogen level in soil |
| P           | Phosphorus level in soil |
| K           | Potassium level in soil |
| Temperature | Avg. temperature (°C) |
| Humidity    | Relative humidity (%) |
| pH          | Soil pH level |
| Rainfall    | Rainfall (mm) |
| Label       | Recommended crop (e.g., rice, maize, etc.) |

##  Process Flow
1. **User inputs** environmental parameters.
2. ML model processes data.
3. **Crop recommendation** is displayed in GUI.
4. Data stored for future reference.
