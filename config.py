import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "real_secret"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.abspath(os.getcwd())+"\database.db"
    USERNAME = "Teodor"
    PASSWORD = "1234"
    MAP_URL = "https://www.google.com/maps/d/embed?mid=1wim-43D4yUcZGrRQtrjzfMTcsNPA1bCd"
    YANDEX_APIKEY = "3bda5c34-41cd-4840-8bc5-6dfe13e3aad4"

class ProductionConfig(Config):
    DEBUG = False
    # SECRET_KEY = os.environ['SECRET']
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] # postgresql:///database


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True