function register(view_url)
{
	event.preventDefault();

	const email = document.getElementById("r_email_inp").value;
	const login = document.getElementById("r_login_inp").value;
	const pwd = document.getElementById("r_pwd_inp").value;

	$.ajax({
		url: view_url,
		data: {'email': email, 'login': login, 'pwd': pwd},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function login(view_url)
{
	event.preventDefault();

	const login = document.getElementById("l_login_inp").value;
	const pwd = document.getElementById("l_pwd_inp").value;

	$.ajax({
		url: view_url,
		data: {'login': login, 'pwd': pwd},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function recover(view_url)
{
	event.preventDefault();
	const login = document.getElementById("rec_login_inp").value;

	$.ajax({
		url: view_url,
		data: {'login': login},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function new_pwd(view_url, token, email)
{
	event.preventDefault();
	const pwd = document.getElementById("rec_pwd_inp").value;

	$.ajax({
		url: view_url,
		data: {'pwd': pwd, 'token': token, 'email': email},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}