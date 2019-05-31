#!/bin/env python
# -*- coding: utf-8 -*- 
import os, sys, string
from dbinfo import *
from pbinfo import *

class CCreateDBFile:
    #创建单个文件
    def CreateSingleFile(self, objDBInfo, objPBInfo):
        self.CreateSingleHeadFile(objDBInfo, objPBInfo)
        self.CreateSingleCppFile(objDBInfo, objPBInfo)

    #创建头文件
    def CreateSingleHeadFile(self, objDBInfo, objPBInfo):
        try:
            strDBFile = objPBInfo.m_strFilePath + "//tb_" + objPBInfo.m_strPBName + ".h"
            print("[CCreateDBFile::CreateSingleFile]strDBFile=%s" % strDBFile)
            objFileHead = open(strDBFile, "w")
        
            strline = "tb_" + objPBInfo.m_strPBName + "_h"
            strline = "#ifndef " +  strline.upper() + "\n"
            objFileHead.write(strline)
            strline = "tb_" + objPBInfo.m_strPBName + "_h"
            strline = "#define " +  strline.upper() + "\n\n"
            objFileHead.write(strline)
            strline = "#include <stdio.h>\n"
            objFileHead.write(strline)
            strline = "#include <stdlib.h>\n"
            objFileHead.write(strline)
            strline = "#include <mysql.h>\n\n"
            objFileHead.write(strline)
            strline = "bool Save_" + objPBInfo.m_strPBName + "_Data(MYSQL* pConn, " + objPBInfo.m_strPBName + " obj" + objPBInfo.m_strPBName + ");\n\n"
            objFileHead.write(strline)
            strline = "#endif" + "\n"
            objFileHead.write(strline)
        finally:
            objFileHead.close()

    #创建代码文件
    def CreateSingleCppFile(self, objDBInfo, objPBInfo):
        try:
            strDBFile = objPBInfo.m_strFilePath + "//tb_" + objPBInfo.m_strPBName + ".cpp"
            print("[CCreateDBFile::CreateSingleCppFile]strDBFile=%s" % strDBFile)
            objFileCpp = open(strDBFile, "w")

            strline = "#include \"tb_" + objPBInfo.m_strPBName + ".h\"\n\n"
            objFileCpp.write(strline)

            strline = "bool Save_" + objPBInfo.m_strPBName + "_Data(MYSQL* pConn, " + objPBInfo.m_strPBName + " obj" + objPBInfo.m_strPBName + ")\n"
            objFileCpp.write(strline)
            strline = "{\n"
            objFileCpp.write(strline)
            strline = "\tchar szSQL[1024] = {'\\0'}\n\n"
            objFileCpp.write(strline)
            strline = "\tif(NULL == pConn)\n\t{\n\t\treturn false;\n\t}\n\n"
            objFileCpp.write(strline)
            strline = "\tsprintf(szSQL, \"insert into "+ objPBInfo.m_strTableName + "() values()\");\n\n"
            objFileCpp.write(strline)
            strline = "\tint ret = mysql_query(pConn, szSQL);\n"
            objFileCpp.write(strline)
            strline = "\tif(ret != 0)\n"
            objFileCpp.write(strline)
            strline = "\t{\n"
            objFileCpp.write(strline)
            strline = "\t\tprintf(\"[" + "Save_" + objPBInfo.m_strPBName + "_Data" + "]error:%s\\n\", mysql_error(pConn));\n"
            objFileCpp.write(strline)
            strline = "\t\treturn false;\n"
            objFileCpp.write(strline)
            strline = "\t}\n"
            objFileCpp.write(strline)
            strline = "\treturn true;\n"
            objFileCpp.write(strline)
            strline = "};\n\n"
            objFileCpp.write(strline)

        finally:
            objFileCpp.close()


    #创建数据库读写文件
    def CreateDBFile(self, objDBInfo, objPBList):
        for objPBInfo in objPBList:
            self.CreateSingleFile(objDBInfo, objPBInfo)
    
