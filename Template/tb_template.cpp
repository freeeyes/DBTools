#include "tb_[pbName].h"

bool Save_aaa_Data(MYSQL* pConn, [pbName] obj[pbName])
{
	char szSQL[2048] = {'\0'}

	if(NULL == pConn)
	{
		return false;
	}

	sprintf(szSQL, "insert into tb_[pbName]() values()");

	int ret = mysql_query(pConn, szSQL);
	if(ret != 0)
	{
		printf("[Save_aaa_Data]error:%s\n", mysql_error(pConn));
		return false;
	}
	return true;
};

