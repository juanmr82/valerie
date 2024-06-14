from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


# Render the HTML template with the calendar and notify button
@app.route('/')
def index():
    return render_template('index.html')


# Handle POST request to notify endpoint
@app.route('/api/date/notify', methods=['POST'])
def notify_date():
    date = request.json.get('date')

    # Make a POST request to NTFY Topic valerie-date
    url = 'https://ntfy.sh/valerie-date'
    payload = f"Valerie woudl like to go on a date on {date}"

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        return jsonify({'message': 'Juan has been notified'}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
