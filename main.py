#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fib/<int:x>')
def fib(x):
	a, b = 0, 1
	for i in range(x):
		temp = b
		b += a
		a = temp
	return jsonify(b)

app.run(port=8000, use_reloader=True, load_dotenv=True)