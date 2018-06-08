from app import app
from flask import request, session
from app.models.likes import like, dislike, unlike, undislike, liked, disliked
from app.views.notifications import add_notification


@app.route('/ajax_like/', methods=['POST'])
def ajax_like():
	id_user = session.get('id_user_logged')
	id_post = request.form.get('post_id')

	if id_user:
		if liked(id_user, id_post):
			res = unlike(id_user, id_post)
			if not res:
				if session.get('id_user_logged') and not id_user == session.get('id_user_logged'):
					msg = "User: " + session.get('user_data')['first_name'] + " " + session.get('user_data')['last_name'] + " unlike your post"
					add_notification(id_user, msg)
				return "unliked"
		else:
			res = like(id_user, id_post)
			if not res:
				if session.get('id_user_logged') and not id_user == session.get('id_user_logged'):
					msg = "User: " + session.get('user_data')['first_name'] + " " + session.get('user_data')['last_name'] + " like your post"
					add_notification(id_user, msg)
				return "liked"
	return "Fail"


@app.route('/ajax_dislike/', methods=['POST'])
def ajax_dislike():
	id_user = session.get('id_user_logged')
	id_post = request.form.get('post_id')

	if id_user:
		if disliked(id_user, id_post):
			res = undislike(id_user, id_post)
			if not res:
				if session.get('id_user_logged') and not id_user == session.get('id_user_logged'):
					msg = "User: " + session.get('user_data')['first_name'] + " " + session.get('user_data')['last_name'] + " undislike your post"
					add_notification(id_user, msg)
				return "undisliked"
		else:
			res = dislike(id_user, id_post)
			if not res:
				if session.get('id_user_logged') and not id_user == session.get('id_user_logged'):
					msg = "User: " + session.get('user_data')['first_name'] + " " + session.get('user_data')['last_name'] + " dislike your post"
					add_notification(id_user, msg)
				return "disliked"
	return "Fail"

