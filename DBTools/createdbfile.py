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
            #读取模板文件
            strTHFile = "../Template/tb_template.h"
            objTHFile = open(strTHFile, "r")

            strTempCode = objTHFile.read()
            objTHFile.close()

            #格式化文件
            strCurrCode = strTempCode
            strCurrCode = strCurrCode.replace("[pbName_Upper]", objPBInfo.m_strPBName.upper())
            strCurrCode = strCurrCode.replace("[pbName]", objPBInfo.m_strPBName)

            strDBFile = objPBInfo.m_strFilePath + "//tb_" + objPBInfo.m_strPBName + ".h"
            print("[CCreateDBFile::CreateSingleFile]strDBFile=%s" % strDBFile)
            objFileHead = open(strDBFile, "w")
                       
            objFileHead.write(strCurrCode)
        finally:
            objFileHead.close()

    #创建代码文件
    def CreateSingleCppFile(self, objDBInfo, objPBInfo):
        try:
            #读取模板文件
            strTCFile = "../Template/tb_template.cpp"
            objTCFile = open(strTCFile, "r")

            strTempCode = objTCFile.read()
            objTCFile.close()

            #格式化文件
            strCurrCode = strTempCode
            strCurrCode = strCurrCode.replace("[pbName]", objPBInfo.m_strPBName)

            strDBFile = objPBInfo.m_strFilePath + "//tb_" + objPBInfo.m_strPBName + ".cpp"
            print("[CCreateDBFile::CreateSingleCppFile]strDBFile=%s" % strDBFile)
            objFileCpp = open(strDBFile, "w")
            objFileCpp.write(strCurrCode)
        finally:
            objFileCpp.close()

    def CreateCommonFile(self, objDBInfo, objPBInfo):
        try:
            #读取模板文件
            strTHFile = "../Template/tb_Common_Template.h"
            objTHFile = open(strTHFile, "r")

            strTempCode = objTHFile.read()
            objTHFile.close()

            strDBFile = objPBInfo.m_strFilePath + "//tb_Common.h"
            print("[CCreateDBFile::CreateCommonFile]strDBFile=%s" % strDBFile)
            objFileHead = open(strDBFile, "w")
            objFileHead.write(strTempCode)

            #读取模板文件
            strTCFile = "../Template/tb_Common_Template.cpp"
            objTCFile = open(strTCFile, "r")

            strTempCode = objTCFile.read()
            objTHFile.close()

            #格式化文件
            strCurrCode = strTempCode
            strCurrCode = strCurrCode.replace("[DBIP]", objDBInfo.m_strDBIP)
            strCurrCode = strCurrCode.replace("[DBUser]", objDBInfo.m_strDBName)
            strCurrCode = strCurrCode.replace("[DBPass]", objDBInfo.m_strDBPass)
            strCurrCode = strCurrCode.replace("[DBName]", objDBInfo.m_strDBName)
            strCurrCode = strCurrCode.replace("[DBPort]", objDBInfo.m_strDBPort)

            strDBFile = objPBInfo.m_strFilePath + "//tb_Common.cpp"
            print("[CCreateDBFile::CreateCommonFile]strDBFile=%s" % strDBFile)
            objFileCpp = open(strDBFile, "w")
            objFileCpp.write(strCurrCode)

        finally:
            objFileHead.close()
            objFileCpp.close()

    #创建数据库读写文件
    def CreateDBFile(self, objDBInfo, objPBList):
        self.CreateCommonFile(objDBInfo, objPBList[0]);
        for objPBInfo in objPBList:
            self.CreateSingleFile(objDBInfo, objPBInfo)
    
