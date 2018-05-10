from flask import Blueprint, jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm

from app.view_models.book import BookViewModel

from . import web

@web.route('/book/search')
def search(m=1):
    """
        q: 普通关键字 isbn
        page    
    """
    # isbn isbn13 13 digits 
    # isbn 10 10 digits with dash
    # q至少要有一个字符， 有最大值限制
    # q=request.args['q']
    # page 正整数，长度限制
    # page=request.args['page']

    #验证层
    form =SearchForm(request.args)
    if form.validate():
        q=form.q.data.strip()
        page=form.page.data
        isbn_or_key=is_isbn_or_key(q)
        
        if isbn_or_key=='isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result,q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
            result = BookViewModel.package_collection(result,q)
        return jsonify(result)
    else:
        return jsonify(form.errors)