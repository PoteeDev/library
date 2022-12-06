from flask import Flask, request

app = Flask(__name__)

fake_db = list()

@app.route("/ping")
def ping():
    return "pong"

@app.route("/get/<_id>")
def get(_id):
    return fake_db[int(_id)]

@app.route("/put", methods=['POST'])
def put():
    global fake_db
    fake_db.append(request.form['flag'])
    return str(len(fake_db)-1)

@app.route("/exploit")
def vulnerability():
    return "yes"

if __name__ == "__main__":
    app.run()