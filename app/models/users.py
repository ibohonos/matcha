from config.databse import db_connect


def user_to_db(login, email, pwd, token):
	agruments = [login, email, pwd, token]
	sql = "INSERT INTO users (login, email, password, token) VALUES (?,?,?,?)"
	res = db_connect(sql, agruments)
	return res


def check_user(login, email):
	agruments = [login, email]
	sql = "SELECT id_user, email, login FROM users WHERE login=? OR email=?"
	res = db_connect(sql, agruments)
	return res

