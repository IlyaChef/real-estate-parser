from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, LargeBinary
from db import Base,engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class Apartments(db.Model):
    __tablename__ = 'Apartments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    price = db.Column(db.Integer)
    image_url = db.Column(db.String(100))
    image_path = db.Column(db.String(1000))


    #def __init__(self, title, url, price, image_url, image_path):
        #self.title = title
        #self.url = url
        #self.price = price
        #self.image_url = image_url
        #self.image_path = image_path

    def __repr__(self):
        return '<Apartments {}>'.format(self.title, self.url)

#if __name__ == '__main__':
    #Base.metadata.create_all(bind=engine)

#class Description(Base):
    #__tablename__ = 'Apartments'
    #cian_id = db.Column(db.Integer, primary_key=True, unique=True)
    #rooms = db.Column(db.Integer, nullable=True)
    #metro = db.Column(db.String, nullable=True)
    #address = db.Column(db.Text, nullable=True)
    #area = db.Column(db.String, nullable=True)
    #house = db.Column(db.String, nullable=True)
    #price = db.Column(db.Integer, nullable=True)
    #description = db.Column(db.Text, nullable=True)
    #renovation = db.Column(db.String, nullable=True)

#def __repr__(self):
    #return '<Apartments {}>'.format(self.cian_id)

#if __name__ == '__main__':
    #Base.metadata.create_all(bind=engine)



#apartments = Apartments(title=title, url=url, image_url=image_url)

#session.add(apartments)

#session.commit()

#engine = create_engine('sqlite:///avitoapartments.db')

#Base.metadata.create_all(engine)

#if __name__ == '__main__':
    #Base.metadata.create_all(bind=engine)