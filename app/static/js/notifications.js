io.connect('http://' + document.domain + ':' + location.port);
var notif_socket = io('http://' + document.domain + ':' + location.port + '/notifications');


chat_socket.on('connect', function()
{
	notif_socket.emit('join_room', {'room': "asd"});
});