from app import app
from flask import session, redirect, request
from app.models.posts import create_post, all_user_post


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

	create_post(user_id, auth_id, "text", "public", content, None, None)

	return "post created"

