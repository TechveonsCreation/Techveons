from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)
HTML_FILE = os.path.join(app.root_path, 'techveons (4).html')

@app.route('/send', methods=['POST'])
def send():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        print(f"Message received from {name} ({email}): {message}")

        return jsonify({"message": "success"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"message": "error"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    return send_file(HTML_FILE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    app.run(debug=True)