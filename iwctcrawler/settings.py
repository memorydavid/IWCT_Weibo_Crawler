# Scrapy settings for iwctcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'iwctcrawler'

SPIDER_MODULES = ['iwctcrawler.spiders']
NEWSPIDER_MODULE = 'iwctcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iwctcrawler (+http://www.yourdomain.com)'



# Redis Config
REDIS_HOST="localhost"
REDIS_PORT=6379


WEIBO_USER_NAME="iwct5307data@126.com"
WEIBO_USER_PASSWORD="iwct5307"

# schedular config
#SCHEDULER_PERSIST = True
#QUEUE_KEY = '%(spider)s:requests'
#DUPEFILTER_KEY = '%(spider)s:dupefilter'
#SCHEDULER = "iwctcrawler.redis.scheduler.Scheduler"


# pipelines Config
ITEM_PIPELINES = ['iwctcrawler.pipelines.IwctcrawlerPipeline']
DOWNLOAD_DELAY = 10
TIME_DELTA = 30


# bootstrap from file (item.txt) or from db
BOOTSTRAP = 'file'

FEED_LIMIT = 300000
