from app import app, db
from app.services import URLServices

from flask import redirect, request, Response


@app.route('/url', methods=['POST'])
def create_url_entry():
    if 'url' not in request.json:
        return Response(status=400)
    else:
        url_entry = URLServices.find_or_create_entry(request.json['url'])
        response = Response(status=302)
        # import code
        # code.interact(local=locals())
        print(url_entry)
        response.set_cookie(url_entry.url_hash, url_entry.prefix + url_entry.url)
        print(url_entry.url_hash)
        return response


@app.route('/<key>', methods=['GET'])
def redirect_route(key):
    if key in request.cookies:
        return redirect(request.cookies[key])
    else:
        url_entry = URLServices.retrieve_url(key)

        return redirect(url_entry.prefix + url_entry.url)
