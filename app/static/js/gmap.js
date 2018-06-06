function init_edit_Map() {
  let latitude = parseFloat($('#lat').val());
  let longitude = parseFloat($('#long').val());

  var uluru = {lat: latitude, lng: longitude};
  if (!document.getElementById('map_edit')){return};
  var map = new google.maps.Map(document.getElementById('map_edit'), {
	zoom: 10,
	center: uluru,
	zoomControl: true,
	scaleControl: false,
	scrollwheel: false,
	disableDoubleClickZoom: true
  });

  var marker = new google.maps.Marker({
	position: uluru,
	map: map,
    draggable:true,
    title:"Drag me!"
  });

  google.maps.event.addListener(marker, 'dragend', function (event) {
      document.getElementById("lat").value = event.latLng.lat();
      document.getElementById("long").value = event.latLng.lng();
  });

  $("#upd_loc_btn").click(function() {
  event.preventDefault();
  $.ajax({
            url: '/ajax_update_location',
            data: {'id_user': $("#user_id").text(), 'latitude': parseFloat($('#lat').val()), 'longitude': parseFloat($('#long').val())},
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
  });
  });
}


function init_UNIT_Map() {
  var uluru = {lat: 50.46883805910163, lng: 30.462166049957204};
  if (!document.getElementById('UNIT_Map')){return};
  var map = new google.maps.Map(document.getElementById('UNIT_Map'), {
	zoom: 10,
	center: uluru,
	zoomControl: true,
	scaleControl: false,
	scrollwheel: false,
	disableDoubleClickZoom: true
  });

  var marker = new google.maps.Marker({
	position: uluru,
	map: map,
    draggable:true,
    title:"Drag me!"
  });
}