function chat_start()
{
    event.preventDefault();
    var chat_to = event.srcElement.parentNode.childNodes[2].innerHTML;
    var chat_from = $("#user_login").text();

    $.ajax({
		url: "/ajax_create_chat",
		data: {'chat_to': chat_to, 'chat_from': chat_from},
		type: 'POST',
		success: function(response)
		{
			var url = window.location.href + "chat";
            var form = $('<form action="' + url + '" method="post">' +
            '<input type="text" name="room_name" value="' + response + '" />' + '</form>');
            $('body').append(form);
            form.submit();
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}