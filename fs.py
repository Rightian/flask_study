from flask import Flask,abort
from flask import request
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://www.zhihu.com')

@app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#         return 'hello, %s' %user.name
# def index():
#     return '<h1>Bad Request</h1>',400

def index():
    user_agent = request.headers.get('User-Agent')
    return 'you browser is %s' % user_agent

# @app.route('/user/<name>')
# def user(name):
#     return 'hello,%s' %name
if __name__ == '__main__':
    app.run(debug=True)
