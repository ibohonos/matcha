function register(view_url)
{
	event.preventDefault();
	var error = 0;
	first_name = $("#firstname").val();
	last_name = $("#lastname").val();
	login = $("#r_login").val();
	email = $("#email").val();
	pasword = $("#password").val();
	var gender;

	if ($('input[id=male]:checked').val() == 'on')
	{gender = 1;}
	else
	{gender = 2;}

	day = $("#day").val()
	month = $("#month").val()
	year = $("#year").val()

	$("#firstname").removeClass("unvalid");
	$("#lastname").removeClass("unvalid");
	$("#r_login").removeClass("unvalid");
	$("#email").removeClass("unvalid");
	$("#password").removeClass("unvalid");
	$("#day").removeClass("unvalid");
	$("#month").removeClass("unvalid");
	$("#year").removeClass("unvalid");


	if (first_name.length < 3 || first_name.length > 20)
	{$("#firstname").addClass("unvalid");
		error = 1;}

	if (last_name.length < 3 || last_name.length > 20)
	{$("#lastname").addClass("unvalid");
		error = 1;}

	if (login.length < 3 || login.length > 30)
	{$("#r_login").addClass("unvalid");
		error = 1;}

	if (email.length < 3 || email.length > 30)
	{$("#email").addClass("unvalid");
		error = 1;}

	if (pasword.length < 6 || pasword.length > 40)
	{$("#password").addClass("unvalid");
		error = 1;}

	if (!day)
	{$("#day").addClass("unvalid");
		error = 1;}
	if (!month)
	{$("#month").addClass("unvalid");
		error = 1;}
	if (!year)
	{$("#year").addClass("unvalid");
		error = 1;}

	$.ajax({
		url: view_url,
		data: {'email': email, 'login': login, 'pwd': pwd, 'first_name': first_name, 'last_name': last_name, 'day': day,
		'month': month, 'year': year, 'gender': gender},
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

$("#forg_pwd_btn").click(function(){
	event.preventDefault();
	$("#login").toggleClass("active");
	$("#forgot_pwd").toggleClass("active");
})

$("#rem_pwd_btn").click(function(){
	event.preventDefault();
	$("#login").toggleClass("active");
	$("#forgot_pwd").toggleClass("active");
})

$("#register_btm").click()