#ifndef TB_[pbName_Upper]_H
#define TB_[pbName_Upper]_H

#include "tb_Common.h"
#include <string>
#include <vector>

using namespace std;

typedef vector<string> vecpbData;

/*
作用:记录玩家的数据(一条)
参数:	pConn		MYSQL指针, 
		nPalyerID	玩家id号,
		nTime		时间(秒),
		sz[pbName]	数据bolb,
		nLen		数据bolb长度
*/
bool Save_[pbName]_Data(MYSQL* pConn, int nPalyerID, int nTime, const char* sz[pbName], int nLen);

/*
作用:内存中没有查找到玩家数据后在数据库中再次查找(一条)
参数:	pConn		MYSQL指针,
		nPalyerID	玩家id号,
		sz[pbName]	数据bolb,
		nLen		数据bolb长度
*/
bool Load_[pbName]_Data(MYSQL* pConn, int nPalyerID, char* sz[pbName], int nLen);

/*
作用:加载所有玩家的数据(时间限制)
参数:	pConn			MYSQL指针,
		nTime			时间(秒),
		objpbDataList	数据bolb,
		nLen			数据bolb长度
*/
bool Load_[pbName]_Data_List(MYSQL* pConn, int nTime, vecpbData& objpbDataList);

#endif