#include "TextView.h"

namespace bt
{
	TextView::TextView() : DockWidget("Text")
	{

	}

	TextView::~TextView()
	{

	}

	void TextView::Render()
	{
		ImGui::Begin(getName());

		auto win = ImGui::GetCurrentWindow();

		ImGui::InputTextMultiline("##text", text, 512, { win->Size.x - 10, win->Size.y - 40});

		ImGui::End();
	}
}