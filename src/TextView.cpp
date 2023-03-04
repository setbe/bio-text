#include "TextView.h"

namespace bt
{
	TextView::TextView() : DockWidget("Text")
	{
	}

	TextView::~TextView()
	{

	}

	void TextView::RenderGUI()
	{
		symbols_counter = std::to_string(strlen(text));
		symbols_counter += " / 512";

		ImGui::Begin(getName());

		auto win = ImGui::GetCurrentWindow();
		ImGui::PushStyleColor(ImGuiCol_FrameBg, { 0.055f, 0.055f, 0.055f, 1.0f });
		ImGui::InputTextMultiline("##text", text, 513, { win->Size.x - 17, win->Size.y - 60});

		ImGui::SetCursorPosX(win->Size.x - 17 - ImGui::CalcTextSize(symbols_counter.c_str()).x);
		ImGui::TextColored({0.4f, 0.4f, 0.4f, 1.0f}, symbols_counter.c_str());
		ImGui::PopStyleColor();

		ImGui::End();
	}
}