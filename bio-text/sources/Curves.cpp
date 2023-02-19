#include "Curves.h"

using namespace bt;

void Curve::AddPoint(BezierPoint point, int pos)
{
	if (pos >= 0) 
	{
		auto it = points.begin();
		std::advance(it, pos);
		points.insert(it, point);
	}
	else
	{
		points.push_back(point);
	}
}

void Curve::DeletePoint(uint32_t del_pos)
{
	if (del_pos >= 0 && del_pos < points.size())
	{
		auto it = points.begin();
		std::advance(it, del_pos);
		points.erase(it);
	}
}