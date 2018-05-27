from app.config.databse import db_connect


def add_friend(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "INSERT INTO friendships (id_requester, id_user_requested) VALUES (?,?)"
	res = db_connect(sql, arguments)
	return res


def check_friends(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "SELECT * FROM friendships WHERE id_requester=? AND id_user_requested=?"
	res = db_connect(sql, arguments)
	if res:
		return res[0]
	return res


def delete_user_request(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "DELETE FROM friendships WHERE id_requester=? AND id_user_requested=?"
	res = db_connect(sql, arguments)
	return res


def confirm_user_request(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "UPDATE friendships SET status=1 WHERE id_requester=? AND id_user_requested=?"
	res = db_connect(sql, arguments)
	return res

