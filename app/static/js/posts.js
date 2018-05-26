var auth_id = $("#auth_id")[0].innerText;
var user_id = $("#user_id")[0].innerText;
var create_post_form = $("#create_post");
var create_post_button = $("#create_post button");

$(document).ready(function () {
	$.get('/ajax_all_posts', {
		'auth_id': auth_id,
		'user_id': user_id
	}).done(function (resp) {
		console.log(resp);
	});
});

function create_post_action(form) {
	let content = $("#content");
	$.post('/ajax_create_post', {
		'content': content.val(),
		'auth_id': auth_id,
		'user_id': user_id
	}).done(function (resp) {
		content.val("");
		console.log(resp);
	});
}
