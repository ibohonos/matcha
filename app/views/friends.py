from app import app
from flask import render_template, session


@app.route('/profile/friends/')
@app.route('/user/id<int:id_user>/friends/')
def user_friends(id_user=None):
	if id_user:
		print("hello")
	else:
		print("not hello")
	if session.get('user_data'):
		print("hello log")
	else:
		print("hello not log")
	return render_template("timeline-friends.html")

