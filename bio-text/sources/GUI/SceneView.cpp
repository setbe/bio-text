#include "SceneView.h"

namespace bt 
{
	SceneView::SceneView() : DockWidget("Scene")
	{
	}

	SceneView::~SceneView()
	{

	}

	void SceneView::Render()
	{
		ImGui::Begin(getName());
		
		ImGui::SetNextWindowSize({ 200.0f, 600.0f });
		//ImGui::MenuItem("File");
		//for (uint32_t i = 0; i < 200; ++i)
		//	ImGui::MenuItem("Item");
		//ImGui::EndMenu();
		ImGui::SameLine();
		ImGui::ButtonEx("Edit");
		ImGui::SameLine();
		ImGui::ButtonEx("View");
		ImGui::Text("%d", ImGui::GetFocusID());

		ImGui::Separator();
		ImGui::End();
	}
}