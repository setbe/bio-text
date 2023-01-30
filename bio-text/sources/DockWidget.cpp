#include "DockWidget.h"

namespace bt {
	DockWidget::DockWidget(const char* name)
	{
		this->name = name;
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