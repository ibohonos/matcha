from app import app, mail
import hashlib
import html
from flask import render_template, request, session, redirect, url_for
import re
from datetime import datetime
from flask_mail import Message
from app.models.users import *
from random import randint


@app.route('/ajax_registration', methods=['POST'])
def ajax_registration():
	r_email = html.escape(request.form['email'])
	r_login = html.escape(request.form['login'])
	pwd = request.form['pasword']
	r_first = request.form['first_name']
	r_last = request.form['last_name']
	r_gender = request.form['gender']
	num = randint(1, 12)

	if num > 0 and num <= 6:
		cover = str(num) + ".jpg"
	else:
		cover = str(num) + ".jpeg"

	str_date = request.form['day'] + " " + request.form['month'] + " " + request.form['year']
	try:
		r_birthday = datetime.strptime(str_date, '%d %b %Y')
	except:
		return "wrong_data"
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
	if not re.match("^[a-zA-Z0-9]+$", r_login):
		return "wrong_login"
	if len(pwd) > 100:
		return "long_pwd"
	if not re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$", r_email.lower()):
		return "wrong_email"
	if re.search("[a-zA-Z]+", pwd.lower()) is None or re.search("[0-9]+", pwd) is None:
		return "week_pwd"
	date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	pwd_hash = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
	token_hash = hashlib.md5((r_email + r_login + date_str).encode('utf-8')).hexdigest()
	cover_img = "/static/uploads/covers/" + cover
	req = user_to_db(r_login, r_email, pwd_hash, token_hash, r_first, r_last, r_gender, r_birthday, cover_img)

	if not req:
		msg = Message('matcha registration', sender="rkhilenksmtp@gmail.com", recipients=[r_email])
		msg.body = "To activate account goto " + request.url_root + "activate?email=" + r_email + "&token=" + token_hash
		msg.html = "<p>To activate account goto <a href='" + request.url_root + "activate?email=" + r_email + "&token=" + token_hash + "'>this link</a></p>"
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


@app.route('/ajax_login', methods=['POST'])
def ajax_login():
	if session.get('id_user_logged'):
		return "already_logged"
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

	if len(res) == 1:
		res = res[0]
		if res['active'] != 1:
			return "not_active"
		pwd_hash = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
		if res['password'] == pwd_hash:
			session['id_user_logged'] = res['id_user']
			session['user_data'] = res
			return "logged_in"
		else:
			return "wrong_pwd"
	else:
		return "no_user"


# @app.route('/ajax_logout', methods=['POST'])
@app.route('/logout')
def ajax_logout():
	session.pop('id_user_logged', None)
	session.pop('user_data', None)
	return redirect(url_for('index'))


@app.route('/recover')
def recover():
	context = {'success': 'false', 'token': "none", 'email': "none"}
	if session.get('id_user_logged'):
		return redirect(url_for('index'))

	email = request.args.get('email')
	token = request.args.get('token')
	if email and token:
		check = check_user_token(email)
		if check:
			check = check[0]
			if token == check['token']:
				context.update({'success': 'true', 'token': token, 'email': email})
				return render_template('recover.html', context=context)
		return render_template('recover.html', context=context)

	return render_template('recover.html', context=context)


@app.route('/ajax_recover', methods=['POST'])
def ajax_recover():
	r_login = html.escape(request.form['login'])

	check = check_user(r_login, r_login)
	if len(check) == 1:
		check = check[0]
	else:
		return "no_user"
	if check["active"] != 1:
		return "not_active"

	date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	token_hash = hashlib.md5((r_login + date_str).encode('utf-8')).hexdigest()

	req = user_update_token(check['id_user'], token_hash)
	if not req:
		msg = Message('matcha recover', sender="rkhilenksmtp@gmail.com", recipients=[check['email']])
		msg.body = "To recover pwd goto " + request.url_root + "recover?email=" + check[
			'email'] + "&token=" + token_hash
		msg.html = "<p>To recover pwd goto " + request.url_root + "recover?email=" + check[
			'email'] + "&token=" + token_hash + "</p>"
		mail.send(msg)

	return "msg_sent"


@app.route('/ajax_new_pwd', methods=['POST'])
def ajax_new_pwd():
	pwd = request.form['pwd']
	token = request.form['token']
	email = request.form['email']

	if len(pwd) < 6:
		return "short_pwd"
	if len(pwd) > 100:
		return "long_pwd"
	if re.search("[a-zA-Z]+", pwd.lower()) is None or re.search("[0-9]+", pwd) is None:
		return "week_pwd"

	pwd_hash = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
	check = check_user_token(email)

	if len(check) == 1:
		check = check[0]
	else:
		return "no_user"

	if check['token'] == token:
		res = user_new_pwd(check['id_user'], pwd_hash)
		if not res:
			return "changed"
	else:
		return "error"