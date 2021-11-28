import os 
import json
from bottle import run, template, default_app
from bottle import get, post 
from bottle import debug
from bottle import request, response, redirect
from sessions import load_session, save_session
from profiles import load_profile, save_profile
from passwords import encode_password, verify_password


def logged_in(session):
    return session.get('username', 'guest') != 'guest'

@get('/')
@get('/hello')
def get_hello(name=None):
    session = load_session(request)

    if not logged_in(session):
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
    if 'username' in profile:
        print("ALREADY A CUSTOMER")
        save_session(session, response)
        redirect('/signup')
    profile['username'] = username
    profile['encoding'] = encode_password(password)
    save_profile(profile)
    session['username'] = username
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

    if verify_password(password, profile.get('encoding',':')):
        print("logged in")
        session['username'] = username
        profile['favcolor'] = favcolor
        save_profile(profile)
        save_session(session, response)
        redirect('/hello')

    else:
        print("not logged in")
        save_session(session, response)
        redirect('/login')


debug(True)
run(host='localhost', port=8068, reloader=True)