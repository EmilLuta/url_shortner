from app import app, db
from app.services import URLServices

from flask import redirect, request, Response


@app.route('/<string:url>', methods=['POST'])
def create_url_entry(url):
    url_entry = URLServices.find_or_create_entry(url)
    response = Response(status=302)
    response.set_cookie(url_entry.url_hash, url_entry.prefix + url_entry.url)
    return response


@app.route('/<key>', methods=['GET'])
def redirect_route(key):
    if key in request.cookies:
        return redirect(request.cookies[key])
    else:
        url_entry = URLServices.retrieve_url(key)

        return redirect(url_entry.url)
