# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request
import json

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def search():
    language_from: str = request.args.get('from', default=None, type=str)
    language_to: str = request.args.get('to', default=None, type=str)
    form: str = request.args.get('form', default=None, type=str)
    format: str = request.args.get('format', default=None, type=str)

    print(language_from, language_to, form)

    if (language_from and form):
              
        ordered_dict = json.load(open('static/data/ordered.json', encoding='utf-8')) 

        try:
            entity_ids = ordered_dict[language_from][form]
        except:
            entity_ids = False

        if entity_ids:
            entities_dict = json.load(open('static/data/entities.json', encoding='utf-8'))

            if isinstance(entity_ids, list): # There are homonymes
                results = {}
                for i in range(len(entity_ids)):
                    results[i] = entities_dict[str(entity_ids[i])]
            
            else: # Only one match
                results = entities_dict[str(entity_ids)]
        
        else:
            results = "No match."
    else:
        results = None

    if format == 'json':
        return results, 200 # Still need some output edit (no lists, only dictionary with results)

    return render_template('home/index.html', language_from = language_from, language_to = language_to, form = form, results = results)