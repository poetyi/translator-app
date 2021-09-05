# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template

from views.home import home

app = Flask(__name__)


app.register_blueprint(home)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('home/404.html'), 404


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host="0.0.0.0",port=8000,debug=True)
    #app.run(host='0.0.0.0') activate on Docker