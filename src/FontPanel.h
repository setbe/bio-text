#pragma once
#include <string>
#include <vector>
#include <filesystem>
#include "imgui.h"
#include "imgui_internal.h"
#include "DockWidget.h"

namespace bt
{
	class FontPanel : public DockWidget
	{
	public:
		FontPanel() : DockWidget("Fonts") { }

		void UpdateFontNames();
		static std::vector<std::string> getFontNames();

	protected:
		void RenderGUI() override;

	private:
		std::vector<std::string> font_names;
		const char* current_font;
	};
}