var auth_id = $("#auth_id")[0].innerText;
var user_id = $("#user_id")[0].innerText;
var friends_button = $("#friends_request button");

$(document).ready(function () {
	if (auth_id !== "None") {
		$.get("/ajax_check_friends/", {
			'user_id': user_id
		})
		.done(function(response)
		{
			friends_status(response);
		});
	}
	else {
		$("#friends_request").addClass("hidden");
	}
});

function friends_status(response) {
	let friends_button_class = friends_button[0].classList.toString();
	var test = friends_button_class.split(" ");

	if (response === "waiting") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-warning");
		friends_button.on('click', delete_user_request);
		friends_button[0].innerText = "Delete request";
	}
	else if (response === "pending") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-success");
		friends_button.on('click', confirm_user_request);
		friends_button[0].innerText = "Confirm request";
	}
	else if (response === "0") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-primary");
		friends_button.on('click', add_user_request);
		friends_button[0].innerText = "Add friend";
	}
	else if (response === "1") {
		for (let i = 0; i < test.length; i++) {
			friends_button[0].classList.remove(test[i]);
		}
		friends_button.addClass("btn-my");
		friends_button.addClass("btn-default");
		friends_button.on('click', delete_user_friend);
		friends_button[0].innerText = "You are friends";
	}
	else if (response === "same user") {
		$("#friends_request").addClass("hidden");
	}
}

function delete_user_request() {
	$.get("/ajax_delete_user_request", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let test = friends_button_class.split(" ");

		if (response === "0") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-primary");
			friends_button.on('click', add_user_request);
			friends_button[0].innerText = "Add friend";
		}
	});
}

function confirm_user_request() {
	$.get("/ajax_confirm_user_request", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let test = friends_button_class.split(" ");

		if (response === "1") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-default");
			friends_button.on('click', delete_user_friend);
			friends_button[0].innerText = "You are friends";
		}
	});
}

function add_user_request() {
	$.get("/ajax_add_user_request", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let test = friends_button_class.split(" ");

		if (response === "waiting") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-warning");
			friends_button.on('click', delete_user_request);
			friends_button[0].innerText = "Delete request";
		}
	});
}

function delete_user_friend() {
	$.get("/ajax_delete_user_friend", {
		'user_id': user_id
	})
	.done(function(response)
	{
		let friends_button_class = friends_button[0].classList.toString();
		let test = friends_button_class.split(" ");

		if (response === "0") {
			for (let i = 0; i < test.length; i++) {
				friends_button[0].classList.remove(test[i]);
			}
			friends_button.addClass("btn-my");
			friends_button.addClass("btn-primary");
			friends_button.on('click', add_user_request);
			friends_button[0].innerText = "Add friend";
		}
	});
}
