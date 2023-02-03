#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <memory>
#include "DockWidget.h"
#include "Style.h"
#include <string>

namespace bt
{
	class TextView : public DockWidget
	{
	public:
		TextView();
		~TextView();

	private:
		void RenderGUI() override;

		std::string symbols_counter;
		char text[513];
	};
}