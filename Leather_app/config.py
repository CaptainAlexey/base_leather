class Configuration(object):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:root@localhost/leather_db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='Secret'