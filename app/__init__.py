import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_mail import Mail, Message
from flask_socketio import SocketIO
from app.models.users import get_user_by_id
from app.models.posts import all_user_post
from app.models.friendship import all_friends
from app.models.comments import all_post_comments
from app.models.likes import liked, disliked, len_post_likes, len_post_dislikes

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

from app.views import newsfeed, login, chat, profiles, posts, friends, comments, likes, notifications, tags, geolocation


@app.route('/')
def index():
	if session.get('id_user_logged'):
		data = {
			'all_posts': all_user_post,
			'all_friends': all_friends(session.get('id_user_logged')),
			"get_user_by_id": get_user_by_id,
			"all_post_comments": all_post_comments,
			"liked": liked,
			"disliked": disliked,
			"len_post_likes": len_post_likes,
			"len_post_dislikes": len_post_dislikes
		}
		return render_template('newsfeed.html', data=data)
	return render_template('index-register.html')

# app.add_url_rule("/test2", "test2", test2, methods=['GET', 'POST'])

# rkhilenksmtp@gmail.com
# asdQWE123
