from app import db
from app.models import URLEntry

import re
url_sanitizer_regex = re.compile(r'https://www\.|http://www\.|www\.|http://|https://')


class URLServices:
    @staticmethod
    def find_or_create_entry(url):
        url_entry = URLEntry()
        url_entry.url = re.sub(url_sanitizer_regex, '', url)
        existing_url = URLEntry.query.filter_by(url=url_entry.url).first()

        if existing_url is not None:
            return existing_url
        else:
            try:
                url_entry.prefix = re.findall(url_sanitizer_regex, url)[0]
            except IndexError as e:
                url_entry.prefix = 'http'

            url_entry.hash_url = URLServices.encode(url_entry.url)

            db.session.add(url_entry)
            db.session.commit()

        return url_entry

    def retrieve_url(key):
        try:
            url_entry = URLEntry.query.filter_by(url_hash=key).first()
        finally:
            if url_entry is None:
                url_entry = URLEntry(url_hash=key, url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

        return url_entry

    @staticmethod
    def encode(url):
        pass
