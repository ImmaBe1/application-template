from flask import Blueprint, render_template

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return render_template('index.html')
    
@site.route('/privacy-policy')
def privacy():
    return '<h1>Privacy policy</h1>'