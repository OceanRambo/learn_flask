import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 电子邮件服务器详细信息
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['452828172@qq.com']

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL对应的MAIL_PORT = 465
    MAIL_USERNAME = 'xxx@qq.com'  # 自己的QQ邮箱
    MAIL_PASSWORD = "rizxuuhirzwvcbah"
    # MAIL_PASSWORD = "frdsggrjcdlhbiae"     MAIL_USE_SSL对应
    MAIL_DEFAULT_SENDER = "xxx@qq.com"  # 默认发送者， 自己的QQ邮箱

    POSTS_PER_PAGE = 25


