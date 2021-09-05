# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request
import json

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def search():
    language_from: str = request.args.get('from', default=None, type=str)
    language_to: str = request.args.get('to', default=None, type=str)
    form: str = request.args.get('form', default=None, type=str)

    print(language_from, language_to, form)

    if (language_from and form):
              
        ordered_dict = json.load(open('static/data/ordered.json', encoding='utf-8')) 
        print(ordered_dict)
        try:
            entity_ids = ordered_dict[language_from][form]
        except:
            entity_ids = False

        if entity_ids:
            entities_dict = json.load(open('static/data/entities.json', encoding='utf-8'))

            if isinstance(entity_ids, list): # There are homonymes
                results = []
                for entity_id in entity_ids:
                    results.append(entities_dict[str(entity_id)])
            
            else: # Only one match
                results = [entities_dict[str(entity_ids)]]
        
        else:
            results = ["No match."]
    else:
        results = []

    return render_template('home/index.html', results = results)