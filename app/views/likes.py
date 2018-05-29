from app import app
from flask import request
from app.models.likes import like, dislike, unlike, undislike


@app.route('/ajax_like/', methods=['POST'])
def ajax_like():
	id_user = request.form.get('auth_id')
	id_post = request.form.get('post_id')

	res = like(id_user, id_post)
	if not res:
		return "Success"
	return "Fail"


@app.route('/ajax_unlike/', methods=['POST'])
def ajax_unlike():
	id_user = request.form.get('auth_id')
	id_post = request.form.get('post_id')

	res = unlike(id_user, id_post)
	if not res:
		return "Success"
	return "Fail"

