from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    # address = 'http://172.17.0.5:5002/' #<--- this is the IP I want to get automatically
    print("received a request")
    # return "Hello from frontend"
    r = requests.post("http://backend-service:5002", data="---[Token]---", timeout=1)
    return "Frontend Here. Response from Backend = "+str(r.content)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5001)