import os
# from flask.config import Config
class Config:
    NEWS_API_SOURCE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2021-08-18&sortBy=popularity&apiKey={}'
    NEWS_API_KEY = 'bc762445f3694294be352930fac05201'
    SECRET_KEY = 'Caroh'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
