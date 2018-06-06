from app import app
from flask import session, render_template, redirect
from app.models.friendship import all_friends_request, all_friends
from app.models.users import get_user_by_id


@app.route('/friends/')
def friends():
	if session.get('id_user_logged'):
		data = {
			'user': get_user_by_id(session.get('id_user_logged')),
			'get_by_id': get_user_by_id,
			'friends': all_friends_request(session.get('id_user_logged')),
			"all_friends": all_friends(session.get("id_user_logged"))
		}
		return render_template("newsfeed-friends.html", data=data)
	return redirect("/")


@app.route('/images/')
def images():
	if not session.get('id_user_logged'):
		return redirect('/')
	user = get_user_by_id(session.get('id_user_logged'))
	data = {
		'user': user,
		'all_friends': all_friends(user['id_user'])
	}
	return render_template("newsfeed-images.html", data=data)

