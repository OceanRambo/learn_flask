from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('用户：{}，恭喜你成功登录'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
