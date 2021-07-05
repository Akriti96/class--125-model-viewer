from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect

app=Flask(__name__)


@app.route("/")
def welcome():
    return "welcome to my webpage"

@app.route("/sucess/<int:score>")
def sucess(score):
    return "<html> <body> <h1> The Person has passed+str(score)</h1></body></html>"

@app.route("/fail/<int:score>")
def fail(score):
    return "The Person has Failed and the marks is "+ str(score)

# result checker
@app.route("/result/<int:marks>")
def result(marks):
    res=""
    if marks <50:
        res= "fail"
    else:
        res="sucess"
    return redirect(url_for(res,score=marks))
if(__name__=="__main__"):
 app.run(debug=True)