#include "SceneView.h"

namespace bt 
{
	SceneView::SceneView() : DockWidget("Scene")
	{
		show_popup = false;
	}

	SceneView::~SceneView()
	{

	}

	void SceneView::Render()
	{
		ImGui::Begin(getName());
		ImGui::Text("There is will be scene view sometime.");
		ImGui::End();
	}
}