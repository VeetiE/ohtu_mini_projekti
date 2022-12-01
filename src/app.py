from flask import Flask
from flask import redirect, render_template, request
from references.book import Book
from references.reference_bank import ReferenceBank
from bibtex_generator import BibtexGenerator



app = Flask(__name__)

reference_storage = ReferenceBank()


@app.route("/")
def index():
    return render_template("print_doc.html",
    references=list(reference_storage.reference_bank.values()))


@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
    #reference_type = request.form["referenceType"]
    book_author = request.form["author"]
    book_name = request.form["title"]
    book_publisher = request.form["publisher"]
    book_address = request.form["address"]
    book_date = request.form["published"]

    book = Book("book", book_author, book_name,
                book_publisher, book_address, book_date)
    reference_storage.add_reference(book)
    print(reference_storage.reference_bank)

    return redirect("/")


@app.route("/referenceForm")
def reference_form():
    return render_template("base.html")


@app.route("/printBibtex")
def print_bibtex():
    generator = BibtexGenerator(reference_storage.reference_bank)
    bibtex_list = generator.make_bibtex_list()
    return render_template("print_bibtex.html", bibtexlist=bibtex_list)
