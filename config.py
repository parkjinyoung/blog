import os

basedir = os.path.abspath(os.path.dirname(__file__))

# default config
class BaseConfig(object):
  DEBUG = False
  # shortened for readability
  SECRET_KEY = 'hiiamasecretkey'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
  print SQLALCHEMY_DATABASE_URI


class DevelopmentConfig(BaseConfig):
  DEBUG = True


class ProductionConfig(BaseConfig):
  DEBUG = False