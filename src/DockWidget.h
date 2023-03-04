#pragma once

#include "Window.h"
#include <imgui_internal.h>

namespace bt {
	class DockWidget
	{
	public:
		DockWidget(const char* name);
		~DockWidget();

		void Dock(ImGuiID node_id);

		const char* getName();

		void Render();

		bool* getShow() { return &show; }

	protected:
		virtual void RenderGUI() {}

	private:
		const char* name;
		bool show;
	};
}