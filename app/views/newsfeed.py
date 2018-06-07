from app import app
from flask import session, render_template, redirect
from app.models.friendship import all_friends_request, all_friends
from app.models.users import get_user_by_id, get_users_and_locations


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


@app.route('/people_nearby/')
def people_nearby():
	if not session.get('id_user_logged'):
		return redirect('/')
	id_user = session.get('id_user_logged')
	user = get_user_by_id(id_user)

	users_list = get_users_and_locations(id_user)
	friends_list = all_friends(id_user)

	friends_id = []
	for i in friends_list:
		if i['id_requester'] != id_user:
			friends_id.append(i['id_requester'])
		if i['id_user_requested'] != id_user:
			friends_id.append(i['id_user_requested'])

	not_friends = []
	for user in users_list:
		if user['id_user'] not in friends_id:
			not_friends.append(user)

	data = {
		'user': user,
		'all_friends': all_friends(user['id_user']),
		'not_friends': not_friends
	}
	return render_template("newsfeed-people-nearby.html", data=data)