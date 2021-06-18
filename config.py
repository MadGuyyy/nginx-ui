import os


# TODO:
# Dark mode
# Syntax highlighting
# Do something with config
# Validate site paths
# Update README
# Docker?
# Minify JS/CSS before deploying, remove mini files from Git


class Config(object):
    SECRET_KEY = "759897607520e195bf25c407330853a3"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    AUTH_PASSWORD = "supersecret"
    NGINX_PATH = "/etc/nginx"
    SITES_AVAILABLE_PATH = os.path.join(NGINX_PATH, "sites-available")
    SITES_ENABLED_PATH = os.path.join(NGINX_PATH, "sites-enabled")

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
