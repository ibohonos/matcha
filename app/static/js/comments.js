function add_comment(form) {
	let id_post = form.id_post.value;
	let text = form.comment.value;

	$.post('/ajax_add_comment/', {
		'id_post': id_post,
		'text': text
	}).done(function (resp) {
		form.comment.value = "";
		let all_comments = $('#all_comments' + resp.id_post);
		let data = "<div class=\"post-comment\">" +
			"<img src=\"" + resp.user_avatar + "\" class=\"profile-photo-sm\" />" +
			"<a href=\"/user/id" + resp.id_user + "\" class=\"profile-link\">" + resp.user_first_name + "</a>" +
			"<p>&nbsp;&nbsp;" + resp.text + "</p>" +
		"</div>";
		all_comments.prepend(data);
	});
}