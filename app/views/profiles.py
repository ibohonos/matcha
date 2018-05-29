from app import app
from flask import render_template, session, redirect, request
from app.models.users import get_by_id, get_about
from app.models.friendship import *
from app.models.posts import all_user_post
from app.models.comments import all_post_comments
from app.models.likes import like, liked, dislike, disliked, undislike, unlike, len_post_dislikes, len_post_likes


@app.route('/profile/')
@app.route('/user/id<int:id_user>/')
def profile(id_user=None):
	if not session.get('user_data') and not id_user:
		return redirect('/')
	if id_user:
		user = get_by_id(id_user)
		posts = all_user_post(id_user)
	else:
		user = session.get('user_data')
		posts = all_user_post(session.get('id_user_logged'))
	if session.get('user_data'):
		user_cur = session.get('user_data')
	else:
		user_cur = None

	data = {
		'user': user,
		'user_cur': user_cur,
		'posts': posts,
		'get_by_id': get_by_id,
		'all_post_comments': all_post_comments,
		'len_post_likes': len_post_likes,
		'len_post_dislikes': len_post_dislikes,
		'like': like,
		'dislike': dislike,
		'liked': liked,
		'disliked': disliked,
		'unlike': unlike,
		'undislike': undislike
	}
	return render_template('timeline.html', data=data)


@app.route('/profile/edit/basic/')
def edit_profile():
	if session.get('id_user_logged'):
		data = {'user': session.get('user_data'), 'about': get_about(session.get('id_user_logged'))}
		return render_template('edit-profile-basic.html', data=data)
	return redirect('/')


@app.route('/profile/edit/work/')
def edit_profile_work():
	if session.get('id_user_logged'):
		data = {'user': session.get('user_data'), 'about': get_about(session.get('id_user_logged'))}
		return render_template('edit-profile-work-edu.html', data=data)
	return redirect('/')


@app.route('/profile/edit/interests/')
def edit_profile_interests():
	if session.get('id_user_logged'):
		data = {'user': session.get('user_data'), 'about': get_about(session.get('id_user_logged'))}
		return render_template('edit-profile-interests.html', data=data)
	return redirect('/')


@app.route('/profile/edit/settings/')
def edit_profile_settings():
	if session.get('id_user_logged'):
		data = {'user': session.get('user_data'), 'about': get_about(session.get('id_user_logged'))}
		return render_template('edit-profile-settings.html', data=data)
	return redirect('/')


@app.route('/profile/edit/password/')
def edit_profile_password():
	if session.get('id_user_logged'):
		data = {'user': session.get('user_data'), 'about': get_about(session.get('id_user_logged'))}
		return render_template('edit-profile-password.html', data=data)
	return redirect('/')


def is_friends_with(auth_id, user_id):
	user = check_friends(auth_id, user_id)
	if user:
		return user
	return "0"


@app.route('/ajax_check_friends/')
def ajax_check_friends():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')
	user1 = is_friends_with(auth_id, user_id)
	user2 = is_friends_with(user_id, auth_id)

	if auth_id == user_id:
		return "same user"
	if user1 == "0":
		if user2 == "0":
			return "0"
		else:
			if user2['status'] == 0:
				return "pending"
			else:
				return "1"
	else:
		if user1['status'] == 0:
			return "waiting"
		else:
			return "1"


@app.route('/ajax_delete_user_request/')
def ajax_delete_user_request():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	delete_user_request(auth_id, user_id)
	return ajax_check_friends()


@app.route('/ajax_add_user_request/')
def ajax_add_user_request():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	add_friend(auth_id, user_id)
	return ajax_check_friends()


@app.route('/ajax_confirm_user_request/')
def ajax_confirm_user_request():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	confirm_user_request(user_id, auth_id)
	return ajax_check_friends()


@app.route('/ajax_delete_user_friend/')
def ajax_delete_user_friend():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	delete_user_request(auth_id, user_id)
	delete_user_request(user_id, auth_id)
	return ajax_check_friends()


@app.route('/profile/about/')
@app.route('/user/id<int:id_user>/about/')
def about(id_user=None):
	if not session.get('user_data') and not id_user:
		return redirect('/')
	if id_user:
		user = get_by_id(id_user)
	else:
		user = session.get('user_data')
	data = {'user': user}
	return render_template("timeline-about.html", data=data)


