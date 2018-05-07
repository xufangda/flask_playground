class BookViewModel:
    def package_single(self, data, keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':''
        }
        if data:
            returned['total']=1

    def package_collection(self):
        pass

    def __cut_boook_data(self,data):
        book={
            'title':data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author':'、'.join(data['author'])
            'price':data['price'],
            'summary':data['summary'],
            'image':data['image']
        }
        
        pass