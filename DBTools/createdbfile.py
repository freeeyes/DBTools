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

    def CreateCommonFile(self, objDBInfo, objPBInfo):
        try:
            strDBFile = objPBInfo.m_strFilePath + "//tb_Common.h"
            print("[CCreateDBFile::CreateCommonFile]strDBFile=%s" % strDBFile)
            objFileHead = open(strDBFile, "w")
            strline = "#ifndef TB_COMMON_H\n"
            objFileHead.write(strline)
            strline = "#define TB_COMMON_H\n\n"
            objFileHead.write(strline)
            strline = "#include <stdio.h>\n"
            objFileHead.write(strline)
            strline = "#include <stdlib.h>\n"
            objFileHead.write(strline)
            strline = "#include <mysql.h>\n\n"
            objFileHead.write(strline)
            strline = "MYSQL* Init_Mysql_Common();\n\n"
            objFileHead.write(strline)
            strline = "void Close_Mysql_Common(MYSQL* pConn);\n\n"
            objFileHead.write(strline)
            strline = "#endif\n"
            objFileHead.write(strline)

            strDBFile = objPBInfo.m_strFilePath + "//tb_Common.cpp"
            print("[CCreateDBFile::CreateCommonFile]strDBFile=%s" % strDBFile)
            objFileCpp = open(strDBFile, "w")
            objFileCpp.write(strline)
            strline = "#include \"tb_Common.h\"\n\n"
            objFileCpp.write(strline)
            strline = "MYSQL* Init_Mysql_Common()\n"
            objFileCpp.write(strline)
            strline = "{\n"
            objFileCpp.write(strline)
            strline = "\tif (mysql_library_init(0, NULL, NULL))\n"
            objFileCpp.write(strline)
            strline = "\t{\n"
            objFileCpp.write(strline)
            strline = "\t\tprintf(\"[Init_Mysql_Common]could not initialize MySQL library\\n\");\n"
            objFileCpp.write(strline)
            strline = "\t\treturn NULL;\n"
            objFileCpp.write(strline)
            strline = "\t}\n"
            objFileCpp.write(strline)
            strline = "\tMYSQL* pConn = new MYSQL();\n"
            objFileCpp.write(strline)
            strline = "\tmysql_init(pConn);\n"
            objFileCpp.write(strline)
            strline = "\tMYSQL *ret = mysql_real_connect(pConn, \"" + objDBInfo.m_strDBIP + "\", \"" + objDBInfo.m_strDBUser + "\", \"" + objDBInfo.m_strDBPass + "\", \"" + objDBInfo.m_strDBName + "\", " + objDBInfo.m_strDBPort + ", NULL, 0);\n"
            objFileCpp.write(strline)
            strline = "\tif(!ret)\n"
            objFileCpp.write(strline)
            strline = "\t{\n"
            objFileCpp.write(strline)
            strline = "\t\tprintf(\"[Init_Mysql_Common]Failed to connect to database:%s\\n\", mysql_error(pConn));\n"
            objFileCpp.write(strline)
            strline = "\t\treturn NULL;\n"
            objFileCpp.write(strline)
            strline = "\t}\n\n"
            objFileCpp.write(strline)
            strline = "\treturn pConn;\n\n"
            objFileCpp.write(strline)
            strline = "}\n\n"
            objFileCpp.write(strline)

            strline = "void Close_Mysql_Common(MYSQL* pConn)\n"
            objFileCpp.write(strline)
            strline = "{\n"
            objFileCpp.write(strline)
            strline = "\tmysql_close(pConn);\n"
            objFileCpp.write(strline)
            strline = "}\n\n"
            objFileCpp.write(strline)

        finally:
            objFileHead.close()
            objFileCpp.close()

    #创建数据库读写文件
    def CreateDBFile(self, objDBInfo, objPBList):
        self.CreateCommonFile(objDBInfo, objPBList[0]);
        for objPBInfo in objPBList:
            self.CreateSingleFile(objDBInfo, objPBInfo)
    
