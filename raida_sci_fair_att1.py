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

def filter_data(df, **demographics):
    """
    Filter the DataFrame based on provided demographic information.

    Args:
    df (DataFrame): The original DataFrame.
    demographics (dict): Key-value pairs of demographics to filter by.

    Returns:
    DataFrame: Filtered DataFrame based on the given demographics.
    """
    filtered_df = df
    for key, value in demographics.items():
        if key in filtered_df.columns:
            filtered_df = filtered_df[filtered_df[key] == value]
    return filtered_df

def aggregate_and_plot(df, demographics):
    """
    Aggregate mood metrics based on the difference between eat-time and sleep time,
    and plot the results for the given demographics.

    Args:
    df (DataFrame): The original DataFrame.
    demographics (dict): Key-value pairs of demographics to filter by.
    """
    filtered_df = filter_data(df, **demographics)

    mood_metrics_columns = ['wakefulness', 'happiness', 'energized-drained', 'active-inactive', 'attentive']
    filtered_df = filtered_df[['Difference between eat time and sleep time'] + mood_metrics_columns]

    # compute mean timeframe between dinner time and bed time 
    grouped_df = filtered_df.groupby('Difference between eat time and sleep time').mean()

    # plot data
    ax = grouped_df.plot(kind='bar', figsize=(10, 6))
    ax.set_xlabel('Difference between eat time and sleep time')
    ax.set_ylabel('Mood Metrics (Average Score)')
    ax.set_title('Mood Metrics vs. Difference between Eat-Time and Sleep Time')

    plt.show()

# ONLY EDIT THIS LINE
aggregate_and_plot(df, {'Gender': 'Male', 'Age': 20, 'Common eating & sleeping patterns?': 'Yes'})

# aggregate_and_plot(df, {'Gender': 'Male', 'Age': 20, 'Common eating & sleeping patterns?': 'Yes'}) -> if you accidentally mess up the line, use this one

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Here you should use your filtering and plotting logic
    # For example, you would call aggregate_and_plot or similar function
    # and get the plot data back as a dictionary
    demographics = data  # Assuming data is a dictionary with the right keys
    plot_data = your_function_to_get_plot_data(demographics)
    
    return jsonify(plot_data)

if __name__ == '__main__':
    app.run(debug=True)

