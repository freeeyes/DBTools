#ifndef TB_[pbName_Upper]_H
#define TB_[pbName_Upper]_H

#include "tb_Common.h"

bool Save_[pbName]_Data(MYSQL* pConn, int nPalyerID, const char* sz[pbName], int nLen);

bool Load_[pbName]_Data(MYSQL* pConn, int nPalyerID, char* sz[pbName], int nLen);

#endif