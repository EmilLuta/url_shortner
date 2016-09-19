from app import app, db
from app.models import URLEntry

from flask import redirect, request, Response

@app.route('/<string:key>', methods=['POST'])
def create_url_entry(key):
	data = request.json
	url_entry = URLEntry(url=data['url'], url_hash=data['url'])
	db.session.add(url_entry)
	db.session.commit()
	response = Response(status=302)
	response.set_cookie(data['url'], data['url'])
	return response

@app.route('/<url>', methods=['GET'])
def redirect_route(url):
	return redirect(url)
