﻿#include "SceneView.h"

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

		setImageLoadCallback( 
		[this](std::wstring filepath) 
		{ 
			OpenImage(filepath);
			setEditType(Edit::Image);
		});
	}

	void SceneView::setEditType(Edit type)
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
		ImGui::Begin(getName(), nullptr, ImGuiWindowFlags_NoScrollWithMouse | ImGuiWindowFlags_HorizontalScrollbar);

		// draw borders
		ImVec2 canvas_p0 = ImGui::GetCursorScreenPos();
		ImVec2 canvas_sz = ImGui::GetContentRegionAvail();
		canvas_sz.y = canvas_sz.x;
		ImVec2 canvas_p1 = ImVec2(canvas_p0.x + canvas_sz.x, canvas_p0.y + canvas_sz.x);

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

		dialog.Display();
		if (dialog.HasSelected())
		{
			auto file_path = dialog.GetSelected().wstring();
			current_file = file_path.substr(file_path.find_last_of(L"/\\") + 1);
			
			ImageLoadCallback(file_path);

			dialog.ClearSelected();
		}
	}
}