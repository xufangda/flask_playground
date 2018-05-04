
from flask import jsonify
from flask import Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook

# 蓝图blueprint

web=Blueprint('web',__name__)

@web.route('/book/search/<q>/<page>')
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
    # json 序列化
    # 与楼下等效
    # return json.dumps(result),200, {'content-type':'application/json'}
    return jsonify(result)
# 当使用基于类的视图（即插视图）时，用下边这个函数注册,等价于 @app.router装饰器
# app.add_url_rule('/hello',view_func=hello)
