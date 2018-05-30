function like(auth_id, post_id) {
	$.post('/ajax_like/', {
		'auth_id': auth_id,
		'post_id': post_id
	}).done(function (resp) {
		let like = $('#like' + post_id);
		let c_like = $('#like' + post_id + ' span');
		like.removeClass('text-green');
		like[0].removeEventListener("click", like);
		like[0].addEventListener("click", unlike);
		let value_like = parseInt(c_like[0].innerText) + 1;
		c_like[0].innerText = value_like;
		console.log(value_like);
		console.log(resp);
	});
}

function unlike(auth_id, post_id) {
	$.post('/ajax_unlike/', {
		'auth_id': auth_id,
		'post_id': post_id
	}).done(function (resp) {
		let like = $('#like' + post_id);
		let c_like = $('#like' + post_id + ' span');
		like.addClass('text-green');
		let value_like = c_like[0].innerText - 1;
		c_like[0].innerText = value_like;
		console.log(value_like);
		console.log(resp);
	});
}

