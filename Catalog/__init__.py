import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import patch_request_class, UploadSet, configure_uploads, IMAGES

with open(os.getcwd() +'\\Catalog\\config.json') as config_file:
    config = json.load(config_file)
    
app = Flask(__name__)

app.config['SECRET_KEY'] = config.get('SECRET_KEY')
#app.config['SECRET_KEY'] = '5791628bb0b16ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres@localhost:5432/cata'
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + config.get('UPLOADED_PHOTOS_DEST')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)
# has to by the last import
from Catalog import routes