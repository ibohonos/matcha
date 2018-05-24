from matcha.config import db_connect


def create_chat_room(room_name):
	agruments = [room_name]
	sql = "INSERT INTO chat_room (room_name) VALUES (?)"
	res = db_connect(sql, agruments)
	return res


def get_chat_room_id(room_name):
	agruments = [room_name]
	sql = "SELECT id_chat_room FROM chat_room WHERE room_name = ?"
	res = db_connect(sql, agruments)
	return res


def add_user_to_chat_room(id_chat_room, id_user):
	agruments = [id_chat_room, id_user]
	sql = "INSERT INTO chat_room_con (id_chat_room, id_user) VALUES (?,?)"
	res = db_connect(sql, agruments)
	return res
