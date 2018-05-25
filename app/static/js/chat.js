var socket = io.connect('http://' + document.domain + ':' + location.port);
var chat_socket = io('http://' + document.domain + ':' + location.port + '/chat');
var room = $("#chat_room").text();

$('#mesage_submit').on('click', function(){
    var message = $("#message_input").val()
    if (!message){return;}

	chat_socket.emit('message', message);
	$("#message_input").val("");
});

chat_socket.on('message_from_server', function(msg)
{
	$("#chat_list").append("<li>"+msg+"</li>");
});

chat_socket.on('connect', function()
{
	chat_socket.emit('join_room', {'room': room});
});


//socket.on('disconnect', function ()
//{
//	chat_socket.emit('test_print', "left");
//});

