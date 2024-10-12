from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Inserted Nutritionix API ID and Key
API_ID = "835aeed3"
API_KEY = "7e2d630ff7f3cef0fd96527937d259b5"

# Nutritionix API endpoint
url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and display results
@app.route('/analyze', methods=['POST'])
def analyze():
    food_item = request.form['food']
    
    headers = {
        "x-app-id": API_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    data = {
        "query": food_item,
        "timezone": "US/Eastern"  # Adjust the timezone if necessary
    }
    
    response = requests.post(url, headers=headers, json=data)
    nutrition_info = response.json() if response.status_code == 200 else None
    
    return render_template('results.html', nutrition=nutrition_info, food_item=food_item)

if __name__ == '__main__':
    app.run(debug=True)
