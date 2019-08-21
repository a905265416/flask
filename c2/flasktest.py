from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'hello'
#route:路由 加int 给定固定的参数类型
@app.route('/profile/<int:uid>/')
def profile(uid):
    return 'profile:' + str(uid)
if __name__=='__main__':
    app.run(debug=True)