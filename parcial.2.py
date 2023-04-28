from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_excel('data.xlsx')
records = df.to_dict(orient='records')

@app.route('/records', methods=['GET'])
def get_records():
    country = 'Panama'
    indicator = 'Indicator'

    filtered_records = [record for record in records if record['Country Name'] == country and record['Indicator'] == indicator]

    return jsonify(filtered_records)

if __name__ == '__main__':
    app.run(debug=True)
