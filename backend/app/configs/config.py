import os.path

# 当前目录
CURRENT_DIR = os.path.abspath(__file__)


# 项目根目录
ROOT_PATH = os.path.dirname(os.path.dirname(CURRENT_DIR))


class BaseConfig(object):
    DEBUG = False


class Development(BaseConfig):
    pass


class Productions(BaseConfig):
    pass



configs = {
        'dev': Development(),
        'prod': Productions()
}

