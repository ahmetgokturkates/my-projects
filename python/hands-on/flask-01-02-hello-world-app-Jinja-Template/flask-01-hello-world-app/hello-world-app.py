from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return " 18.01.2022 <h1> I am Gokturk. This is my first Flask App  </h1>  <br> <h1> I hope i am gonna be a good DevOps Engineer and AWS Solution Architech </h1> <br>  "

@app.route("/second")
def second():
    return "This is the second page"

@app.route("/third/first")
def third():
    return "This is the subpath of third path"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__=="__main__":
    app.run(debug=True)
    