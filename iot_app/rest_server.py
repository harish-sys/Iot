from flask import Flask

from iot_base.model import IotRepo

app = Flask(__name__)
from rest_api.iot_api import iot_routes

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/iot"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(iot_routes, url_prefix='/events')



@app.route('/')
def check():
    return 'Iot Project'


if __name__ == '__main__':
    app.run()
