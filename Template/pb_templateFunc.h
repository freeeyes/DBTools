#ifndef PB_TEMPLATE_FUNC_H
#define PB_TEMPLATE_FUNC_H

#include <<google/protobuf/message.h>

using google::protobuf::Message;

Message* CreateMessage(const char* pbName);

bool Serialize_Data(const Message* pMsg, char* buf, int bufLen);

bool Parse_Data(Message* pMsg, const char* buf, int bufLen);

#endif