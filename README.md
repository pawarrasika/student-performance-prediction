# 🎓 Student Performance Prediction

## 📌 Project Overview
Student Performance Prediction is a Machine Learning project that predicts a student's final examination score based on academic and personal study-related parameters.

The project uses **Linear Regression**, a supervised machine learning algorithm, to estimate student performance. A simple and interactive web application is developed using Streamlit, where users can enter student details and receive a predicted score.

## 🎯 Project Objectives
- Predict students' final examination scores.
- Understand the relationship between study habits and academic performance.
- Perform Exploratory Data Analysis (EDA) using Python.
- Build and evaluate a Machine Learning model.
- Develop an interactive web application using Streamlit.

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib
- **Machine Learning:** Scikit-learn
- **Algorithm:** Linear Regression
- **Model Saving:** Joblib
- **Frontend:** Streamlit
- **Development Environment:** Jupyter Notebook, VS Code

## 📂 Project Structure

```text
Student-Performance-Prediction/
│
├── app.py
├── demo.py
├── student_data.csv
├── student_model.pkl
├── Student_Performance.ipynb
└── README.md
```

## 📊 Dataset Description

The project uses a sample synthetic dataset containing 1,000 student records and 10 columns.

### Input Features Used for Prediction

| Feature | Description |
|---|---|
| Study_Hours | Daily study hours |
| Attendance | Attendance percentage |
| Previous_Score | Previous examination score |
| Sleep_Hours | Daily sleeping hours |
| Assignment_Average | Average assignment percentage |
| Practice_Tests | Number of practice tests per month |

**Target Variable:** `Final_Score`

Other dataset columns include Internet_Access, Parent_Education, and Extracurricular. These are available for analysis but are not used by the current prediction model.

## 🔍 Exploratory Data Analysis (EDA)

The Jupyter Notebook includes:
- Dataset loading and inspection.
- Checking dataset shape and data types.
- Statistical summary using `describe()`.
- Checking missing values using `isnull().sum()`.
- Calculating average and maximum final scores.
- Grouping student performance by parent education.
- Histogram for final score distribution.
- Scatter plot for study hours vs final score.
- Scatter plot for attendance vs final score.

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values.

### Model Workflow
1. Load the dataset.
2. Select input features and target variable.
3. Split the dataset into training and testing sets.
4. Train the Linear Regression model.
5. Predict student scores.
6. Evaluate model performance.
7. Save the trained model using Joblib.

### Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score (Coefficient of Determination)

## 🌐 Streamlit Web Application

The Streamlit application allows users to:
- Enter study hours.
- Enter attendance percentage.
- Enter previous examination score.
- Enter sleep hours.
- Enter assignment average.
- Enter practice tests per month.
- Click the Predict button.
- View the estimated final examination score.

## ⚙️ Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/pawarrasika/student-performance-prediction.git
```

### Step 2: Open the Project Folder

```bash
cd student-performance-prediction
```

### Step 3: Install Required Libraries

```bash
python -m pip install pandas numpy matplotlib scikit-learn streamlit joblib jupyter
```

### Step 4: Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

### Step 5: Run the Jupyter Notebook

```bash
jupyter notebook
```

Open `Student_Performance.ipynb` and execute the cells in order.

### Optional: Train and Save the Model Again

```bash
python demo.py
```

This trains the Linear Regression model using the dataset and saves it as `student_model.pkl`.

## 📈 Key Learning Outcomes
- Practical experience with Python and Pandas.
- Understanding of data exploration and visualization.
- Understanding supervised machine learning.
- Implementation of Linear Regression.
- Model evaluation using regression metrics.
- Saving and loading ML models using Joblib.
- Building a web application using Streamlit.
- Managing a project using Git and GitHub.

## ⚠️ Disclaimer
This project uses synthetic sample data for educational and demonstration purposes. Predictions are estimates and should not be treated as actual academic assessments.

## 👩‍💻 Author
**Rasika Pawar**

GitHub: [pawarrasika](https://github.com/pawarrasika)

---

⭐ If you find this project useful, consider giving the repository a star!
