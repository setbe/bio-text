#include "DockWidget.h"

namespace bt {
	DockWidget::DockWidget(const char* name)
	{
		this->name = name;
		this->show = true;
	}

	void DockWidget::Render()
	{
		if (show) RenderGUI();
	}

	DockWidget::~DockWidget()
	{

	}

	void DockWidget::Dock(ImGuiID node_id)
	{
		ImGui::DockBuilderDockWindow(name, node_id);
	}

	const char* DockWidget::getName()
	{
		return name;
	}
}