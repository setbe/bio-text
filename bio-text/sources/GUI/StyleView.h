#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <glm/glm.hpp>
#include "DockWidget.h"
#include "Style.h"

namespace bt
{
	class StyleView : public DockWidget
	{
	public:
		StyleView() : DockWidget("Style") {}

		void Render() override;

		Style style;
	};
}