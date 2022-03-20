from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 1994, number2 = 2022)

@app.route("/mult")
def number():
    var1, var2 = 1994, 2022
    return render_template("body.html", num1 = var1, num2 = var2, age = var2-var1)




if __name__=="__main__":
    app.run(debug=True) 