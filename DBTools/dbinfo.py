#!/bin/env python
# -*- coding: utf-8 -*- 
import os, sys, string

class CDBInfo:
    def __init__(self):
        self.m_strDBIP   = ""
        self.m_strDBPort = ""
        self.m_strDBName = ""
        self.m_strDBUser = ""
        self.m_strDBPass = ""

    def Show(self):
        print("[CDBInfo::Show]m_strDBIP=%s" % self.m_strDBIP)
        print("[CDBInfo::Show]m_strDBPort=%s" % self.m_strDBPort)
        print("[CDBInfo::Show]m_strDBName=%s" % self.m_strDBName)
        print("[CDBInfo::Show]m_strDBUser=%s" % self.m_strDBUser)
        print("[CDBInfo::Show]m_strDBPass=%s" % self.m_strDBPass)

