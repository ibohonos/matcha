from app import app
from flask import request, session, url_for, render_template
from app.models.location import *


@app.route('/ajax_set_location', methods=['POST'])
def ajax_set_location():
	res = set_coords_to_id(int(request.form.get('id_user')), request.form.get('latitude'), request.form.get('longitude'))
	if not res:
		session['location'] = get_location_by_id(int(request.form.get('id_user')))
	return "response"


@app.route('/ajax_update_location', methods=['POST'])
def ajax_update_location():
	res = update_coords_by_id(int(request.form.get('id_user')), request.form.get('latitude'), request.form.get('longitude'))
	print(res)
	if not res:
		session['location'] = get_location_by_id(int(request.form.get('id_user')))
	print(get_location_by_id(int(request.form.get('id_user'))))
	return "response"
