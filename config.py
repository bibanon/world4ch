import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLAlchemy Database connection
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sjis-20140420.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
