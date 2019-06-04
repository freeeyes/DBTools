#include "pb_templateFunc.h"

bool Serialize_Data(const Message* pMsg, char* buf, int bufLen)
{
	bool bKet = false;
	if (pMsg != nullptr)
	{
		bKet = pMsg->SerializeToArray(buf, bufLen);
	}
	return bKet;
}

bool Parse_Data(Message* pMsg, const char* buf, int bufLen)
{
	bool bKet = false;
	if (pMsg != nullptr)
	{
		bKet = pMsg->ParseFromArray(buf, bufLen);
	}
	return bKet;
}

Message* CreateMessage(const char* pbName)
{
	Message* pMsg = nullptr;
	auto descriptor = google::protobuf::DescriptorPool::generated_pool()->FindMessageTypeByName(pbName);
	if (nullptr != descriptor)
	{ 
		auto prototype = google::protobuf::MessageFactory::generated_factory()->GetPrototype(descriptor);
		if (nullptr != prototype)
		{
			//需要自己实现该函数.最好用对象池
			pMsg = prototype->New();
		}
	}
	return pMsg;
}