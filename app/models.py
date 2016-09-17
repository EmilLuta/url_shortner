from app import db

class URLEntry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(2048))
	url_hash = db.Column(db.String(255))

	def __str__(self):
		return 'URLEntry {} -> {}'.format(self.url, self.url_hash)

	def __repr__(self):
		return 'URLEntry {} -> {}'.format(self.url, self.url_hash)