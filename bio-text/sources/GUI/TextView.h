#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <memory>
#include "DockWidget.h"

namespace bt
{
	class TextView : public DockWidget
	{
	public:
		TextView();
		~TextView();

		void Render() override;

	private:
		char text[512];
	};
}