from app import app, socketio
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask import Flask, render_template, request, session, redirect, url_for


@app.route('/chat')
def chat():
	if not session.get('id_user_logged'):
		return redirect(url_for('index'))

	if session.get('id_user_logged') == 1 or session.get('id_user_logged') == 3:
		context = {'chat_room': 'test_room_1_2'}
	else:
		context = {'chat_room': 'room_for_all'}
	return render_template('newsfeed-messages.html', context=context)


# @socketio.on('message')
# def handleMessage(msg, user):
# 	print('Message: ' + msg)
# 	msg = html.escape(msg)
# 	send(msg, broadcast=True)


chat_users_sid_to_id = {}
chat_users_sid_to_room = {}


@socketio.on('test_print', namespace='/chat')
def test_print(msg):
	print(msg['room'])


@socketio.on('message', namespace='/chat')
def message(msg):
	print(msg)
	room = chat_users_sid_to_room[request.sid]
	emit('message_from_server', msg, room=room)


@socketio.on('connect', namespace='/chat')
def connect():
	chat_users_sid_to_id[request.sid] = session.get('id_user_logged')
	print("connected")


@socketio.on('disconnect', namespace='/chat')
def disconnect():
	chat_users_sid_to_id.pop(request.sid)
	room = chat_users_sid_to_room[request.sid]
	leave_room(room)
	chat_users_sid_to_room.pop(request.sid)


@socketio.on('join_room', namespace='/chat')
def test_print(data):
	join_room(data['room'])
	chat_users_sid_to_room[request.sid] = data['room']

	print("sid:" + request.sid + " joined room " + data['room'])
	print(chat_users_sid_to_id)
	print(chat_users_sid_to_room)
