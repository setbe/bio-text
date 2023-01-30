#pragma once
#include <imgui.h>
#include "DockWidget.h"
#include <imgui_internal.h>
#include <glm/glm.hpp>

namespace bt
{
	class ImageView : public DockWidget
	{
	public:
		ImageView();
		~ImageView();

		void Render() override;

	private:
		int position[2];
	};
}