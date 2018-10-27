# flaskfib

Clone the project and install the dependencies using :

```sh
git clone git@github.com:neilrichter/flaskfib.git; pip install -r ./requirements.txt;
```

Run the server with

```sh
./app.py
```

Test the x<sup>nth</sup> number in the Fibonacci number by running
```sh
curl -X GET http://127.0.0.1:8000/fib/x
```

Example : 
```sh
curl -X GET http://127.0.0.1:8000/fib/13
377
```