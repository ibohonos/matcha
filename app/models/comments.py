from app.config.databse import db_connect, db_insert


def add_comment(id_user, id_post, text):
	arguments = [id_user, id_post, text]
	sql = "INSERT INTO comments (id_user, id_post, text) VALUES (?, ?, ?)"
	res = db_insert(sql, arguments)
	return res


def all_post_comments(id_post):
	arguments = [id_post]
	sql = "SELECT * FROM comments WHERE id_post=?"
	res = db_connect(sql, arguments)
	return res

