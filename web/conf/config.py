import os


class Config(object):
    # 邮件服务配置
    EMAIL_SERVER = "smtp.xxx.com"
    EMAIL_PORT = 465
    EMAIL_ADDR = "abc@xxx.com"
    EMAIL_PASSWORD = "123456"
    EMAIL_TIMEOUT = 10  # 单位(秒)
    # 服务监听端口
    PORT = 8082
    # 日志文件路径
    LOG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "log", "app.log")

class ProductionConfig(Config):
    # 日志配置
    LOG_LEVEL = "INFO"

class DevelopmentConfig(Config):
    pass

config = {
        "production": ProductionConfig,
        "development": DevelopmentConfig,
        "default": ProductionConfig
        }
