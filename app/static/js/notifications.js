io.connect('http://' + document.domain + ':' + location.port);
var notif_socket = io('http://' + document.domain + ':' + location.port + '/notifications');


notif_socket.on('connect', function()
{
	notif_socket.emit('join_room', {'room': "asd"});
});

notif_socket.on('check_notifications', function(data)
{
    alert("notification");
    console.log(data);
});

$("#notification_red").click(function () {
    event.preventDefault();


    $.ajax({
		url: ajax_clear_notifications,
		data: {'id_user': $('#user_id').text()},
		type: 'POST',
		success: function(response)
		{
			console.log(error);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
})