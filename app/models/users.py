from config.databse import db_connect


def user_to_db(login, email, pwd, token, first_name, last_name, gender, birthday):
	agruments = [login, email, pwd, token, first_name, last_name, gender, birthday]
	sql = "INSERT INTO users (login, email, password, token, first_name, last_name, gender, date_birth) VALUES (?,?,?,?,?,?,?,?)"
	res = db_connect(sql, agruments)
	return res


def check_user(login, email):
	agruments = [login, email]
	sql = "SELECT * FROM users WHERE login=? OR email=?"
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


def user_update_token(id_user, token):
	agruments = [token, id_user]
	sql = "UPDATE users SET token = ? WHERE id_user=?"
	res = db_connect(sql, agruments)
	return res


def user_new_pwd(id_user, pwd):
	agruments = [pwd, id_user]
	sql = "UPDATE users SET password = ?, token = NULL WHERE id_user=?"
	res = db_connect(sql, agruments)
	return res
