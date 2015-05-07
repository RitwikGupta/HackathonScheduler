from flask import render_template
from scheduler import scheduler


@scheduler.route('/')
@scheduler.route('/index')
@scheduler.route('/index/')
def index():
    return "<h1>Hi</h1>"

if __name__ == '__main__':
    scheduler.run()
