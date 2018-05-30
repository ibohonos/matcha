from app.config.databse import db_connect, db_insert


def create_post(id_user, id_user_from, type_p, status, content, img, video):
	arguments = [id_user, id_user_from, type_p, status, content, img, video]
	sql = "INSERT INTO posts (id_user, id_user_from, type, status, content, img, video) VALUES (?,?,?,?,?,?,?)"
	res = db_insert(sql, arguments)
	return res


def all_user_post(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM posts WHERE id_user=? ORDER BY id_post DESC"
	res = db_connect(sql, arguments)
	return res
