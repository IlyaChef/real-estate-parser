from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db = SQLAlchemy()

engine = create_engine('postgresql://cqdiqzza:iFkFWOZp3T6CIKaOWkfiI84t9SJefz_y@mouse.db.elephantsql.com:5432/cqdiqzza')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()



