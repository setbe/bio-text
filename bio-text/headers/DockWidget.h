#pragma once

#include <glm/glm.hpp>
#include "GUIObject.h"
#include "Window.h"
#include <imgui_internal.h>

namespace bt {
	class DockWidget : protected GUIObject
	{
	public:
		DockWidget(const char* name);
		~DockWidget();

		void Resize(int32_t w, int32_t h) 
		{
			size.x = w;
			size.y = h;
		}
		void Resize(float w, float h)
		{
			size.x = w;
			size.y = h;
		}

		void Dock(ImGuiID node_id);

		const char* getName();

		virtual void Render() {}
	private:
		const char* name;
	};
}