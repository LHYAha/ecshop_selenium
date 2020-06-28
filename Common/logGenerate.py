import logging
import time
import os

class GenLog():
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 设置文件名
        rq = time.strftime('%Y%m%d%H%m', time.localtime(time.time()))
        logPath = os.path.dirname(os.path.abspath('.'))
        logName = logPath + '\\Logs\\' + rq + '.log'
        # 写到日志文件里面
        fh = logging.FileHandler(logName)
        fh.setLevel(logging.INFO)
        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 设置log里面信息的格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def loggen(self):
        return self.logger