from flask import Flask
from flask import render_template
from flask import send_from_directory
from models import db, Apartments


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def index():
    apartments = Apartments.query.all()
    return render_template('index.html', apartments=apartments)

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

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)