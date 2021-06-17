import os


class Config(object):
    SECRET_KEY = os.urandom(64).hex()

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
