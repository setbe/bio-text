#pragma once
#include <list>
#include <imgui.h>
#include <imgui_internal.h>
#include <glm/glm.hpp>
#include "DockWidget.h"
#include "Style.h"
#include "Curves.h"

namespace bt
{
	class FontView
	{
	public:
		FontView() {
			curves.push_back(Curve());
			selected_curve = &curves.front();
		}
		void Render();

		std::list<Curve> curves;
		Curve* selected_curve;
	private:

		void HelpManipulateControlPoint(const ImVec4 canvas);
	};
}