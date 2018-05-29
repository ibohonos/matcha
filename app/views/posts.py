from app import app
from flask import session, redirect, request, jsonify
from app.models.posts import create_post, all_user_post
from app.models.users import get_by_id


@app.route('/ajax_all_posts')
def ajax_all_posts():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	return "all posts"


@app.route('/ajax_create_post', methods=['POST'])
def ajax_create_post():
	content = request.form.get('content')
	auth_id = request.form.get('auth_id')
	user_id = request.form.get('user_id')

	res = create_post(user_id, auth_id, "text", "public", content, None, None)
	user = get_by_id(auth_id)
	user_first_name = user['first_name']
	user_last_name = user['last_name']
	user_avatar = user['avatar']
	if res:
		data = {
			'user_avatar': user_avatar,
			'user_first_name': user_first_name,
			'user_last_name': user_last_name,
			'auth_id': auth_id,
			'type': "text",
			'content': content,
			'id_post': res
		}
		return jsonify(data)
	return "Fail"

