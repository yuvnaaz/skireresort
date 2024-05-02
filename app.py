# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from data import resorts_data  
from data2 import scrape_and_save  

app = Flask(__name__)
CORS(app) 


@app.route('/resorts')
def get_resorts_data():
    return jsonify(resorts_data)

@app.route('/scraped_content')
def get_scraped_content_data():
    content = scrape_and_save()
    return jsonify(content)

@app.route('/api_data')
def get_api_data_from_other_file():
    api_data = scrape_and_save
    return jsonify(api_data)

if __name__ == '__main__':
    app.run(debug=True)
