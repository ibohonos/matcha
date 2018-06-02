from app import app
from flask import request, session
from app.models.likes import like, dislike, unlike, undislike, liked, disliked


@app.route('/ajax_like/', methods=['POST'])
def ajax_like():
	id_user = session.get('id_user_logged')
	id_post = request.form.get('post_id')

	if id_user:
		if liked(id_user, id_post):
			res = unlike(id_user, id_post)
			if not res:
				return "unliked"
		else:
			res = like(id_user, id_post)
			if not res:
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
				return "undisliked"
		else:
			res = dislike(id_user, id_post)
			if not res:
				return "disliked"
	return "Fail"

