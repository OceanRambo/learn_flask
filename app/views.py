from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '田'}
    posts = [
        {
            'author': {'username': '张'},
            'body': '武汉，每天不一样！'
        },

        {
            'author': {'username': '李'},
            'body': '武汉的东湖很美丽！'
        }
    ]
    return render_template("index.html",
                           title='我的',
                           user=user,
                           posts=posts)
