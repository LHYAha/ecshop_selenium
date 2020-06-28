import xlrd,xlwt
from ecshop.Common.readConfig import readConfig
from ecshop.Common.readCase import readCase
from ecshop.Script.test import webToursLogin
from ecshop.Script.baiduTest import baidu

from ecshop.Common.logGenerate import GenLog
import os

def readSuit(excelFile,sheetName):
    logger = GenLog(logger='测试用例集操作').loggen()
    if os.path.exists(excelFile):
        logger.info("解析%s文件" %excelFile)
        ef=xlrd.open_workbook(excelFile)
        suitCase=ef.sheet_by_name(sheetName)
        taskAmount=suitCase.nrows-1
        logger.info("一共有%s个测试任务" %taskAmount)
        for i in range(1,taskAmount+1):
            taskName=suitCase.cell(i,1).value
            taskFlag = suitCase.cell(i,2).value
            # logger.info("测试任务名称是：%s,测试状态是：%s" %(taskName,taskFlag))
            logger.info("判断测试任务：")
            if taskName=='search':
                logger.info("当前任务是：%s" % taskName)
                if taskFlag=='Y':
                    baidu().search("软件测试")
                else:
                    logger.info("当前任务标记是：%s ,所以不用执行" % taskFlag)
            if taskName=='linkTest':
                logger.info("当前任务是：%s" % taskName)
                if taskFlag=='Y':
                    value=readCase("C:\\Users\\lihai\Desktop\\test.xlsx", "suitcase")
                    baidu().clicLinTest(value)
                else:
                    logger.info("当前任务标记是：%s ,所以不用执行" % taskFlag)
    else:
        logger.info("解析文件不存在")

readSuit("C:\\Users\\lihai\Desktop\\test.xlsx","testsuit")