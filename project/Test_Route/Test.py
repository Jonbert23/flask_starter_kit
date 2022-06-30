from flask import Blueprint, render_template, url_for, request, redirect

test2 = Blueprint('test2', __name__)

@test2.route('/test')
def test():
    return "Hello fureks"