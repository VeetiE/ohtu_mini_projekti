from flask import Flask
from flask import redirect, render_template, request
from references.book import Book
from bibtex_generator import BibtexGenerator
from references.reference_bank import ReferenceBank


app = Flask(__name__)

bibtex_list = []
referenceStorage = ReferenceBank()

@app.route("/")
def index():
	return render_template("print_doc.html", references = list(referenceStorage.reference_bank.values()))

@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
	referenceType = request.form["referenceType"]
	bookAuthor = request.form["author"]
	bookName = request.form["title"]
	bookPublisher = request.form["publisher"]
	bookAddress = request.form["address"]
	bookDate = request.form["published"]

	book = Book("book", bookAuthor, bookName, bookPublisher, bookAddress, bookDate)
	referenceStorage.add_reference(book)
	print(referenceStorage.reference_bank)
	
	generator = BibtexGenerator(book)
	bibtex = generator.make_bibtex()
	bibtex_list.append(bibtex)


	return redirect("/")

@app.route("/referenceForm")
def referenceForm():
	return render_template("base.html")

@app.route("/printBibtex")
def printBibtex():
	return render_template("print_bibtex.html", bibtexlist = bibtex_list)