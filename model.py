import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


data = pd.read_csv("student_data.csv")

X = data[['attendance', 'study_hours', 'internal_marks']]
y = data['result']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

def predict_result(attendance, study_hours, internal_marks):
    prediction = model.predict([[attendance, study_hours, internal_marks]])
    return "PASS" if prediction[0] == 1 else "FAIL"
import matplotlib.pyplot as plt
import os

def generate_charts():
    os.makedirs("static/charts", exist_ok=True)

    
    data['result'].value_counts().plot(kind='bar')
    plt.title("Pass vs Fail")
    plt.savefig("static/charts/pass_fail.png")
    plt.clf()

    
    plt.scatter(data['study_hours'], data['internal_marks'])
    plt.xlabel("Study Hours")
    plt.ylabel("Internal Marks")
    plt.title("Study Hours vs Marks")
    plt.savefig("static/charts/study_marks.png")
    plt.clf()
