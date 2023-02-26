from flask import Flask, request
import json

from memsum import MemSum


def memsum_hn_predict(text, p_stop_thres= 0.7):
    memsum_hn = MemSum("model/MemSum_Final/lexis_headnotes/model.pt", "model/glove/vocabulary_200dim.pkl")

    return memsum_hn.summarize(text, p_stop_thres=p_stop_thres)

# Read file with users
def getUsers():
    userfile = "users.json"
    with open(userfile) as f:
        users = json.load(f)
    
    return users

# Very simple bearer token check
def checkUserAuth():
    headers = request.headers
    bearer = headers.get('Authorization')    # Bearer YourTokenHere
    token = bearer.split()[1]

    loggedIn = False

    # Read users
    users = getUsers()

    for user in users:
        if token == user["token"]:
            loggedIn = True
            break


    return loggedIn 
    
app = Flask(__name__)
    
@app.route("/")
def hello_world():
    data = {"text": "Hello world."}

@app.post("/summarize")
def summarize():
    loggedIn = checkUserAuth()

    if loggedIn == True:
        data = request.get_json() or {}

        text = data.get("text", None)
        p_stop_thres = data.get("p_stop_temp", None)

        if p_stop_thres and text:
            summary = memsum_hn_predict(text, p_stop_thres=p_stop_thres)
        elif text:
            summary = memsum_hn_predict(text)
        else:
            summary = "No text to summarize."

        return {"summary": summary}
    
    return "Please Authenticate", 403