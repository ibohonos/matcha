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
		let all_posts = $("#all_posts");
		let data = '<div class="post-content"><!--Post Date--><div class="post-date hidden-xs hidden-sm"><h5>' + resp.user_first_name + '</h5><p class="text-grey">Sometimes ago</p></div><!--Post Date End--><div class="post-container"><img src="' + resp.user_avatar + '" alt="user" class="profile-photo-md pull-left" /><div class="post-detail"><div class="user-info"><h5><a href="/user/id' + resp.auth_id + '" class="profile-link">' + resp.user_first_name + ' ' + resp.user_last_name + '</a> <span class="following">following</span></h5><p class="text-muted">Published a ' + resp.type + ' about 15 mins ago</p></div><div class="reaction"><a class="btn text-green"><i class="icon ion-thumbsup"></i> 0</a><a class="btn text-red"><i class="fa fa-thumbs-down"></i> 0</a></div><div class="line-divider"></div><div class="post-text"><p>' + resp.content + '</p></div><div class="line-divider"></div><div class="post-comment"><img src="' + resp.user_avatar + '" alt="" class="profile-photo-sm" /><input type="text" class="form-control" placeholder="Post a comment"></div></div></div></div>';
		all_posts.prepend(data);
		console.log(all_posts);
		console.log(resp);
	});
}
