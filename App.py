from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/styles')
def styles():
    return render_template('styles.css'), 200, {'Content-Type': 'text/css'}

if __name__ == '__main__':
    print("🛒 Grocery List Manager Starting...")
    print("📍 Open your browser and go to: http://localhost:5000")
    print("Press CTRL+C to stop the server\n")
    app.run(debug=True, port=5000)