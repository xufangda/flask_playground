from app import create_app

__author__ = 'Fangda'

app=create_app()

if __name__ == '__main__':
    app.debug=app.config['DEBUG']
    app.run(host='localhost')
