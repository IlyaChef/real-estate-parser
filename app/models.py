from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Apartments(db.Model):
    __tablename__ = 'Apartments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    price = db.Column(db.Integer)
    image_url = db.Column(db.String(100))
    image_path = db.Column(db.String(1000))

    def __repr__(self):
        return '<Apartments {}>'.format(self.title, self.url)

class Flat(db.Model):
    __tablename__ = 'flat'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    image = db.Column(db.String(100))
    url = db.Column(db.String(100))
    flat = db.Column(db.String(1000))

    def __repr__(self):
        return '<Flat {}>'.format(self.title, self.url)

