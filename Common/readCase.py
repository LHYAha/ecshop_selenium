import xlrd,xlwt
from ecshop.Common.readConfig import readConfig
from ecshop.Script.test import webToursLogin
from ecshop.Common.logGenerate import GenLog
import os

def readCase(excelFile,sheetName):
    logger = GenLog(logger='测试用例操作').loggen()
    if os.path.exists(excelFile):
        logger.info("解析%s文件" %excelFile)
        ef=xlrd.open_workbook(excelFile)
        suitCase = ef.sheet_by_name(sheetName)
        caseAmount = suitCase.nrows
        if caseAmount>0:
            #读取第一行的数据
            testData=suitCase.row_values(0)
            return testData
    else:
        logger.info("解析文件不存在")

value=readCase("C:\\Users\\lihai\Desktop\\test.xlsx", "suitcase")

print(value.__len__())