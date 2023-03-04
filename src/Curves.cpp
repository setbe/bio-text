#include "Curves.h"

using namespace bt;

ImVec2 CalcOpposite(ImVec2 p0, ImVec2 p_opposite)
{
	return { p0.x + p0.x - p_opposite.x, p0.y + p0.y - p_opposite.y };
}

void BezierPoint::RotateRightOppositeLeft()
{
	right = CalcOpposite(point, left);
}

void BezierPoint::RotateLeftOppositeRight()
{
	left = CalcOpposite(point, right);
}

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