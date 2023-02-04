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

	SceneView::SceneView() : DockWidget("Scene")
	{
		this->shader_program = new Shader("default.vert", "default.frag");

		this->edit_type = Edit::None;
		this->vao = new VAO();
		this->vao->Bind();
		this->vbo = new VBO(vertices, sizeof(vertices));
		this->ebo = new EBO(indices, sizeof(indices));

		this->vao->LinkAttrib(*(this->vbo), 0, 3, GL_FLOAT, 8 * sizeof(float), (void*)0);

		this->vao->Unbind();
		this->vbo->Unbind();
		this->ebo->Unbind();

		this->uniID = glGetUniformLocation(shader_program->ID, "scale");
		this->image_view = std::make_unique<ImageView>(shader_program);
		this->style_view = std::make_unique<StyleView>(image_view->getStyle());
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
		shader_program->Delete();
	}

	void SceneView::RenderGUI()
	{
		ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, { 10.0f, 10.0f });
		ImGui::Begin(getName());

		switch (edit_type)
		{
		case bt::Edit::Image:
			image_view->Render();
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