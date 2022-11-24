from flask import Flask
from flask import redirect, render_template, request
from src.references.book import Book


app = Flask(__name__)
references = []

@app.route("/")
def index():
	return render_template("base.html")

@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
	referenceType = request.form["referenceType"]
	bookAuthor = request.form["author"]
	bookName = request.form["title"]
	bookDate = request.form["published"]

	if referenceType.lower() == "book":
		book = Book(bookAuthor, bookName, bookDate)
		references.append(book)

	for i in references: print(i)

	return redirect("/")

@app.route("/print", methods=["POST"])
def print():
	return render_template("print.html")

