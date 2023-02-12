#include "SceneView.h"

namespace bt 
{
	GLfloat vertices[] =
	{ 
	  // Coords                 Colors              ImgCoords
		-0.5f, -0.5f, 0.0f,     1.0f, 0.0f, 0.0f,	0.0f, 0.0f,
		-0.5f,  0.5f, 0.0f,     0.0f, 1.0f, 0.0f,	0.0f, 1.0f,
		 0.5f,  0.5f, 0.0f,     0.0f, 0.0f, 1.0f,	1.0f, 1.0f,
		 0.5f, -0.5f, 0.0f,     1.0f, 1.0f, 1.0f,	1.0f, 0.0f
	};

	GLuint indices[] =
	{
		0, 2, 1,
		0, 3, 2
	};

	SceneView::SceneView() : DockWidget("Scene"), ImageView()
	{
		this->shader = new Shader("default.vert", "default.frag");
		this->edit_type = Edit::None;
		this->vao = new VAO();
		this->vao->Bind();
		this->vbo = new VBO(vertices, sizeof(vertices));
		this->ebo = new EBO(indices, sizeof(indices));

		this->vao->LinkAttrib(*(this->vbo), 0, 3, GL_FLOAT, 8 * sizeof(float), (void*)0);

		this->vao->Unbind();
		this->vbo->Unbind();
		this->ebo->Unbind();

		this->uniID = glGetUniformLocation(shader->ID, "scale");
		this->style_view = std::make_unique<StyleView>(getStyle());
		this->font_view = std::make_unique<FontView>();
	}

	void SceneView::ChangeEditType(Edit type)
	{
		edit_type = type;
	}

	void SceneView::Delete()
	{
		vao->Delete();
		vbo->Delete();
		ebo->Delete();
		shader->Delete();
	}

	void SceneView::RenderGUI()
	{
		ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, { 0.0f, 0.0f });
		ImGui::Begin(getName(), nullptr, ImGuiWindowFlags_NoScrollbar);
		//dialog.Display();

		// draw borders
		ImVec2 canvas_p0 = ImGui::GetCursorScreenPos();
		ImVec2 canvas_sz = ImGui::GetContentRegionAvail();
		canvas_sz.y = canvas_sz.x;
		ImVec2 canvas_p1 = ImVec2(canvas_p0.x + canvas_sz.x, canvas_p0.y + canvas_sz.x);

		ImDrawList* draw_list = ImGui::GetWindowDrawList();

		draw_list->AddLine({ canvas_p0.x + 1.0f, ImGui::GetCursorScreenPos().y + 26.0f }, { canvas_p0.x + 1.0f, ImGui::GetContentRegionAvail().y + 13.0f + ImGui::GetCursorScreenPos().y }, IM_COL32(29, 121, 106, 255), 1.0f);
		draw_list->AddLine({ canvas_p1.x - 2.0f, ImGui::GetCursorScreenPos().y + 26.0f }, { canvas_p1.x - 2.0f, ImGui::GetContentRegionAvail().y + 13.0f + ImGui::GetCursorScreenPos().y }, IM_COL32(29, 121, 106, 255), 1.0f);


		switch (edit_type)
		{
		case bt::Edit::Image:
			RenderImage();
			break;
		case bt::Edit::Font:
			font_view->Render();
			break;
		default:
			break;
		}

		ImGui::End();
		ImGui::PopStyleVar();
	}
}