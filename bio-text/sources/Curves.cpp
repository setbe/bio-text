#include "Curves.h"

using namespace bt;

void Curve::AddPoint(BezierPoint point, int pos)
{
	if (pos >= 0) {
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
	if (del_pos > 0 && del_pos < points.size() + 1)
	{
		auto it = points.begin();
		std::advance(it, del_pos);
		points.erase(it);
	}
}

std::list<ImVec2> Curve::GetPointsToDraw(std::list<ImVec2> points_, size_t n)
{
	std::list<ImVec2> list;

	std::list<ImVec2>::iterator it = points_.begin();
	std::advance(it, n);

	list.push_back(*it); it++;
	list.push_back(*it); it++;
	list.push_back(*it);

	if (n >= points_.size())
	{
		list.push_back({it->x + 0.05f, it->y});
	}
	else
	{
		it++;
		list.push_back(*it);
	}

	return list;
}