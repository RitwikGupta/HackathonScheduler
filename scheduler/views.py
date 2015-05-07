from flask import Flask


hs = Flask(__name__)

@hs.route('/')
@hs.route('/index')
@hs.route('/index/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    hs.run()
