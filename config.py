import os


# TODO:
# Dark mode
# Do something with config
# Validate site paths
# Update README
# Reload nginx button


class Config(object):
    SECRET_KEY = "759897607520e195bf25c40733085300"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    AUTH_PASSWORD = ""
    NGINX_PATH = "/etc/nginx"
    SITES_AVAILABLE_PATH = os.path.join(NGINX_PATH, "sites-available")
    SITES_ENABLED_PATH = os.path.join(NGINX_PATH, "sites-enabled")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "sqlalchemy"
    SESSION_COOKIE_SAMESITE = "Lax"

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


class WorkingConfig(Config):
    DEBUG = False


config = {
    'dev': DevConfig,
    'default': WorkingConfig
}
