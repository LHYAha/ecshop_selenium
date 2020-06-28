from ecshop.Common.startBrowser import startBrowser
from ecshop.Common.readConfig import readConfig
from ecshop.Common.logGenerate import GenLog
import time

def webToursLogin(username,password):
    logger = GenLog(logger='测试用例操作').loggen()
    logger.info('读取测试用例配置文件')
    # username=readConfig('Config','Data','username')
    # password=readConfig('Config','Data','password')
    driver=startBrowser()
    driver.switch_to_frame('body')
    driver.switch_to_frame('navbar')
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    time.sleep(3)
    driver.quit()
    logger = GenLog(logger='退出测试操作').loggen()
    logger.info('退出地址')

