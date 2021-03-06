from decouple import config

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*")
SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL", default="sqlite:///./sql_app.db")