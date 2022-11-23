from flask import Flask
from flask import redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
     return render_template("base.html")

@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
    referenceType = request.form["referenceType"]
    bookName = request.form["title"]
    author = request.form["author"]
    published = request.form["published"]
    print(referenceType)
    print(bookName)
    print(author)
    print(published)
    return redirect("/")

