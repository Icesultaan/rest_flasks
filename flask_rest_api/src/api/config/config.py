import os
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    missing='NONE'
    dbName = os.environ.get('RDS_DB_NAME', missing)
    dbUser = os.environ.get('RDS_USERNAME', missing)
    dbPassword = os.environ.get('RDS_PASSWORD', missing)
    dbHost = os.environ.get('RDS_HOSTNAME', missing)
    dbPort = os.environ.get('RDS_PORT', missing)
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dbUser}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'
    print("DB URI: ", SQLALCHEMY_DATABASE_URI);

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://marius:password@localhost:3306/devdb'
    SQLALCHEMY_ECHO = False


