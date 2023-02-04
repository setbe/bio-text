#pragma once
#include <list>
#include "imgui.h"

namespace bt
{
	class BezierPoint
	{
	public:
		BezierPoint() {}
		BezierPoint(ImVec2 p1, ImVec2 p2, ImVec2 p3)
		{
			this->left = p1;
			this->point = p2;
			this->right = p3;
		}

		ImVec2 left;
		ImVec2 point;
		ImVec2 right;
	};

	class Curve
	{
	public:
		void AddPoint(BezierPoint point, int pos = -1);
		void DeletePoint(uint32_t pos_in_points);
		std::list<ImVec2> GetPointsToDraw(std::list<ImVec2> points, size_t n);

		std::list<BezierPoint> points;
	};
}