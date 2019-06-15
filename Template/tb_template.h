#ifndef TB_[pbName_Upper]_H
#define TB_[pbName_Upper]_H

#include "tb_Common.h"
#include <string>
#include <vector>

using namespace std;

typedef vector<string> vecpbData;

bool Save_[pbName]_Data(MYSQL* pConn, int nPalyerID, const char* sz[pbName], int nLen);

bool Load_[pbName]_Data(MYSQL* pConn, int nPalyerID, char* sz[pbName], int nLen);

bool Load_[pbName]_Data_List(MYSQL* pConn, int nPalyerID, vecpbData& objpbDataList);

#endif