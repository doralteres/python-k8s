from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World!"


@app.post("/avg")
def avarage():
    numbers = request.get_json()["numbers"]  # example [3,5,6,20]
    # ... Calculate Avarage
    # return avarage


@app.post("/min")
def minimum():
    numbers = request.get_json()["numbers"]  # example [3,5,6,20]
    # ... Calculate minimum
    # return minimum


@app.post("/max")
def maximum():
    numbers = request.get_json()["numbers"]  # example [3,5,6,20]
    # ... Calculate maximum
    # return maximum


if __name__ == "__main__":
    app.run()
