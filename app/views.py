from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Rambo'}
    # 直接返回html
    return render_template("index.html",
                           title='Home',
                           user=user)
