from flask import Flask, render_template, request, session, redirect, url_for
from flask_mail import Mail, Message
from flask_socketio import SocketIO, send, join_room, leave_room, emit
import re
import hashlib
import html
import os
from datetime import datetime, date
from models.users import *
from models.chat import *

app = Flask(__name__)
app.secret_key = os.urandom(16)
socketio = SocketIO(app)

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
def index():
	if session.get('id_user_logged'):
		return render_template('newsfeed.html')
	return render_template('index-register.html')


@app.route('/test')
def test():
	return render_template('activate.html')


# @app.route('/registration')
# def registration():
# 	return render_template('register.html')


# def ajax_registration():
# 	print(request.form['email'])
# 	return jsonify("return from python")
#
# app.add_url_rule("/ajax_registration", "ajax_registration", ajax_registration, methods=['POST'])


@app.route('/ajax_registration', methods=['POST'])
def ajax_registration():
	r_email = html.escape(request.form['email'])
	r_login = html.escape(request.form['login'])
	pwd = request.form['pasword']
	r_first = request.form['first_name']
	r_last = request.form['last_name']
	r_gender = request.form['gender']

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
	pwd_hash = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
	token_hash = hashlib.md5((r_email + r_login).encode('utf-8')).hexdigest()
	req = user_to_db(r_login, r_email, pwd_hash, token_hash, r_first, r_last, r_gender, r_birthday)

	if not req:
		msg = Message('matcha registration', sender="rkhilenksmtp@gmail.com", recipients=[r_email])
		msg.body = "To activate account goto " + request.url_root + "activate?email=" + r_email + "&token=" + token_hash
		msg.html = "<p>To activate account goto " + request.url_root + "activate?email=" + r_email + "&token=" + token_hash + "</p>"
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


# @app.route('/login')
# def login():
# 	if session.get('id_user_logged'):
# 		return redirect(url_for('index'))
#
# 	return render_template('login.html')


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
			return "logged_in"
		else:
			return "wrong_pwd"
	else:
		return "no_user"


# @app.route('/ajax_logout', methods=['POST'])
@app.route('/ajax_logout')
def ajax_logout():
	session.pop('id_user_logged', None)
	return "logged_out"


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

	token_hash = hashlib.md5((r_login + "asdasd").encode('utf-8')).hexdigest()

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


@app.route('/chat')
def chat():
	if not session.get('id_user_logged'):
		return redirect(url_for('login'))

	if session.get('id_user_logged') == 1 or session.get('id_user_logged') == 3:
		context = {'chat_room': 'test_room_1_2'}
	else:
		context = {'chat_room': 'room_for_all'}
	return render_template('chat.html', context=context)


# @socketio.on('message')
# def handleMessage(msg, user):
# 	print('Message: ' + msg)
# 	msg = html.escape(msg)
# 	send(msg, broadcast=True)


chat_users_sid_to_id = {}
chat_users_sid_to_room = {}


@socketio.on('test_print', namespace='/chat')
def test_print(msg):
	print(msg['room'])


@socketio.on('message', namespace='/chat')
def message(msg):
	print("msg: " + msg)
	room = chat_users_sid_to_room[request.sid]
	emit('message_from_server', msg, room=room)


@socketio.on('connect', namespace='/chat')
def connect():
	chat_users_sid_to_id[request.sid] = session.get('id_user_logged')


@socketio.on('disconnect', namespace='/chat')
def disconnect():
	chat_users_sid_to_id.pop(request.sid)
	room = chat_users_sid_to_room[request.sid]
	leave_room(room)
	chat_users_sid_to_room.pop(request.sid)


@socketio.on('join_room', namespace='/chat')
def test_print(data):
	join_room(data['room'])
	chat_users_sid_to_room[request.sid] = data['room']

	print("sid:" + request.sid + " joined room " + data['room'])
	print(chat_users_sid_to_id)
	print(chat_users_sid_to_room)


if __name__ == '__main__':
	socketio.run(app, host="0.0.0.0")


# rkhilenksmtp@gmail.com
# asdQWE123
