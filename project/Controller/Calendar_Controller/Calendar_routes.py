from flask import Blueprint, flash, render_template, url_for, request, redirect
from flask_login import login_required, current_user
from ...models import TestCodes
from ..Calendar_Controller import Calendar_selenium


cal = Blueprint('cal', __name__)



@cal.route("/calendar")
@login_required
def calendar():
    return render_template('Calendar_Template/Calendar_index.html')

@cal.route("/runCalendar", methods=['POST','GET'])
@login_required
def runCalendar():
    test_code = request.form.get('test_code')
    default_test = request.form.getlist('default_test[]')
    optional_test = request.form.getlist('optional_test[]')
    get_test_code = TestCodes.query.filter_by(test_code=test_code).first()


    if not get_test_code:
        flash('The Test Code does not exist', 'fail')
        return redirect('/calendar')
    else:
        all_data = Calendar_selenium.login(get_test_code, optional_test)

        if all_data == 'fail':
            flash('The Test Code Is Already use in this test', 'fail')
            return redirect('/calendar')
        return render_template('Calendar_Template/Calendar_index.html')