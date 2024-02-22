from flask import Flask, render_template, Response
import csv

app = Flask(__name__)

# Function to fetch SQL data (replace this with your actual SQL query)
def fetch_sql_data():
    # Example SQL data
    data = [
        {"id": 1, "name": "John", "age": 30},
        {"id": 2, "name": "Alice", "age": 25},
        {"id": 3, "name": "Bob", "age": 35}
    ]
    return data

# Route to handle the download request
@app.route('/download_sql_data')
def download_sql_data():
    # Fetch SQL data
    sql_data = fetch_sql_data()

    # Create a CSV string from SQL data
    csv_data = ','.join(sql_data[0].keys()) + '\n'
    for row in sql_data:
        csv_data += ','.join(str(val) for val in row.values()) + '\n'

    # Create a response with CSV data
    response = Response(csv_data, mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename="sql_data.csv")
    return response

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
