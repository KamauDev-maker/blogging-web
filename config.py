import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:2021@localhost/blogpost'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
    
    pass   
 
class DevConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:2021@localhost/blogpost'

      DEBUG = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:2021@localhost/blogpost_test'      

config_options = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}       