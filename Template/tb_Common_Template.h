#ifndef TB_COMMON_H
#define TB_COMMON_H

#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>

MYSQL* Init_Mysql_Common();

void Close_Mysql_Common(MYSQL* pConn);

#endif
