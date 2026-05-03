# 🏥 HealthSight: Chronic Disease Prediction & EHR Analysis

---

## 📌 **Project Overview**

**HealthSight** is a data analytics project focused on analyzing healthcare data to identify patterns and risk factors associated with **Chronic Kidney Disease (CKD)**.

The project leverages **data cleaning, exploratory data analysis (EDA), and statistical insights** to support early disease detection and improve decision-making in healthcare systems.

---

## 🎯 **Objective**

* Analyze Electronic Health Records (EHR)-like data
* Identify key medical indicators influencing CKD
* Generate actionable insights for early diagnosis
* Build a strong foundation for predictive modeling (future scope)

---

## 📂 **Dataset**

* **Source:** UCI Machine Learning Repository (CKD Dataset)
* **Type:** Structured healthcare dataset
* **Features include:**

  * Age
  * Blood Pressure (bp)
  * Blood Glucose (bgr)
  * Serum Creatinine (sc)
  * Hemoglobin (hemo)
  * Albumin (al), Sugar (su)
  * Target: **classification (CKD / Not CKD)**

---

## 🛠️ **Tech Stack**

* **Python** 🐍
* **Pandas & NumPy** → Data Processing
* **Matplotlib & Seaborn** → Data Visualization
* **Jupyter Notebook** → Analysis Workflow
* **Git & GitHub** → Version Control

---

## ⚙️ **Project Workflow**

### 🔹 **Week 1: Data Preparation**

* Loaded raw dataset
* Handled missing values (`? → NaN`)
* Performed data cleaning
* Converted incorrect data types
* Applied:

  * Median imputation (numerical features)
  * Mode imputation (categorical features)
* Encoded target variable (`ckd = 1`, `notckd = 0`)

---

### 🔹 **Week 2: Exploratory Data Analysis (EDA)**

* Distribution analysis of medical features
* Target variable analysis (CKD vs Non-CKD)
* Correlation heatmap
* Feature vs target comparisons using boxplots
* Identification of key biomarkers

---

## 📊 **Key Insights**

* 📈 **Serum Creatinine** shows strong positive correlation with CKD
* 📉 **Hemoglobin levels** are significantly lower in CKD patients
* ⚠️ **Blood Glucose** levels are higher in CKD cases
* 🔍 Blood Pressure shows noticeable variation between groups
* 📊 Dataset shows moderate class imbalance

---

## 📁 **Project Structure**

```
HealthSight/
│
├── data/
│   ├── raw/            # Original dataset
│   └── cleaned/        # Processed dataset
│
├── notebooks/
│   └── Week1_Week2.ipynb
│
├── README.md
```

---

## 🚀 **Future Scope**

* Build machine learning models (Logistic Regression, Random Forest)
* Evaluate model performance (Accuracy, Recall, ROC-AUC)
* Develop interactive dashboard (Power BI / Tableau)
* Expand to multi-disease prediction

---

## ⚠️ **Data Ethics & Privacy**

* Dataset is fully anonymized
* No personal or sensitive patient data used
* Project follows ethical data handling practices

---

## 👨‍💻 **Author**

**Rohit Ranjan**
Aspiring Data Analyst

---

## ⭐ **Conclusion**

This project demonstrates a complete **data analytics pipeline (cleaning → EDA → insights)** applied to a real-world healthcare problem, showcasing strong analytical and problem-solving skills.

---
