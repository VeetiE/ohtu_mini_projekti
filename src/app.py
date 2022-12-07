from flask import Flask
from flask import redirect, render_template, request
from references.book import Book
from references.reference_bank import ReferenceBank
from bibtex_generator import BibtexGenerator
from references.reference_type_bank import ReferenceTypeBank


app = Flask(__name__)

reference_storage = ReferenceBank()
reference_type_storage = ReferenceTypeBank()

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



@app.route("/referenceForm",methods=["GET","POST"])
def reference_form():
    if request.method == "POST":
        fill = request.form["option"]
        print(fill)
    return render_template("base.html",refType=reference_type_storage.reference_types)

@app.route("/referenceForm/setFilter/", methods=["POST"])
def reference_form_set_filter():
    filter = request.form["references"]
    print(filter)
    return redirect("/referenceForm/" + filter)

@app.route("/referenceForm/<filter>")
def reference_form_filtered(filter):
  
    print("hello")
   
    n = {filter:reference_type_storage.reference_types[filter]}
    print(n)
    return render_template("base.html",refType=n)

@app.route("/printBibtex")
def print_bibtex():
    generator = BibtexGenerator(reference_storage.reference_bank)
    bibtex_list = generator.make_bibtex_list()
    return render_template("print_bibtex.html", bibtexlist=bibtex_list)

@app.route("/referenceTypesAdd", methods = ["GET", "POST"])
def reference_types_add():
    if request.method == "POST":
        pass
    return render_template("reference_types_add.html", refType =reference_type_storage.all_possible_types)