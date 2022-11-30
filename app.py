from flask import Flask
from flask import redirect, render_template, request
from src.references.book import Book


app = Flask(__name__)
referenceList = []

@app.route("/")
def index():
	return render_template("base.html")

@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
	referenceType = request.form["referenceType"]
	bookAuthor = request.form["author"]
	bookName = request.form["title"]
	bookDate = request.form["published"]

	book = Book(referenceType, bookAuthor, bookName, bookDate)
	referenceList.append(book)

	for i in referenceList: print(i)

	return redirect("/")

@app.route("/print_doc", methods=["POST"])
def print_doc():
	return render_template("print_doc.html", references = referenceList)
