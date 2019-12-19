# /src/config.py

import os


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('postgres://postgres:admin@localhost:5432/blog_api_db')
    JWT_SECRET_KEY = os.getenv('my_secret_key')


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('postgres://postgres:admin@localhost:5432/blog_api_db')
    JWT_SECRET_KEY = os.getenv('my_secret_key')


app_config = {
    'development': Development,
    'production': Production,
}
