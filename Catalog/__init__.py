import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import patch_request_class, UploadSet, configure_uploads, IMAGES


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b16ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres@localhost:5432/cata'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '\\Catalog\\_uploads'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)
# has to by the last import
from Catalog import routes