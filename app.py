from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from model import predict_nutrition, calculate_calories

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    age = data.get('age')
    weight = data.get('weight')
    height = data.get('height')
    gender = data.get('gender')
    activity = data.get('activity')
    meals = data.get('plan')

    predicted_nutrition = predict_nutrition(age, weight, height, gender, activity, meals)

    total_calories = calculate_calories(predicted_nutrition['protein'], 
                                         predicted_nutrition['fat'], 
                                         predicted_nutrition['carbs'])

    response = {
        'breakfast': predicted_nutrition['meals']['breakfast'],
        'lunch': predicted_nutrition['meals']['lunch'],
        'dinner': predicted_nutrition['meals']['dinner'],
        'total_calories': total_calories
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)