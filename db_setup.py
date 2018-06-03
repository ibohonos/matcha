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
		theme VARCHAR(255) NOT NULL DEFAULT "light",
		date_birth DATE,
		active BOOLEAN DEFAULT 0,
		token VARCHAR(255),
		gender INT NOT NULL DEFAULT 1,
		sex_pref INT,
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
		room_name VARCHAR(255) NOT NULL UNIQUE)
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


def create_posts_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS posts (
		id_post INTEGER PRIMARY KEY AUTOINCREMENT,
		id_user INTEGER NOT NULL,
		id_user_from INTEGER NOT NULL,
		`type` VARCHAR(255) NOT NULL,
		status VARCHAR(255) NOT NULL DEFAULT "public",
		content TEXT DEFAULT NULL,
		img VARCHAR(255) DEFAULT NULL,
		video VARCHAR(255) DEFAULT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE,
		FOREIGN KEY (id_user_from) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("posts ok")


def create_about_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS about (
		id_about INTEGER PRIMARY KEY AUTOINCREMENT,
		id_user INTEGER NOT NULL,
		biography TEXT DEFAULT NULL,
		location VARCHAR(255) DEFAULT NULL,
		`language` VARCHAR(255) DEFAULT NULL,
		phone VARCHAR(255) DEFAULT NULL,
		status VARCHAR(255) DEFAULT NULL,
		political VARCHAR(255) DEFAULT NULL,
		fb VARCHAR(255) DEFAULT NULL,
		tw VARCHAR(255) DEFAULT NULL,
		inst VARCHAR(255) DEFAULT NULL,
		site VARCHAR(255) DEFAULT NULL,
		hobbies TEXT DEFAULT NULL,
		tv_shows TEXT DEFAULT NULL,
		movies TEXT DEFAULT NULL,
		games TEXT DEFAULT NULL,
		music TEXT DEFAULT NULL,
		books TEXT DEFAULT NULL,
		writers TEXT DEFAULT NULL,
		others TEXT DEFAULT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
 		''')
	if res:
		print(res)
	else:
		print("about ok")


def create_messages_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS messages (
		id_message INTEGER PRIMARY KEY AUTOINCREMENT,
		id_chat_room INTEGER NOT NULL,
		id_user_from INTEGER NOT NULL,
		id_user_to INTEGER NOT NULL,
		message TEXT NOT NULL,
		read_status BOOLEAN DEFAULT 0,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_user_from) REFERENCES users(id_user) ON DELETE CASCADE,
		FOREIGN KEY (id_user_to) REFERENCES users(id_user) ON DELETE CASCADE,
		FOREIGN KEY (id_chat_room) REFERENCES chat_room(id_chat_room) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("messages ok")


def create_comments_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS comments (
		id_comment INTEGER PRIMARY KEY AUTOINCREMENT,
		id_user INTEGER NOT NULL,
		id_post INTEGER NOT NULL,
		text TEXT DEFAULT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_post) REFERENCES posts(id_post) ON DELETE CASCADE,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("comments ok")


def create_likes_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS likes (
		id_user INTEGER NOT NULL,
		id_post INTEGER NOT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_post) REFERENCES posts(id_post) ON DELETE CASCADE,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("likes ok")


def create_dislikes_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS dislikes (
		id_user INTEGER NOT NULL,
		id_post INTEGER NOT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_post) REFERENCES posts(id_post) ON DELETE CASCADE,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("dislikes ok")


def create_notifications_table():
	res = db_connect('''
		CREATE TABLE IF NOT EXISTS notifications (
		id_notif INTEGER PRIMARY KEY AUTOINCREMENT,
		id_user INTEGER NOT NULL,
		notification TEXT NOT NULL,
		date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
		''')
	if res:
		print(res)
	else:
		print("notifications ok")


if __name__ == '__main__':
	create_users_table()
	create_tags_table()
	create_img_table()
	create_chat_table()
	create_friends_table()
	create_posts_table()
	create_about_table()
	create_comments_table()
	create_likes_table()
	create_dislikes_table()
	create_messages_table()
	create_notifications_table()
