#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <memory>
#include "DockWidget.h"

namespace bt
{
	class SceneView : public DockWidget
	{
	public:
		SceneView();
		~SceneView();

		void Render() override;
	};
}