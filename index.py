# _*_ coding: utf-8 _*_

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/more")
def more():
    return render_template("more.html", name="kkk")

if __name__ == "__main__":
    app.run(debug=True)
