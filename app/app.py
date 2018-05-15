from flask import Flask, render_template, request, session
from flask_mail import Mail, Message
import re
import hashlib
import html
import os
from models.users import *

app = Flask(__name__)

app.secret_key = os.urandom(16)
app.config.update(dict(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=587,
	MAIL_USE_TLS=True,
	MAIL_USE_SSL=False,
	MAIL_USERNAME='rkhilenksmtp@gmail.com',
	MAIL_PASSWORD='asdQWE123',
))

mail = Mail(app)


@app.route('/')
def hello_world():
	return 'Hello Ludochka!!'


@app.route('/registration')
def registration():
	return render_template('register.html')


# def ajax_registration():
# 	print(request.form['email'])
# 	return jsonify("return from python")
#
# app.add_url_rule("/ajax_registration", "ajax_registration", ajax_registration, methods=['POST'])


@app.route('/ajax_registration', methods=['POST'])
def ajax_registration():
	r_email = html.escape(request.form['email'])
	r_login = html.escape(request.form['login'])
	pwd = request.form['pwd']

	check = check_user(r_login, r_email)
	if check:
		if check[0]["email"] == r_email:
			return "email_exist"
		elif check[0]["login"] == r_login:
			return "login_exist"
	if not r_email:
		return "no_email"
	if not r_login:
		return "no_login"
	if not pwd:
		return "no_pwd"
	if len(r_email) > 100:
		return "long_mail"
	if len(r_login) > 40:
		return "long_login"
	if len(pwd) > 100:
		return "long_pwd"
	if not re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$", r_email.lower()):
		return "wrong_email"
	if re.search("[a-zA-Z]+", pwd.lower()) is None or re.search("[0-9]+", pwd) is None:
		return "week_pwd"
	pwd_hash = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
	token_hash = hashlib.md5((r_email + r_login).encode('utf-8')).hexdigest()
	req = user_to_db(r_login, r_email, pwd_hash, token_hash)

	if not req:
		msg = Message('matcha registration', sender="rkhilenksmtp@gmail.com", recipients=[r_email])
		msg.body = "To activate account goto http://localhost:5000/activate?email=" + r_email + "&token=" + token_hash
		msg.html = "<p>To activate account goto http://localhost:5000/activate?email=" + r_email + "&token=" + token_hash + "</p>"
		mail.send(msg)
		return "registered"
	else:
		return "error"


@app.route('/activate')
def activate():
	context = {'success': 'false'}

	email = request.args.get('email')
	token = request.args.get('token')
	if email is None or token is None:
		return render_template('activate.html', context=context)

	user = check_user_token(email)
	if not user:
		return render_template('activate.html', context=context)

	if user[0]['token'] == token and user[0]['active'] == 0:
		ret = activate_user(user[0]['id_user'])
		if not ret:
			context.update({'success': 'true'})
	return render_template('activate.html', context=context)


@app.route('/login')
def login():
	context = {'success': 'false'}
	# session['id_user'] = 'admin'
	# session.pop('username', None)
	# print(session)

	return render_template('login.html', context=context)


@app.route('/ajax_login', methods=['POST'])
def ajax_login():
	l_login = html.escape(request.form['login'])
	pwd = request.form['pwd']

	if not l_login:
		return "no_login"
	if not pwd:
		return "no_pwd"
	if len(l_login) > 40:
		return "long_login"
	if len(pwd) > 100:
		return "long_pwd"
	res = check_user(l_login, l_login)
	print(res)

	return "return"


@app.route('/ajax_logout', methods=['POST'])
def ajax_logout():
	session.pop('id_user', None)
	return "logged_out"


if __name__ == '__main__':
	app.run(host="0.0.0.0")


# rkhilenksmtp@gmail.com
# asdQWE123
