import os
import glob
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_latest_csv(folder_path):
    # Get a list of all CSV files in the folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    if not csv_files:
        return None  # Return None if no CSV files are found
    
    # Sort files by their modification time
    latest_file = max(csv_files, key=os.path.getmtime)
    return latest_file

@app.route("/")
def index():
    # The path to the folder containing your CSV files
    folder_path = "\Attendance"  # Replace with the actual path to your folder
    
    # Get the latest CSV file
    latest_csv = get_latest_csv(folder_path)
    
    if not latest_csv:
        return "No CSV files found in the folder."
    
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(latest_csv)
        # Convert the DataFrame to a list of dictionaries
        data = df.to_dict(orient="records")
        return render_template("table.html")
    except Exception as e:
        return f"Error reading the CSV file: {str(e)}"

@app.route("/data")
def data():
    # The path to the folder containing your CSV files
    folder_path = "/Attendance"  # Replace with the actual path to your folder
    
    latest_csv = get_latest_csv(folder_path)
    
    if not latest_csv:
        return jsonify([])  # Return an empty list if no CSV file is found
    
    try:
        df = pd.read_csv(latest_csv)
        data = df.to_dict(orient="records")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
