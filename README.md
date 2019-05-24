根据如下网址
http://www.pythondoc.com/flask-mega-tutorial/index.html
一步步学习Flask

本机环境Windows10 64位
python3.6.5


打开一个终端窗口，切换到某目录下创建文件夹 microblog。
D:\>mkdir microblog
D:\>cd microblog
创建虚拟环境
D:\microblog>python -m venv env_flask
D:\microblog>cd env_flask\Scripts
激活，进入虚拟环境
D:\microblog\env_flask\Scripts>activate
(env_flask) D:\microblog\env_flask\Scripts>

安装flask 以及扩展
(env_flask) D:\microblog\env_flask\Scripts>pip install flask

依次安装下面扩展
D:\microblog\env_flask\Scripts>pip install flask-login
D:\microblog\env_flask\Scripts>pip install flask-openid
D:\microblog\env_flask\Scripts>pip install flask-mail
D:\microblog\env_flask\Scripts>pip install flask-sqlalchemy
D:\microblog\env_flask\Scripts>pip install sqlalchemy-migrate
D:\microblog\env_flask\Scripts>pip install flask-whooshalchemy
D:\microblog\env_flask\Scripts>pip install flask-wtf
D:\microblog\env_flask\Scripts>pip install flask-babel
D:\microblog\env_flask\Scripts>pip install guess_language
D:\microblog\env_flask\Scripts>pip install flipflop
D:\microblog\env_flask\Scripts>pip install coverage