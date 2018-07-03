import os # Module allowing our application to interact with the operating system dependent functionality.
class Config:
    '''
    General configuration parent class
    '''
    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
    # A to help us access different configuration option classes.
    'development' : DevConfig,
    'production' : ProdConfig
}