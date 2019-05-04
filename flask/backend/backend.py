from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def testPost():
    if request.method == 'POST':
        return "Received POST --->>> " + str(request.data)
    else:
        return "Post didnt work"

@app.route("/", methods=['GET'])
def hello():
    return "Hello from the backend!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5002)