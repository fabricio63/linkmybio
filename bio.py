from flask import Flask, jsonify, render_template, request
import os,optparse,sys
import yaml

app = Flask(__name__)

code_file = "links.yaml"
with open(code_file) as yml:
    yml_file = yaml.load(yml)
links = yml_file['links']
face = links['facebook']
descriptionf = face['description']
linkf = face['link']
ig = links['instagram']
descriptiong = ig['description']
linkg = ig['link']

@app.route("/")
def home():
    
    return render_template("home.html", name = yml_file['name'],shortbio = yml_file['shortbio'],miimagen =yml_file['picture'],facebook = descriptionf,linkf = linkf,instagram = descriptiong,linkg = linkg )

debug = True
app.run(host="0.0.0.0",debug=debug)
