#include "tb_[pbName].h"

bool Save_aaa_Data(MYSQL* pConn, int nPalyerID, const char* sz[pbName], int nLen)
{
	char szSQL[4096] = {'\0'}

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
		printf("[Save_aaa_Data]error:%s\n", mysql_error(pConn));
		return false;
	}
	return true;
};

