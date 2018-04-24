import os
from baseconfig import DefaultConfig
from spider import Spider
from urlparse import urlparse
import sys
from utils import Logger

if __name__ == "__main__":
    defconfig = DefaultConfig.defaultconfig()
    Logger().info('Start Spider')
    spiderInstance = Spider(config=defconfig)
    