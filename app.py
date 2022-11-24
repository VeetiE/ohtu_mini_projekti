from flask import Flask
from flask import redirect, render_template, request
from references.book import Book


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("base.html")

@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
	referenceType = request.form["referenceType"]
	bookAuthor = request.form["author"]
	bookName = request.form["title"]
	bookDate = request.form["published"]

	references = []

	if referenceType.lower() == "book":
		book = Book(bookAuthor, bookName, bookDate)
		references.append(book)

	print(referenceType)
	print(bookAuthor)
	print(bookName)
	print(bookDate)
	return redirect("/")

