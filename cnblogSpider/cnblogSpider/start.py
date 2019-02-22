import sys

from scrapy import cmdline

print(sys.path)
cmdline.execute('scrapy crawl cnblogs'.split())
