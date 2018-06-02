from app.config.databse import db_connect, db_insert


def user_to_db(login, email, pwd, token, first_name, last_name, gender, birthday, cover):
	agruments = [login, email, pwd, token, first_name, last_name, gender, birthday, cover]
	sql = "INSERT INTO users (login, email, password, token, first_name, last_name, gender, date_birth, cover) VALUES (?,?,?,?,?,?,?,?,?)"
	res = db_insert(sql, agruments)
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


def get_user_by_id(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM users WHERE id_user = ?"
	res = db_connect(sql, arguments)
	if res:
		return res[0]
	return res


def get_about(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM about WHERE id_user=?"
	res = db_connect(sql, arguments)
	if res:
		return res[0]
	return res


def create_about(id_user):
	arguments = [id_user]
	sql = "INSERT INTO about (id_user) VALUES (?)"
	res = db_connect(sql, arguments)
	return res

