#include "FontPanel.h"
#include <iostream>

using namespace bt;

void FontPanel::RenderGUI()
{
	ImGui::Begin(getName());
	if (ImGui::BeginCombo("Font##fontcombo", font.getName().c_str()))
	{
		for (const auto& name : font_names)
		{
			bool is_selected = (font.getName() == name);
			if (ImGui::Selectable(name.c_str()))
			{
				font.setName(name);
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
    try
    {
        std::filesystem::path path = std::filesystem::current_path() / "BioFonts";

        for (const auto& entry : std::filesystem::directory_iterator(path))
        {
            if (entry.is_regular_file() && entry.path().extension().string() == ".bf")
            {
                std::string name = entry.path().filename().string();
                names.push_back(name);
            }
        }
    }
    catch (std::exception& e)
    {
		throw "BioFonts doesn't exist.";
    }

	return names;
}

void FontPanel::setDefaultFont()
{
	UpdateFontNames();
	for (const auto& name : font_names)
	{
		if (name == "Default.bf") font.setName(name);
	}
	if (font_names.size() > 0)
	{
		font.setName(font_names[0]);
	}
}
