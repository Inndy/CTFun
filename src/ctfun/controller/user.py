from ..common import *
from ..model import *

@route('/register', method='POST')
def regist():
    grab(requests.forms, locals(), 'username', 'password', 'invite_code')

@route('/login', method='GET')
@view('login.html')
def login_page():
    pass

@route('/login', method='POST')
def login():
    grab(requests.forms, locals(), 'username', 'password')
    user.find(username)
