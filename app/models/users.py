from config.databse import db_connect


def user_to_db(login, email, pwd, token):
	agruments = [login, email, pwd, token]
	sql = "INSERT INTO users (login, email, password, token) VALUES (?,?,?,?)"
	res = db_connect(sql, agruments)
	return res


def check_user(login, email):
	agruments = [login, email]
	sql = "SELECT id_user, email, login, password FROM users WHERE login=? OR email=?"
	res = db_connect(sql, agruments)
	return res


def check_user_token(email):
	agruments = [email]
	sql = "SELECT id_user, token, active FROM users WHERE email=?"
	res = db_connect(sql, agruments)
	return res


def activate_user(id_user):
	agruments = [id_user]
	sql = "UPDATE users SET active = 1, token = NULL WHERE id_user=?"
	res = db_connect(sql, agruments)
	return res
