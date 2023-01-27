from __init__ import create_app
from parser import scrape

app = create_app()
with app.app_context():
    scrape()
