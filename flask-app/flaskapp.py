from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    timestamp = datetime.now()
    return "hello from ".flask.request.host_url." it's ".timestamp
if __name__ == "__main__":
    app.run(host='0.0.0.0')