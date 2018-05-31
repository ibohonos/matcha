from app import app, socketio
from app.models.notifications import *
from flask import Flask, render_template, request, session, redirect, url_for, make_response
from flask_socketio import SocketIO, join_room, leave_room, emit, send

notif_users_sid_to_id = {}


def add_notification(id_user, notif_text):
	if not check_notification_in_db(id_user, notif_text):
		add_notification_to_db(id_user, notif_text)

		notifications = get_notifications_by_user_id(id_user)

		for key, value in notif_users_sid_to_id.items():
			print(key)
			print(value)
			if str(value) == str(id_user):
				emit('check_notifications', notifications, namespace='/notifications', room=key)


@socketio.on('connect', namespace='/notifications')
def connect():
	notif_users_sid_to_id[request.sid] = session.get('id_user_logged')
	print("connect to notifications")


@socketio.on('disconnect', namespace='/notifications')
def disconnect():
	notif_users_sid_to_id.pop(request.sid)
	print("disconect from notifications")

