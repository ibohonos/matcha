function register(view_url)
{
	event.preventDefault();

	$.ajax({
		url: view_url,
		data: {title: 'hallo', article: 'test'},
		type: 'POST',
		success: function(response) {
			console.log(response);
		},
		error: function(error) {
			console.log(error);
		}
	});
}

function ready(data)
{
	alert(data);
}