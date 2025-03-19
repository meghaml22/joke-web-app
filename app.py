from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why was the math book sad? Because it had too many problems.",
    "I told my computer I needed a break, and it said 'No problem, I’ll go to sleep.'",
    "Why don’t programmers like nature? It has too many bugs.",
    "What did the router say to the Wi-Fi? You complete me.",
    "Debugging: Removing the needles from the haystack."
]

@app.route('/')
def index():
    return render_template("index.html")
# 123
# absch
# hgsdfd

@app.route('/joke')
def get_joke():
    return jsonify({'joke': random.choice(jokes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
