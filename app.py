#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/fib/<int:x>')
def fib(x):
	a, b = 0, 1
	for _ in range(x):
		a, b = b, a+b
	return str(b)

if __name__ == '__main__':
	app.run(port=8000)