from app import app
from flask import session, request, jsonify
import html
from app.models.posts import create_post, get_post_by_id, dell_post
from app.models.users import get_user_by_id
from app.models.likes import dell_post_likes, dell_post_dislikes
from app.models.comments import dell_post_comments


@app.route('/ajax_create_post', methods=['POST'])
def ajax_create_post():
	content = html.escape(request.form.get('content'))
	auth_id = session.get('id_user_logged')
	user_id = request.form.get('user_id')

	if content:
		user = get_user_by_id(auth_id)
		if user and user['active']:
			res = create_post(user_id, auth_id, "text", "public", content, None, None)
			if res:
				user_first_name = user['first_name']
				user_last_name = user['last_name']
				user_avatar = user['avatar']
				post = get_post_by_id(res)
				if post:
					data = {
						'user_avatar': user_avatar,
						'user_first_name': user_first_name,
						'user_last_name': user_last_name,
						'auth_id': auth_id,
						'type': "text",
						'content': content,
						'id_post': res,
						'date_creation': post['date_creation'].split(" ")[0],
						'time_creation': post['date_creation'].split(" ")[1]
					}
					return jsonify(data)
	return "Fail"


@app.route('/ajax_dell_post/', methods=['POST'])
def ajax_dell_post():
	if session.get('id_user_logged'):
		post_id = request.form.get('id_post')
		auth_id = session.get('id_user_logged')

		res = get_post_by_id(post_id)
		if res and (res['id_user'] == auth_id or res['id_user_from'] == auth_id):
			dell = dell_post(post_id)
			if not dell:
				likes = dell_post_likes(post_id)
				if not likes:
					dislikes = dell_post_dislikes(post_id)
					if not dislikes:
						comment = dell_post_comments(post_id)
						if not comment:
							return "deleted"
	return "Fail"

