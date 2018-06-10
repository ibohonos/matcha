/**
 * Created by Roma on 10.06.2018.
 */

var age_from = $("#age_from");
var age_to = $("#age_to");
var fame_from = $("#fame_from");
var fame_to = $("#fame_to");
var country = $("#country");
var city = $("#city");
var tag_1 = $("#tag_1");
var tag_2 = $("#tag_2");
var tag_3 = $("#tag_3");


function re_sort(data) {
    // console.log(data);
}

$("#apply_filter_btn").click(function () {
    event.preventDefault();
    var sort = 'none';
    var sort_list = $(".active_arrow")[0];
    if (sort_list){
    	sort = sort_list.id;}
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': sort},
		type: 'POST',
		success: function(response)
		{
            re_sort(response);
		}
	});
});

$("#age_desc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'age_desc'},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#age_desc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#age_asc").click(function () {
   $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'age_asc'},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#age_asc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#dist_desc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'dist_desc'},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#dist_desc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#dist_asc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'dist_asc'},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#dist_asc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#rate_desc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'rate_desc'},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#rate_desc").addClass("active_arrow");
            re_sort(response);
		}
	});
});

$("#rate_asc").click(function () {
    $.ajax({
		url: '/ajax_filter_apply',
		data: {'age_from': age_from.val(), 'age_to': age_to.val(), 'fame_from': fame_from.val(), 'fame_to': fame_to.val(),
            'country': country.val(), 'city': city.val(), 'tag_1': tag_1.val(), 'tag_2': tag_2.val(), 'tag_3': tag_3.val(),
            'sort': 'rate_asc'},
		type: 'POST',
		success: function(response)
		{
            $(".fas").removeClass("active_arrow");
            $("#rate_asc").addClass("active_arrow");
            re_sort(response);
		}
	});
});