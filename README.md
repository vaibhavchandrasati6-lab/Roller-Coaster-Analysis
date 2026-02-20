# 🎢 Roller Coaster Data Analysis (EDA Project)

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a roller coaster dataset to uncover patterns and relationships between different coaster characteristics such as **speed, height, inversions, G-force, and year of introduction**.

The goal of this project is to practice real-world data analysis using Python and visualization libraries while deriving meaningful insights from the dataset.

---

## 🎯 Objectives

* Clean and preprocess the dataset
* Handle missing values and duplicates
* Perform exploratory data analysis (EDA)
* Visualize relationships between important coaster features
* Identify trends in coaster development over time

---

## 🗂 Dataset Information

The dataset contains information about roller coasters including:

* Coaster Name
* Location
* Manufacturer
* Year Introduced
* Opening Date
* Speed (mph)
* Height (ft)
* Number of Inversions
* G-force
* Type of Coaster
* Latitude & Longitude

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 🧹 Data Cleaning Steps

The following preprocessing steps were performed:

* Selected relevant columns
* Renamed columns for better readability
* Converted date columns into datetime format
* Checked and handled missing values
* Removed duplicate records based on coaster name, location, and opening date

---

## 📊 Exploratory Data Analysis

The following visualizations were created:

1. Distribution of coaster speeds
2. Top years with highest coaster introductions
3. Height vs Speed relationship (scatter plot)
4. Height vs Speed with year differentiation
5. Pairplot for multi-variable relationships
6. Correlation heatmap between numerical features

---

## 🔍 Key Insights

* Taller roller coasters generally tend to have higher speeds.
* There is a positive correlation between **height** and **speed**.
* Coasters with more inversions often experience higher G-forces.
* Certain years show spikes in coaster introductions, indicating industry growth periods.
* Different coaster types show variations in physical characteristics.

---

## 📁 Project Structure

```
roller-coaster-analysis/
│
├── coaster.csv
├── coaster_analysis.py
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run the Project

1. Clone this repository:

```
git clone https://github.com/vaibhavchandrasati6-lab/roller-coaster-analysis.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the script:

```
python coaster_analysis.py
```



---

## 📈 Future Improvements

* Add more advanced visualizations
* Perform statistical hypothesis testing
* Build a machine learning model to predict coaster speed or G-force
* Create an interactive dashboard using Plotly or Power BI

---

## 👨‍💻 Author

**Vaibhav Chandra Sati**


If you found this project useful, feel free to ⭐ the repository.

---
