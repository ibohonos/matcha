from app import app
from flask import session, redirect, request, jsonify
from app.models.comments import add_comment
from app.models.users import get_by_id


@app.route('/ajax_add_comment/', methods=['POST'])
def ajax_add_comment():
	id_user = session.get('id_user_logged')
	id_post = request.form.get('id_post')
	text = request.form.get('text')

	res = add_comment(id_user, id_post, text)
	user = get_by_id(id_user)
	if res:
		data = {
			'user_avatar': user['avatar'],
			'user_first_name': user['first_name'],
			'id_user': id_user,
			'id_post': id_post,
			'text': text
		}
		return jsonify(data)
	return "False"

