import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:2021@localhost/watchlist'
    
class ProdConfig(Config):
    
    pass   
 
class DevConfig(Config):
      DEBUG = True

config_options = {
    'production':ProdConfig,
    'development':DevConfig,
}       