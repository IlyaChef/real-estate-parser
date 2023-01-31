from flask import Flask

from models import db, Apartments

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def index():
    return 'Weird Appartment Finder!'

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

if __name__ == '__main__':
    app.run(debug=True)