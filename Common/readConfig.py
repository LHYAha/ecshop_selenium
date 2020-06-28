import os
import configparser


def readConfig(configFile,section,option):
    cf = configparser.ConfigParser()
    path = os.path.dirname(os.path.abspath('.'))
    configPath = path+ '\\Config\\'+configFile+'.ini'
    cf.read(configPath)
    browsername = cf.get(section, option)
    return browsername
