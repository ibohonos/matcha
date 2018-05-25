from app import app
from flask import render_template, session, redirect
from app.models.users import get_by_id


@app.route('/profile/')
@app.route('/user/id<int:id_user>')
def profile(id_user=None):
	if session.get('id_user_logged'):
		if id_user:
			return render_template('timeline.html', user=get_by_id(id_user), user_cur=session.get('user_data'))
		return render_template('timeline.html', user=session.get('user_data'), user_cur=session.get('user_data'))
	if id_user:
		return render_template('timeline.html', user=get_by_id(id_user), user_cur=None)
	return redirect('/')


@app.route('/profile/edit/')
def edit_profile():
	if session.get('id_user_logged'):
		return render_template('edit-profile-basic.html', user=session.get('user_data'))
	return redirect('/')
