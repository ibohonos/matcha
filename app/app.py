from flask import Flask, render_template, request, jsonify
import re
import hashlib
import html
from models.users import *

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello Ludochka!!'


@app.route('/registration')
def registration():
	return render_template('register.html', name="asd")


# def ajax_registration():
# 	print(request.form['email'])
# 	return jsonify("return from python")
#
# app.add_url_rule("/ajax_registration", "ajax_registration", ajax_registration, methods=['POST'])


@app.route('/ajax_registration', methods=['POST'])
def ajax_registration():
	email = html.escape(request.form['email'])
	login = html.escape(request.form['login'])
	pwd = request.form['pwd']

	check = check_user(login, email)
	if check:
		if check[0]["email"] == email:
			return "email_exist"
		elif check[0]["login"] == login:
			return "login_exist"
	if not email:
		return "no_email"
	if not login:
		return "no_login"
	if not pwd:
		return "no_pwd"
	if len(email) > 100:
		return "long_mail"
	if len(login) > 40:
		return "long_login"
	if len(pwd) > 100:
		return "long_pwd"
	if not re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$", email.lower()):
		return "wrong_email"
	if re.search("[a-zA-Z]+", pwd.lower()) is None or re.search("[0-9]+", pwd) is None:
		return "week_pwd"
	pwd_hash = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
	token_hash = hashlib.md5((email + login).encode('utf-8')).hexdigest()
	req = user_to_db(login, email, pwd_hash, token_hash)
	if not req:
		return "registered"
	else:
		return "error"


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True, )
