from config.databse import db_connect


def create_users_table():
    res = db_connect('''
        CREATE TABLE IF NOT EXISTS users (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        login VARCHAR(255) NOT NULL UNIQUE,
        date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
        active BOOLEAN DEFAULT 0 NOT NULL,
        token VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        gender INT NOT NULL DEFAULT 1,
        sex_pref INT,
        biography TEXT)
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
        img_src VARCHAR(255) NOT NULL,
        avatar BOOLEAN DEFAULT 0 NOT NULL,
        date_creation DATETIME DEFAULT CURRENT_TIMESTAMP)
        ''')
    if res:
        print(res)
    else:
        print("tags ok")

    res = db_connect('''
        CREATE TABLE IF NOT EXISTS images_con (
        id_img INTEGER NOT NULL,
        id_user INTEGER NOT NULL,
        FOREIGN KEY (id_img) REFERENCES images(id_img) ON DELETE CASCADE,
        FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE)
        ''')
    if res:
        print(res)
    else:
        print("tags_con ok")


if __name__ == '__main__':
    create_users_table()
    create_tags_table()
