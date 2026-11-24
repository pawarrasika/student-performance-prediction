import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_data.csv")

# Define input features and target
X = data[["Study_Hours", "Attendance", "Previous_Score", "Sleep_Hours",
          "Assignment_Average", "Practice_Tests"]]
y = data["Final_Score"]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Save trained model
joblib.dump(model, "student_model.pkl")

print("Training Completed")
print("Model saved as student_model.pkl")
