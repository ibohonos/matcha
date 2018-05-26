from app.config.databse import db_connect


def create_users_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS users (
		id_user INTEGER PRIMARY KEY AUTOINCREMENT,
		email VARCHAR(255) NOT NULL UNIQUE,
		password VARCHAR(255) NOT NULL,
		first_name VARCHAR(255),
		last_name VARCHAR(255),
		login VARCHAR(255) NOT NULL UNIQUE,
		avatar VARCHAR(255) NOT NULL DEFAULT "/static/uploads/avatars/default.png",
		cover VARCHAR(255) NOT NULL DEFAULT "/static/uploads/covers/1.jpg",
		date_birth DATE,
		active BOOLEAN DEFAULT 0,
		token VARCHAR(255),
		gender INT NOT NULL DEFAULT 1,
		sex_pref INT,
		biography TEXT DEFAULT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP)
		''')
	if res:
		print(res)
	else:
		print("users ok")


def create_tags_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS tags (
		id_tag INTEGER PRIMARY KEY AUTOINCREMENT,
		tag VARCHAR(255) NOT NULL UNIQUE)
		''')
	if res:
		print(res)
	else:
		print("tags ok")

	res = db_connect('''
		CREATE TABLE IF NOT EXISTS tags_con (
		id_tag INTEGER NOT NULL,
		id_user INTEGER NOT NULL,
		FOREIGN KEY (id_tag) REFERENCES tags(id_tag) ON DELETE CASCADE,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("tags_con ok")


def create_img_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS images (
		id_img INTEGER PRIMARY KEY AUTOINCREMENT,
		id_user INTEGER NOT NULL,
		img_src VARCHAR(255) NOT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("images ok")


def create_chat_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS chat_room (
		id_chat_room INTEGER PRIMARY KEY AUTOINCREMENT,
		room_name VARCHAR(255) NOT NULL)
		''')
	if res:
		print(res)
	else:
		print("chat_room ok")

	res = db_connect('''
		CREATE TABLE IF NOT EXISTS chat_room_con (
		id_chat_room INTEGER NOT NULL,
		id_user INTEGER NOT NULL,
		FOREIGN KEY (id_chat_room) REFERENCES chat_room(id_chat_room) ON DELETE CASCADE,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("chat_room_con ok")

	res = db_connect('''
		CREATE TABLE IF NOT EXISTS chat_message (
		id_message INTEGER PRIMARY KEY AUTOINCREMENT,
		id_user INTEGER NOT NULL,
		id_chat_room INTEGER NOT NULL,
		m_text TEXT,
		red BOOLEAN DEFAULT 0 NOT NULL,
		FOREIGN KEY (id_chat_room) REFERENCES chat_room(id_chat_room) ON DELETE CASCADE,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("chat_message ok")


def create_friends_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS friendships (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		id_requester INTEGER NOT NULL,
		id_user_requested INTEGER NOT NULL,
		status BOOLEAN DEFAULT 0 NOT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_requester) REFERENCES users(id_user) ON DELETE CASCADE,
		FOREIGN KEY (id_user_requested) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("friendships ok")


if __name__ == '__main__':
	create_users_table()
	create_tags_table()
	create_img_table()
	create_chat_table()
	create_friends_table()
