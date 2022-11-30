from flask import Flask
from flask import redirect, render_template, request
from src.references.book import Book


app = Flask(__name__)
referenceList = []

@app.route("/")
def index():
	return render_template("print_doc.html", references = referenceList)

@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
	referenceType = request.form["referenceType"]
	bookAuthor = request.form["author"]
	bookName = request.form["title"]
	bookPublisher = request.form["publisher"]
	bookAddress = request.form["address"]
	bookDate = request.form["published"]

	book = Book(referenceType, bookAuthor, bookName, bookPublisher, bookAdress, bookDate)
	referenceList.append(book)

	for i in referenceList: print(i)

	return redirect("/")

@app.route("/referenceForm")
def referenceForm():
	return render_template("base.html")


