from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user

cal = Blueprint('cal', __name__)

@cal.route("/calendar")
def calendar():
    return render_template('Calendar_Template/Calendar_index.html')