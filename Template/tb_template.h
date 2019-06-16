#ifndef TB_[pbName_Upper]_H
#define TB_[pbName_Upper]_H

#include "tb_Common.h"
#include <string>
#include <vector>

using namespace std;

typedef vector<string> vecpbData;

/*
����:��¼��ҵ�����(һ��)
����:	pConn		MYSQLָ��, 
		nPalyerID	���id��,
		nTime		ʱ��(��),
		sz[pbName]	����bolb,
		nLen		����bolb����
*/
bool Save_[pbName]_Data(MYSQL* pConn, int nPalyerID, int nTime, const char* sz[pbName], int nLen);

/*
����:�ڴ���û�в��ҵ�������ݺ������ݿ����ٴβ���(һ��)
����:	pConn		MYSQLָ��,
		nPalyerID	���id��,
		sz[pbName]	����bolb,
		nLen		����bolb����
*/
bool Load_[pbName]_Data(MYSQL* pConn, int nPalyerID, char* sz[pbName], int nLen);

/*
����:����������ҵ�����(ʱ������)
����:	pConn			MYSQLָ��,
		nTime			ʱ��(��),
		objpbDataList	����bolb,
		nLen			����bolb����
*/
bool Load_[pbName]_Data_List(MYSQL* pConn, int nTime, vecpbData& objpbDataList);

#endif