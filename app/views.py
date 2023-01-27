
from flask import render_template
from app import app
app.run(debug = True)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Alex' } # выдуманный пользователь
    return render_template("index.html",
                           title = 'Home',
                           user = user)

if __name__ == '__main__':
    app.run()