from flask import Blueprint, render_template, url_for, request, redirect

test2 = Blueprint('test2', __name__)
test3 = Blueprint('test3', __name__)

@test2.route('/test')
def test():
<<<<<<< HEAD:project/Test_Route/Test.py
    return "Hello fureks"

@test3.route('/test3')
def test3():
    return "Hello fuckers"
=======
    return "Hello World"

@test2.route('/testing')
def testing():
    return "Hello World"
>>>>>>> 9935e8f797bd013eaf6a9e88e354b546d7bc6d56:project/Controller/Test_Route/Test.py
