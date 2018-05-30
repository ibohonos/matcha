from app import app, socketio
from app.models.notifications import *
from flask import Flask, render_template, request, session, redirect, url_for

notif_users_sid_to_id = {}


def add_notification(id_user, notif_text):
	print(id_user)
	print(notif_text)
	if not check_notification_in_db(id_user, notif_text):
		add_notification_to_db(id_user, notif_text)


@socketio.on('connect', namespace='/notifications')
def connect():
	notif_users_sid_to_id[request.sid] = session.get('id_user_logged')
	print("connect to notifications")


@socketio.on('disconnect', namespace='/notifications')
def disconnect():
	notif_users_sid_to_id.pop(request.sid)
	print("disconect from notifications")
