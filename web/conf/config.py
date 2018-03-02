import os


class Config(object):
    # Mysql配置
    MYSQL_HOST = "xxx"
    MYSQL_USER = "xxx"
    MYSQL_PASSWD = "xxx"
    MYSQL_DB = "xxx"

    # 服务监听端口
    PORT = 8000

    # 日志文件路径
    LOG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "log", "app.log")


class ProductionConfig(Config):
    # 日志配置
    LOG_LEVEL = "INFO"
    DEBUG = False


class DevelopmentConfig(Config):
    pass


config = ProductionConfig
