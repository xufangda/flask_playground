from flask import Flask

app = Flask(__name__)




# @app.route('/hello')
def hello():
    # 基于类的视图（即插视图）
    return 'hello, jiuyue'

app.add_url_rule('/hello',view_func=hello)

app.debug=True
app.run()