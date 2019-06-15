#include "tb_[pbName].h"

bool Save_[pbName]_Data(MYSQL* pConn, int nPalyerID, const char* sz[pbName], int nLen)
{
	char szSQL[8192] = {'\0'}

	if(NULL == pConn)
	{
		return false;
	}

	sprintf(szSQL, "INSERT INTO tb_[pbName](playerID, userdata, outtime) values(%d, x'%s', NOW()) ON DUPLICATE KEY UPDATE userdata=x'%s', outtime=NOW()", 
			nPalyerID, 
			sz[pbName],
			sz[pbName]);

	int ret = mysql_query(pConn, szSQL);
	if(ret != 0)
	{
		printf("[Save_[pbName]_Data]error:%s\n", mysql_error(pConn));
		return false;
	}
	return true;
};

bool Load_[pbName]_Data(MYSQL* pConn, int nPalyerID, char* sz[pbName], int nLen)
{
	char szSQL[500] = {'\0'}
	MYSQL_ROW sql_row;

	if(NULL == pConn)
	{
		return false;
	}
	
	sprintf(szSQL, "select hex(userdata) tb_[pbName] where playerID='%s'", 
			nPalyerID);	
			
	int ret = mysql_query(pConn, szSQL);
	if(ret != 0)
	{
		printf("[Save_[pbName]_Data]error:%s\n", mysql_error(pConn));
		return false;
	}
	
	MYSQL_RES *result = mysql_store_result(pConn);
	if(NULL != result)
	{
		while(sql_row = mysql_fetch_row(result))
		{
			strcpy(sz[pbName], sql_row[0]);
			break;
		}
	}

	mysql_free_result(result);
	return true;
}

bool Load_[pbName]_Data_List(MYSQL* pConn, int nPalyerID, vecpbData& objpbDataList)
{
	char szSQL[500] = {'\0'}
	MYSQL_ROW sql_row;

	if(NULL == pConn)
	{
		return false;
	}
	
	sprintf(szSQL, "select hex(userdata) tb_[pbName]", 
			nPalyerID);	
			
	int ret = mysql_query(pConn, szSQL);
	if(ret != 0)
	{
		printf("[Save_[pbName]_Data_List]error:%s\n", mysql_error(pConn));
		return false;
	}
	
	MYSQL_RES *result = mysql_store_result(pConn);
	if(NULL != result)
	{
		while(sql_row = mysql_fetch_row(result))
		{
			string strData = (string)sql_row[0];
			objpbDataList.pushback(strData);
		}
	}

	mysql_free_result(result);
	return true;	
}

