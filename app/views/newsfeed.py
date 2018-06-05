from app import app
from flask import session, render_template, redirect
from app.models.friendship import all_friends_request, all_friends


@app.route('/friends/')
def friends():
	if session.get('id_user_logged'):
		data = {
			'friends': all_friends_request(session.get('id_user_requested')),
			"all_friends": all_friends(session.get("id_user_requested"))
		}
		return render_template("newsfeed-friends.html", data=data)
	return redirect("/")

