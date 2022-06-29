# from __main__ import app
from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user

app = Blueprint('tcc', __name__)

@app.route("/")
@login_required
def testcode():
    return render_template('Testcode_Template/Testcode_index.html', name=current_user.name)