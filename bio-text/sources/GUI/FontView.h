#pragma once
#include <memory>
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
			curve = std::make_unique<Curve>();
			curve->AddPoint(BezierPoint({ 0.09, 0.70 }, { 0.12, 0.82 }, { 0.15, 0.95 }));
			curve->AddPoint(BezierPoint({ 0.37, 0.66 }, { 0.46, 0.3 }, { 0.3, 0.1 }));
		}
		void Render();

		std::unique_ptr<Curve> curve;
	private:
	};
}