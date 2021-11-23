from bottle import run, template, default_app
from bottle import get, post 
from bottle import debug
from bottle import request, response, redirect
from sessions import load_session, save_session

import os 
import json

def new_profile(username):
    profile = {
        'username' : username,
        'password' : 'no_password'
    }
    os.makedirs('data/profiles', exist_ok=True)
    with open(f'data/profiles/{username}.profile','w') as f:
        json.dump(profile, f)
    return profile

def load_profile(username):
    try:
        os.makedirs('data/profiles', exist_ok=True)
        with open(f'data/profiles/{username}.profile','r') as f:
            profile = json.load(f)
    except Exception as e:
        print(f'Profile error:{e}')
        profile = new_profile(username)
    print('loaded profile = ',profile)
    return profile

def save_profile(profile):
    username = profile['username']
    if username == 'guest':
        return
    os.makedirs('data/profiles', exist_ok=True)
    with open(f'data/profiles/{username}.profile','w') as f:
        json.dump(profile, f)

def not_logged_in(session):
    if 'username' not in session:
        return True
    if session['username'] == 'guest':
        return True

@get('/')
@get('/hello')
def get_hello(name=None):
    session = load_session(request)
    if not_logged_in(session):
        redirect("/login")
    username = session.get('username', 'guest')
    profile = load_profile(username)
    favcolor = profile.get('favcolor', 'not known')
    print('saving loaded session',session)
    save_session(session, response)
    return template('hello', name=username, color=favcolor)

@get('/signup')
def get_login():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('signup', message='')

@post('/signup')
def post_signup():
    session = load_session(request)
    username = request.forms['username']
    password = request.forms['password']
    password_again = request.forms['password_again']
    profile = load_profile(username)
    print('signup starting ',profile)
    if profile['password'] != 'no_password':
        print("ALREADY A CUSTOMER")
        save_session(session, response)
        redirect('/login')
    profile['password'] = password
    session['username'] = username
    save_profile(profile)
    save_session(session, response)
    redirect('/hello')

@get('/login')
def get_login():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('login', message='')

@post('/login')
def post_login():
    session = load_session(request)
    username = request.forms['username']
    password = request.forms['password']
    favcolor = request.forms['favcolor']
    profile = load_profile(username)
    print("loaded profile",profile)
    print('password',password)
    if profile['password'] != password:
        save_session(session, response)
        redirect('/hello')

    print("logged in")
    session['username'] = username
    profile['favcolor'] = favcolor

    save_profile(profile)
    save_session(session, response)
    redirect('/hello')

debug(True)
run(host='localhost', port=8068, reloader=True)