from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')



@app.route('/hello')
def hello():
    headers ={
        'content-type':'text/plain',
        'location':'http://www.bing.com'
    }
    response = make_response('<html></html>',301)
    response.headers=headers
    return response

# 当使用基于类的视图（即插视图）时，用下边这个函数注册
# app.add_url_rule('/hello',view_func=hello)

if __name__ == '__main__':
    app.debug=app.config['DEBUG']
    app.run(host='0.0.0.0')
