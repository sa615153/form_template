from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
@app.route('/')
def index():
    user = {'nickname': 'Miguel'}
    return "hello world"
import views
if __name__ == '__main__':
    app.run(debug=True)