from flask import Flask,current_app

app=Flask(__name__)

# applicationn context  a embeded Flask
# request context   a Request Flask

# ctx=app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# with app.app_context():
#     a=current_app
#     d=current_app.config['DEBUG']

class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self
    def __exit__(self,exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource')
        # return value is True or False
        # when true no exception will throw out
        # if false, it will throw an exception
        return True
    def query(self):
        print('query data')

with MyResource() as resource:
    1/0
    resource.query()