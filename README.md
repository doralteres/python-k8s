# Coding, Docker & K8S

Hello!
We are going to create a Math server Using python flask api than, wrap it in a docker image and k8s objects. Please follow the steps:

## 1. Build the Math API

- Init new python3.8+ project using [virtualenv](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) and dependencies list under [requirement.txt](https://learnpython.com/blog/python-requirements-file/) file.
- Install [Flask](https://flask.palletsprojects.com)
  ```shell
  pip install flask
  ```
- Create `index.py` file with hello world route:

  ```python
  from flask import Flask

  app = Flask(__name__)


  @app.route("/")
  def helloworld():
      return "Hello World!"


  if __name__ == "__main__":
      app.run()

  ```

- Check everything is working by running thr app and check the response of http://localhost:5000:

  ```shell
  python ./index.py
  ```

- Add to `index.py` file 3 new POST requests:

  - `/avg` - returns the avarage of the numbers.
  - `/min` - returns the min number from the list.
  - `/max` - returns the max number from the list.

  Request body in all the requests is a JSON object with number key and list of numbers as a value.

  ```json
  {
    "numbers": [2, 4, 5, 34, 22, 1]
  }
  ```

  copy this code to your `index.py` and compete the calculation code

  ```python
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

  ```

- Check everything is working by running thr app and check the response of:
  - POST http://localhost:5000/avg
  - POST http://localhost:5000/min
  - POST http://localhost:5000/max

## Packaging & Dockerfile

- install [gunicorn](https://flask.palletsprojects.com/en/3.0.x/deploying/gunicorn/)
- check if your app is working using gunicorn command (visit http://localhost:8000 and check your app is successfully run)

  ```shell
  gunicorn 'index:app'
  ```

- Create a Dockerfile from `python:3.9.18-slim` base image that copy your code, install dependencies from your `requirements.txt` file using pip, and run the app using gunicorn.
  > HINT: to make gunicorn works inside docker image you should add `-b 0.0.0.0:8000` argument
- **BONUS**: make sure the image is running with non-root user.

## Kubernetes

- Create **deployment** and **service** objects to your math api
- Answer to the following questions:
  - What is the differences between `Deployment` to `StatefulSet` to `DaemonSet`?
  - What is the differences between service types `ClusterIp` to `NodePort`?
  - Give 3 advantages of using helm charts.
- **BONUS:** Build a new image that choose the app port using `PORT` environment variable and create a `ConfigMap` object that add PORT env to your deployment
