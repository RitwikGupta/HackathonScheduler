from flask import Flask


hs = Flask(__name__)

@hs.route('/')
@hs.route('/index')
@hs.route('/index/')
def index():
    return render_template('index.html')

@hs.route('/calc', methods=['POST'])
def calc():
    

if __name__ == '__main__':
    hs.run()
