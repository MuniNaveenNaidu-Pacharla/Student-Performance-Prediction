from flask import Flask, render_template, request, redirect, url_for
from model import predict_result, generate_charts

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    attendance = int(request.form.get('attendance'))
    study_hours = int(request.form.get('study_hours'))
    internal_marks = int(request.form.get('internal_marks'))

    result = predict_result(attendance, study_hours, internal_marks)
    return render_template('result.html', result=result)

@app.route('/analysis', methods=['GET'])
def analysis():
    generate_charts()
    return render_template('analysis.html')

# 🔒 BLOCK direct access to /predict
@app.errorhandler(405)
def method_not_allowed(e):
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
