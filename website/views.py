from flask import Blueprint, render_template, request, flash, make_response, Response
import os
import re
import time
from tqdm import tqdm
from datetime import datetime
import spacy
from spacy import displacy

views = Blueprint('views', __name__)

model_name = "model-brand"
nlp = spacy.load(model_name)


@views.route('/')
def home():
	return render_template("home.html")


@views.route('/ner-marques', methods=["GET", "POST"])
def ner_marques():
	if request.method == "POST":
		text = request.form['text']
		print(text)

		doc = nlp(text)
		colors = {"Brand": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
		options = {"ents": ["Brand"], "colors": colors}
		spacy_render = displacy.render(doc, style="ent", options=options, page=True)
		spacy_render = spacy_render.replace(" padding: 4rem 2rem;", "")
		return render_template("ner_marques.html", page=2, spacy_render=spacy_render)
	else:
		return render_template("ner_marques.html", page=1)