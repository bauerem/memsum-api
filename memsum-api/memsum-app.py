from flask import Flask, request

from memsum import MemSum
memsum_hn = MemSum("model/MemSum_Final/lexis_headnotes/model.pt", "model/glove/vocabulary_200dim.pkl")
def memsum_hn_predict(text, p_stop_thres= 0.7):
    return memsum_hn.summarize(text, p_stop_thres=p_stop_thres)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"text": "hello world"}

@app.route("/summarize", methods=["POST"])
def summarize():
    if request.method == "POST":

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
    
    return "You should send POST requests to this server."