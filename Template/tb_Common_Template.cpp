#include "tb_Common.h"

MYSQL* Init_Mysql_Common()
{
	if (mysql_library_init(0, NULL, NULL))
	{
		printf("[Init_Mysql_Common]could not initialize MySQL library\n");
		return NULL;
	}
	MYSQL* pConn = new MYSQL();
	mysql_init(pConn);
	MYSQL *ret = mysql_real_connect(pConn, "[DBIP]", "[DBUser]", "[DBPass]", "[DBName]", "[DBPort]", NULL, 0);
	if(!ret)
	{
		printf("[Init_Mysql_Common]Failed to connect to database:%s\n", mysql_error(pConn));
		return NULL;
	}

	return pConn;

}

void Close_Mysql_Common(MYSQL* pConn)
{
	mysql_close(pConn);
}

