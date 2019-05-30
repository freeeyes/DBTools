#!/bin/env python
# -*- coding: utf-8 -*- 
import os, sys, string

class CPBInfo:
    def __init__(self):
        self.m_strPBPath   = ""
        self.m_strPBName   = ""
        self.m_strFilePath = ""

    def Show(self):
        print("[CPBInfo::Show]m_strPBPath=%s" % self.m_strPBPath)
        print("[CPBInfo::Show]m_strPBName=%s" % self.m_strPBName)
        print("[CPBInfo::Show]m_strFilePath=%s" % self.m_strFilePath)

