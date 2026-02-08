# Student Performance Prediction System 🎓

A Machine Learning–based web application that predicts whether a student will **PASS or FAIL** based on academic and behavioral parameters such as attendance, study hours, and internal marks.

The system uses a Logistic Regression model and is deployed as a web app using Flask, allowing users to input student data and instantly view predictions along with basic data analysis visualizations.

---

## Features
- Predicts student result (PASS / FAIL)
- Machine Learning model trained using real student data
- User-friendly web interface built with Flask
- Data visualization for performance analysis
- Clean and modular code structure

---

## Tech Stack
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Visualization:** Matplotlib  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS  

---

## Machine Learning Workflow
1. Data loading and preprocessing
2. Feature selection
3. Train–test split
4. Model training using Logistic Regression
5. Prediction and evaluation
6. Visualization of insights

---

## Input Parameters
- Attendance percentage
- Study hours per day
- Internal assessment marks

---

## Output
- Predicted result: **PASS / FAIL**
- Visual charts:
  - Pass vs Fail distribution
  - Study hours vs Internal marks

---

## How to Run the Project
```bash
pip install pandas scikit-learn flask matplotlib
python app.py