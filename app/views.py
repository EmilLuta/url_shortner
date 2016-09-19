from app import app, db
from app.services import URLService

from flask import redirect, request, Response

@app.route('/<string:url>', methods=['POST'])
def create_url_entry(url):
	if 'url' not in request.json:
		return Response(status=400)
	else:
		url_entry = URLServices.find_or_create_entry(request.json['url'])
		response = Response(status=302)
		response.set_cookie(url_entry.url_hash, url_entry.prefix + url_entry.url)
		return response

@app.route('/<key>', methods=['GET'])
def redirect_route(key):
	if key in request.cookies:
		return redirect(request.cookies[key])
	else:
		try:
			url_entry = URLEntry.query.filter_by(url_hash=key).first()
		except:
			url_entry = URLEntry(url_hash=key, url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
		
		return redirect(url_entry.url)
