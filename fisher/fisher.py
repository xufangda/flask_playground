from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook
import json

app = Flask(__name__)
app.config.from_object('config')



@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q: 普通关键字 isbn
        page    
    """
    # isbn isbn13 13 digits 
    # isbn 10 10 digits with dash

    isbn_or_key=is_isbn_or_key(q)
    if isbn_or_key=='isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return json.dumps(result),200, {'content-type':'application/json'}

# 当使用基于类的视图（即插视图）时，用下边这个函数注册
# app.add_url_rule('/hello',view_func=hello)

if __name__ == '__main__':
    app.debug=app.config['DEBUG']
    app.run(host='localhost')
