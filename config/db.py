from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

user = 'DanmercU'
passw = ''
host = 'DanmercU.mysql.pythonanywhere-services.com'
db = 'DanmercU$movil2ul'

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{passw}@{host}/{db}"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = "movil2"

db = SQLAlchemy(app)

ma = Marshmallow(app)