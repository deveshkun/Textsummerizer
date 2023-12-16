from flask import Flask,render_template,request,url_for
import requests

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])  #app kaha bhejna hai
def index():
    return render_template('index.html')
@app.route('/summarize',methods=["GET","POST"])
def summarize():
    if request.method =="POST":

        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data = request.form['inputdata']
        maxlen = int(request.form['maxl'])
        minl = 100

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        output = query({"inputs": f"{data}",
                        "parameters":{"min_length":minl,"max_length":maxlen}})
        return render_template("index.html",result=list(output)[0])
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.debug=True
    app.run()