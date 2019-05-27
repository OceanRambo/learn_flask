from app import app

# 本机访问 http://127.0.0.1:5000/
app.run(debug=True)

# 局域网内其他电脑通过访问本机ip + 端口号访问
# app.run('0.0.0.0', 9000, debug=True)
