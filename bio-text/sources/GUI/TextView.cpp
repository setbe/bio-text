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
		ImGui::PushStyleColor(ImGuiCol_FrameBg, ColorFromBytes(25, 25, 27));
		ImGui::InputTextMultiline("##text", text, 513, { win->Size.x - 17, win->Size.y - 60});

		ImGui::SetCursorPosX(win->Size.x - 17 - ImGui::CalcTextSize(symbols_counter.c_str()).x);
		ImGui::TextColored(ColorFromBytes(77, 77, 78), symbols_counter.c_str());
		ImGui::PopStyleColor();

		ImGui::End();
	}
}