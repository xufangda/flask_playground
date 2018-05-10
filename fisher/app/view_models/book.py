class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':''
        }
        if data:
            returned['total']=1
            returned['books']=[cls.__cut_boook_data]
    @classmethod
    def package_collection(cls,data,keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total']=data['total']
            returned['books']=[cls.__cut_boook_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_boook_data(self, data):
        book={
            'title':data['title'],
            'publisher': data['publisher'],
            'pages':  data['pages'] or '' ,
            'author':'、'.join(data['author']),
            'price':data['price'],
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book