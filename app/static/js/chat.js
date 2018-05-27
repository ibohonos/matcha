var socket = io.connect('http://' + document.domain + ':' + location.port);
var chat_socket = io('http://' + document.domain + ':' + location.port + '/chat');
var room = $("#chat_room").text();


$('#mesage_submit').on('click', function(){

    var message = $("#message_input").val();
    if (!message){return;}
    var data =  {'login': 'login', 'message': message};
	chat_socket.emit('message', message);
	$("#message_input").val("");
});

chat_socket.on('message_from_server', function(msg)
{
	$("#chat_body").append('<li class="left"><img src="http://placehold.it/300x300" alt=""class="profile-photo-sm pull-left"><div class="chat-item"><div class="chat-item-header"><h5>Linda Lohan</h5><small class="text-muted">3 days ago</small></div><p>' +
	msg + '</p></div></li>');
});

chat_socket.on('connect', function()
{
	chat_socket.emit('join_room', {'room': room});
});
