from flask import Flask,render_template,url_for
import requests

qury = 'hello'

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])  #app kaha bhejna hai
def index():
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    api = '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'
    headers = {"Authorization": f"Bearer {api}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    output = query({"inputs": f'{qury}'})
    return render_template("index.html", result=output)  # redirect to homepage

if __name__=='__main__':
    app.debug=True
    app.run()