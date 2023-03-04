#pragma once
#include <list>
#include <inttypes.h>
#include "imgui.h"

ImVec2 CalcOpposite(ImVec2 p0, ImVec2 p_opposite);

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

		void RotateRightOppositeLeft();
		void RotateLeftOppositeRight();

		ImVec2 left;
		ImVec2 point;
		ImVec2 right;
	};

	class Curve
	{
	public:
		void AddPoint(BezierPoint point, int pos = -1);
		void DeletePoint(uint32_t pos_in_points);

		std::list<BezierPoint> points;
	};
}
