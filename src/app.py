from flask import Flask
from flask import redirect, render_template, request
from references.reference_bank import ReferenceBank
from bibtex_generator import BibtexGenerator
from references.reference_type_bank import ReferenceTypeBank
from json_saver import read_dictionary_from_json


app = Flask(__name__)

references_from_disk = read_dictionary_from_json("testi.json")
reference_storage = ReferenceBank(references_from_disk)

reference_type_storage = ReferenceTypeBank()


@app.route("/")
def index():
    return render_template("print_doc.html", references=list(reference_storage.reference_bank.values()))


@app.route("/submitReferenceInformation/", methods=["POST"])
def result():
    reference_data = request.form
    print(reference_data)
    reference_storage.add_reference(reference_data)

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
    return render_template("base.html",refType=reference_type_storage.reference_types, filter=filter)

@app.route("/printBibtex")
def print_bibtex():
    generator = BibtexGenerator(reference_storage.get_reference_bank())
    bibtex_list = generator.make_bibtex_list()
    return render_template("print_bibtex.html", bibtexlist=bibtex_list)

@app.route("/referenceTypesAdd")
def reference_types_add():
    return render_template("reference_types_add.html", refType =reference_type_storage.all_possible_types)

@app.route("/referenceTypesAdd/add", methods = ["POST"])
def reference_types_add_new():
    tyyppi = request.form["viittaustyyppi"]
    kentat = request.form.getlist("field")
    reference_type_storage.add_new_reference_type(tyyppi, kentat)
    return redirect("/referenceTypesAdd")