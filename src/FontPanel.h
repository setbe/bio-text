#pragma once
#include <string>
#include <vector>
#include "imgui.h"
#include "imgui_internal.h"
#include "DockWidget.h"

#if __has_include(<filesystem>)
#  include <filesystem>
#elif __has_include(<experimental/filesystem>)
#  include <experimental/filesystem>
#endif

namespace bt
{
	class FontPanel : public DockWidget
	{
	public:
		FontPanel() : DockWidget("Font")
		{
            current_font = NULL;
		}

		void setDefaultFont();
		void UpdateFontNames();
		static std::vector<std::string> getFontNames();

	protected:
		void RenderGUI() override;

	private:
		std::vector<std::string> font_names;
		const char* current_font;
	};
}
