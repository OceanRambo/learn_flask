from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Rambo'}
    posts = [
        {
            'author': {'nickname': 'Tian'},
            'body': 'Beautiful day in Wuhan!'
        },

        {
            'author': {'nickname': 'Li'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
