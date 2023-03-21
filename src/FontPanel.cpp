#include "FontPanel.h"

using namespace bt;

void FontPanel::RenderGUI()
{
	ImGui::Begin(getName());
	
	if (ImGui::BeginCombo("Font##fontcombo", current_font))
	{
		for (const auto& name : font_names)
		{
			bool is_selected = (current_font == name.c_str());
			if (ImGui::Selectable(name.c_str(), current_font))
			{
				current_font = name.c_str();
				printf("%s\n", current_font);
			}
		}
		ImGui::EndCombo();
	}

	ImGui::End();
}

void FontPanel::UpdateFontNames()
{
	font_names = getFontNames();
}

std::vector<std::string> FontPanel::getFontNames()
{
	std::vector<std::string> names;
	std::filesystem::path path = std::filesystem::current_path() / "BioFonts\\";

	for (const auto& entry : std::filesystem::directory_iterator(path))
	{
		if (entry.is_regular_file() && entry.path().extension().string() == ".bf")
		{
			std::string name = entry.path().filename().string();
			names.push_back(name);
		}
	}

	return names;
}