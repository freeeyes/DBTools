#!/bin/env python
# -*- coding: utf-8 -*- 
import os, sys, string
from dbinfo import *
from pbinfo import *

class CCreateDBFile:
    #创建单个文件
    def CreateSingleFile(self, objDBInfo, objPBInfo):
        strDBFile = objPBInfo.m_strFilePath + "//tb_" + objPBInfo.m_strPBName + ".h"
        print("[CCreateDBFile::CreateSingleFile]strDBFile=%s" % strDBFile)
        objFileHead = open(strDBFile, "w")

        objFileHead.close()


    #创建数据库读写文件
    def CreateDBFile(self, objDBInfo, objPBList):
        for objPBInfo in objPBList:
            self.CreateSingleFile(objDBInfo, objPBInfo)
    
