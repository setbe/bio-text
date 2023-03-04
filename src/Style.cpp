#include "Style.h"

namespace bt {
	Style::Style()
	{
		fontsize = 32;
		cursive = 0;
		thickness = 2.0f;
		curl = 0.0f;
		color = new float[4]{ 0.0f, 0.0f, 0.1f, 1.0f };

		fontsize_random = 0;
		cursive_random = 0;
		thickness_random = 0.0f;
		curl_random = 0.0f;

		color_random = new float[4]{ 0.0f, 0.0f, 0.0f, 1.0f };
		seed = 0;
	}

	Style::~Style()
	{
		delete color;
		delete color_random;
	}

	int* Style::getFontSize()
	{
		return &fontsize;
	}

	int* Style::getCursive() 
	{
		return &cursive;
	}

	float* Style::getThickness()
	{
		return &thickness;
	}

	float* Style::getCurl()
	{
		return &curl;
	}

	float* Style::getColor()
	{
		return color;
	}


	int* Style::getFontSizeRandom()
	{
		return &fontsize_random;
	}

	int* Style::getCursiveRandom()
	{
		return &cursive_random;
	}

	float* Style::getThicknessRandom()
	{
		return &thickness_random;
	}

	float* Style::getCurlRandom()
	{
		return &curl_random;
	}


	float* Style::getColorRandom()
	{
		return color_random;
	}

	int* Style::getSeed()
	{
		return &seed;
	}

	void Style::CorrectToFontSize()
	{
		// yes, i like hardcoding
		if (cursive > fontsize)
		{
			cursive = fontsize;
		} 
		else if(cursive < -fontsize)
		{
			cursive = -fontsize;
		}

		if (thickness > (float)fontsize / 10)
			thickness = (float)fontsize / 10;

		if (curl > (float)fontsize / 10)
			curl = (float)fontsize / 10;

		if (fontsize_random > fontsize)
			fontsize_random = fontsize;

		if (cursive_random > fontsize)
			cursive_random = fontsize;

		if (thickness_random > (float)fontsize / 10)
			thickness_random = (float)fontsize / 10;

		if (curl_random > (float)fontsize / 10)
			curl_random = (float)fontsize / 10;
	}

	constexpr ImVec4 ColorFromBytes(uint8_t r, uint8_t g, uint8_t b, uint8_t a)
{
    return ImVec4((float)r / 255.0f, (float)g / 255.0f, (float)b / 255.0f, (float)a / 255.0f);
};

	void UseDarkTheme()
	{
		ImVec4* colors = ImGui::GetStyle().Colors;
		const ImVec4 bgColor = ColorFromBytes(20, 20, 21);
		const ImVec4 lightBgColor = ColorFromBytes(82, 82, 85);
		const ImVec4 veryLightBgColor = ColorFromBytes(90, 90, 95);

		const ImVec4 panelColor = ColorFromBytes(51, 51, 55);
		const ImVec4 panelActiveColor = ColorFromBytes(29, 121, 106);
		const ImVec4 panelHoverColor = ColorFromBytes(0, 85, 70);

		const ImVec4 textColor = ColorFromBytes(255, 255, 255);
		const ImVec4 textDisabledColor = ColorFromBytes(151, 151, 151);
		const ImVec4 borderColor = ColorFromBytes(78, 78, 78);

		colors[ImGuiCol_Text] = textColor;
		colors[ImGuiCol_TextDisabled] = textDisabledColor;
		colors[ImGuiCol_TextSelectedBg] = panelActiveColor;
		colors[ImGuiCol_WindowBg] = bgColor;
		colors[ImGuiCol_ChildBg] = bgColor;
		colors[ImGuiCol_PopupBg] = bgColor;
		colors[ImGuiCol_Border] = panelActiveColor;
		colors[ImGuiCol_BorderShadow] = borderColor;
		colors[ImGuiCol_FrameBg] = panelColor;
		colors[ImGuiCol_FrameBgHovered] = panelHoverColor;
		colors[ImGuiCol_FrameBgActive] = panelActiveColor;
		colors[ImGuiCol_TitleBg] = bgColor;
		colors[ImGuiCol_TitleBgActive] = bgColor;
		colors[ImGuiCol_TitleBgCollapsed] = bgColor;
		colors[ImGuiCol_MenuBarBg] = bgColor;
		colors[ImGuiCol_ScrollbarBg] = {0.0, 0.0f, 0.0f, 0.0f};
		colors[ImGuiCol_ScrollbarGrab] = lightBgColor;
		colors[ImGuiCol_ScrollbarGrabHovered] = veryLightBgColor;
		colors[ImGuiCol_ScrollbarGrabActive] = veryLightBgColor;
		colors[ImGuiCol_CheckMark] = panelHoverColor;
		colors[ImGuiCol_SliderGrab] = panelHoverColor;
		colors[ImGuiCol_SliderGrabActive] = panelActiveColor;
		colors[ImGuiCol_Button] = panelColor;
		colors[ImGuiCol_ButtonHovered] = panelHoverColor;
		colors[ImGuiCol_ButtonActive] = panelHoverColor;
		colors[ImGuiCol_Header] = bgColor;
		colors[ImGuiCol_HeaderHovered] = panelHoverColor;
		colors[ImGuiCol_HeaderActive] = panelActiveColor;
		colors[ImGuiCol_Separator] = panelColor;
		colors[ImGuiCol_SeparatorHovered] = panelHoverColor;
		colors[ImGuiCol_SeparatorActive] = panelActiveColor;
		colors[ImGuiCol_ResizeGrip] = panelColor;
		colors[ImGuiCol_ResizeGripHovered] = panelHoverColor;
		colors[ImGuiCol_ResizeGripActive] = bgColor;
		colors[ImGuiCol_PlotLines] = panelActiveColor;
		colors[ImGuiCol_PlotLinesHovered] = panelHoverColor;
		colors[ImGuiCol_PlotHistogram] = panelActiveColor;
		colors[ImGuiCol_PlotHistogramHovered] = panelHoverColor;
		colors[ImGuiCol_DragDropTarget] = bgColor;
		colors[ImGuiCol_NavHighlight] = bgColor;
		colors[ImGuiCol_DockingPreview] = panelActiveColor;
		colors[ImGuiCol_Tab] = ColorFromBytes(25, 25, 26);
		colors[ImGuiCol_TabActive] = panelHoverColor;
		colors[ImGuiCol_TabUnfocused] = panelActiveColor;
		colors[ImGuiCol_TabUnfocusedActive] = panelActiveColor;
		colors[ImGuiCol_TabHovered] = panelHoverColor;
		colors[ImGuiCol_ModalWindowDimBg] = ColorFromBytes(0, 0, 0, 80);

		// Docking
		colors[ImGuiCol_DockingPreview] = ColorFromBytes(0, 85, 70);

		auto& style = ImGui::GetStyle();
		style.TabRounding = 3.0f;
		style.ScrollbarRounding = 5.0f;
		style.WindowRounding = 4.0f;
		style.GrabRounding = 2.0f;
		style.FrameRounding = 4.0f;
		style.PopupRounding = 4.0f;
		style.ChildRounding = 4.0f;
		style.WindowMinSize = {220, 100};
		style.ItemInnerSpacing = { 10.0f, 7.0f };
		style.FramePadding = { 10.0f, 5.0f };
	}
}