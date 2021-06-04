from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from src.services.util import httpQuery
import json

account = Blueprint('account', __name__, url_prefix='/myaccount')

@account.route('/')
def myhome():
    return render_template('profile.html')

@account.route('/login')
def login():
    return render_template('login.html')

@account.route('/login', methods=['POST'])
def login_post():
    session.pop('_flashes', None)
    username = request.form.get('email')
    password = request.form.get('password')
    print(username)
    print(password)
    #session['tet'] = 'lol'
    #print(session.items())
    try: 
        resp = httpQuery("post", "/account/login", {"username": username, "password": generate_password_hash(password, method='sha256')})
        if resp.status_code == 200:
            return redirect(url_for('account.myhome'))
        else:
            error = (json.loads(resp.get_data().decode("utf-8")))
            flash(u'{}'.format(error['text']), 'danger')
            return redirect(url_for('account.login'))
    except Exception as e:
        flash(u'{}'.format(e), 'danger')
        return redirect(url_for('account.login'))

@account.route('/register')
def register():
    return render_template('register.html')

@account.route('/register', methods=['POST'])
def signup_post():
    session.pop('_flashes', None)
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    try: 
        resp = httpQuery("post", "/account/register", {"username": email, "name":name, "password": generate_password_hash(password, method='sha256')})
        #print(resp)
        if resp.status_code == 200:
            flash(u'Successful registration', 'success')
            return redirect(url_for('account.login'))
        else:
            error = (json.loads(resp.get_data().decode("utf-8")))
            flash(u'{}'.format(error['text']), 'danger')
            return redirect(url_for('account.register'))
    except Exception as e:
        flash(u'{}'.format(e), 'danger')
        return redirect(url_for('account.register'))

@account.route('/logout')
def logout():
    return 'Logout'
