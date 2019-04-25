import pymysql
from pymysql import Error

db_host = 'localhost'
db_name = 'sites_matcha'
db_user = 'sites_matcha'
db_password = 'qfh6cHktW0'
db_port = 3306
db_socket = "/var/run/mysqld/mysqld.sock"


def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d


def db_connect(sql, arguments=None):
	# create a database connection to a SQLite database
	sql = sql.replace('?', '%s')
	conn = pymysql.connect(
		host=db_host,
		user=db_user,
		password=db_password,
		database=db_name,
		port=db_port,
		unix_socket=db_socket,
		cursorclass=pymysql.cursors.DictCursor
	)
	conn.row_factory = dict_factory

	print("============= db_connect ===============")
	print(sql)
	print(arguments)
	print("========================================")
	try:
		with conn.cursor() as cursor:
			# Create a new record
			if arguments:
				cursor.execute(sql, arguments)
			else:
				cursor.execute(sql)
		conn.commit()
		return cursor.fetchall()
	except Error as e:
		return e
	finally:
		conn.close()


def db_insert(sql, arguments=None):
	# create a database connection to a SQLite database
	sql = sql.replace('?', '%s')
	conn = pymysql.connect(
		host=db_host,
		user=db_user,
		password=db_password,
		database=db_name,
		port=db_port,
		unix_socket=db_socket,
		cursorclass=pymysql.cursors.DictCursor
	)
	conn.row_factory = dict_factory

	try:
		with conn.cursor() as cursor:
			# Create a new record
			if arguments:
				cursor.execute(sql, arguments)
			else:
				cursor.execute(sql)

		# connection is not autocommit by default. So you must commit to save
		# your changes.
		conn.commit()
		return cursor.lastrowid
	except Error as e:
		return e
	finally:
		conn.close()
