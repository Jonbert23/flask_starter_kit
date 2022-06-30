from flask import Blueprint, render_template, url_for, request, redirect

test2 = Blueprint('test2', __name__)
test3 = Blueprint('test3', __name__)

@test2.route('/test')
def test():
    return "Hello World"

@test2.route('/testing')
def testing():
    return "Hello World"
