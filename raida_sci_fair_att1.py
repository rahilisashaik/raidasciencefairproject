import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import os
import uuid

from flask import Flask, jsonify, request

app = Flask(__name__)


csv_path = 'form_responses_updated.csv'  
raw_data = pd.read_csv(csv_path)


df = pd.read_csv('form_responses_updated.csv')

def predict():
    data = request.json
    demographics = {
        'Gender': data['gender'],
        'Age': int(data['age']),
        'Common eating & sleeping patterns?': data['patterns']
    }
    
    filtered_df = filter_data(df, **demographics)
    
    # Instead of plotting, aggregate the data and convert to JSON
    mood_metrics = ['wakefulness', 'happiness', 'energized-drained', 'active-inactive', 'attentive']
    mean_scores = filtered_df[mood_metrics].mean().to_dict()
    
    # Return the mean scores as JSON
    return jsonify(mean_scores)



def filter_data(df, **demographics):
    filtered_df = df
    for key, value in demographics.items():
        if key in filtered_df.columns and value != '':
            filtered_df = filtered_df[filtered_df[key] == value]
    return filtered_df


# ONLY EDIT THIS LINE
# aggregate_and_plot(df, {'Gender': 'Male', 'Age': 20, 'Common eating & sleeping patterns?': 'Yes'})
# aggregate_and_plot(df, {'Gender': 'Male', 'Age': 20, 'Common eating & sleeping patterns?': 'Yes'}) -> if you accidentally mess up the line, use this one

if __name__ == '__main__':
    app.run(debug=True)

