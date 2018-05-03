from flask import Flask

app = Flask(__name__)
app.config.from_object('config')



@app.route('/hello')
def hello():
    return 'hello, jiuyue'

# 当使用基于类的视图（即插视图）时，用下边这个函数注册
# app.add_url_rule('/hello',view_func=hello)

if __name__ =='__main__':
    app.debug=app.config['DEBUG']
    app.run(host='0.0.0.0')
