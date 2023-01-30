#pragma once
#include <imgui.h>
#include "DockWidget.h"
#include <imgui_internal.h>

namespace bt
{
	class SceneView : public DockWidget
	{
	public:
		SceneView();
		~SceneView();

		void Render() override;

	private:
		bool show_popup;
	};
}