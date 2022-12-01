from flask import Flask
from flask import redirect, render_template, request
from src.references.book import Book
from src.bibtex_generator import BibtexGenerator
from src.json_saver import save_array_to_json



app = Flask(__name__)
reference_list = []
bibtex_list = []

@app.route("/")
def index():
	

	


	return render_template("print_doc.html", references = reference_list)

@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
	referenceType = request.form["referenceType"]
	bookAuthor = request.form["author"]
	bookName = request.form["title"]
	bookPublisher = request.form["publisher"]
	bookAddress = request.form["address"]
	bookDate = request.form["published"]

	book = Book("book", bookAuthor, bookName, bookPublisher, bookAddress, bookDate)
	reference_list.append(book)
	save_array_to_json(reference_list)
	
	generator = BibtexGenerator(book)
	bibtex = generator.make_bibtex()
	bibtex_list.append(bibtex)


	for i in reference_list: print(i)

	return redirect("/")

@app.route("/referenceForm")
def referenceForm():
	return render_template("base.html")

@app.route("/printBibtex")
def printBibtex():
	return render_template("print_bibtex.html", bibtexlist = bibtex_list)
