import os
class Config:
    DB_USER = 'admin'
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = 'localhost'
    DB_NAME = 'Van'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://admin:admin@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True