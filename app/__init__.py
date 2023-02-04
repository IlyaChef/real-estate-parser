from flask import Flask
from flask import render_template
from flask import send_from_directory
from models import db, Apartments, Flat
from math import ceil

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def index():
    flats = Flat.query.all()
    return render_template('index.html', flats=flats)

@app.route("/<int:page>")
def flats(page):
    flats_per_page = 10
    flats = Flat.query.paginate(page, flats_per_page, False)
    total_pages = ceil(Flat.query.count() / flats_per_page)
    return render_template("index.html", flats=flats, total_pages=total_pages)

def create_app() -> object:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return 'Weird Appartment Finder!'

    return app

@app.route('/static/media/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)