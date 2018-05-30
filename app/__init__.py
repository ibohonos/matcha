import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_mail import Mail, Message
from flask_socketio import SocketIO
from app.models.users import get_user_by_id


app = Flask(__name__)

app.secret_key = os.urandom(16)
socketio = SocketIO(app)
app.config.update(dict(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=587,
	MAIL_USE_TLS=True,
	MAIL_USE_SSL=False,
	MAIL_USERNAME='rkhilenksmtp@gmail.com',
	MAIL_PASSWORD='asdQWE123',
))
mail = Mail(app)

from app.views import newsfeed, login, chat, profiles, posts, friends, comments, likes, notifications


@app.route('/')
def index():
	if session.get('id_user_logged'):
		return render_template('newsfeed.html', user=session.get('user_data'))
	return render_template('index-register.html')

# app.add_url_rule("/test2", "test2", test2, methods=['GET', 'POST'])

# rkhilenksmtp@gmail.com
# asdQWE123
