from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user
from Project.Controller.Eod_Controller.Eod_tester import testEod

eod = Blueprint('eod', __name__)

@eod.route("/eod-form")
def eodForm():
    testEod("as")
    return render_template('Eod_Template/Eod_index.html')