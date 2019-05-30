
import xml.dom.minidom as xmldom
from dbinfo import *
from pbinfo import *
from createdbfile import *

#读取指定的配置文件
def parse_config_xml(filename, objDBInfo, objPBList):
    xml_file = xmldom.parse(filename)
    config_element = xml_file.getElementsByTagName("config")[0]
    db_info = config_element.getElementsByTagName("DBInfo")[0]
    #print("[parse_config_xml]%s." % db_info.getAttribute("DBIP"))

    #读取数据库配置
    objDBInfo.m_strDBIP   = db_info.getAttribute("DBIP")
    objDBInfo.m_strDBPort = db_info.getAttribute("DBPort")
    objDBInfo.m_strDBName = db_info.getAttribute("DBName")
    objDBInfo.m_strDBUser = db_info.getAttribute("DBUser")
    objDBInfo.m_strDBPass = db_info.getAttribute("DBPass")

    for pb_info in config_element.getElementsByTagName("PBClassInfo"):
        objPBInfo = CPBInfo()
        objPBInfo.m_strPBPath   = pb_info.getAttribute("PBFilePath")
        objPBInfo.m_strPBName   = pb_info.getAttribute("PBName")
        objPBInfo.m_strFilePath = pb_info.getAttribute("FilePath")
        objPBList.append(objPBInfo)

if __name__ == "__main__":
    objDBInfo = CDBInfo()
    objPBList = []

    #解析XML配置文件
    parse_config_xml('../Config/DB.xml', objDBInfo, objPBList)

    #显示配置文件
    objDBInfo.Show()
    for objPBInfo in objPBList:
        objPBInfo.Show()

    #创建文件
    objCreateDBFile = CCreateDBFile()
    objCreateDBFile.CreateDBFile(objDBInfo, objPBList)