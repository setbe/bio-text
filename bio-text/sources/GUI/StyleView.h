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
		StyleView(Style* style_) : DockWidget("Style"), style(style_) { }
		
	protected:
		void RenderGUI() override;

	private:
		Style* style;
	};
}