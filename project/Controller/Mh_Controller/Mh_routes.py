from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user

mh = Blueprint('mh', __name__)


##FIX
@mh.route("/morning-huddle")
def morning_huddle():
    return render_template('Mh_Template/Mh_index.html')