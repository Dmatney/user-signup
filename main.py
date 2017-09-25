from flask import Flask, request, redirect, render_template
import os
import jinja2

app = Flask(__name__)
app.config['Debug'] = True

@app.route("/")
def index():
    return render_template('userinfo.html')
@app.route("/", methods=['POST'])
def validate_info():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']
    usernameerror = ''
    passworderror = ''
    emailerror = ''
    if username == '':
        usernameerror = "Please add a user name"
    elif ' ' in username:
        usernameerror = "The user name can not contain spaces"
    elif len(username) <3 or len(username) > 20:
        usernameerror = "The user name must be between 3 and 20 characters long"
    if password == '' or verifypassword == '':
        passworderror = 'Please add a password and verify it'
    elif password != verifypassword:
        passworderror = 'Password and verify password fields MUST match'
    elif ' ' in password:
        passworderror = 'Password can not contain spaces'
    elif len(password) <3 or len(password) > 20:
        passworderror = 'Password must be between 3 and 20 characters long'
    if email != '':
        if ' ' in email:
            emailerror = 'Email can not contain spaces'
        elif len(email) <3 or len(email) > 20:
            emailerror = 'Email must be between 3 and 20 characters in length'
        elif email.count('.') != 1 or email.count ('@') != 1:
            emailerror = 'Email must contain exactly one "." and one "@"'
    if not usernameerror and not passworderror and not emailerror:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('userinfo.html', usernameerror = usernameerror, passworderror = passworderror, emailerror = emailerror,
                                username = username, email = email)

@app.route('/welcome')
def welcomemessage():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)
app.run()