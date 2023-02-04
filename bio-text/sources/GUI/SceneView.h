#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <memory>

#include "DockWidget.h"
#include "VAO.h"
#include "VBO.h"
#include "EBO.h"
#include "Texture.h"
#include "ImageView.h"
#include "StyleView.h"
#include "FontView.h"

namespace bt
{
	enum class Edit
	{
		None,
		Image,
		Font
	};

	class SceneView : public DockWidget
	{
	public:
		SceneView();

		void Delete();

		std::unique_ptr<StyleView> style_view;

		void ChangeEditType(Edit what_to_edit);
		Edit getCurrentEditType() { return edit_type; }

		std::unique_ptr<ImageView> image_view;
		std::unique_ptr<FontView> font_view;

	private:
		void RenderGUI() override;

		VAO* vao;
		VBO* vbo;
		EBO* ebo;
		Shader* shader_program;
		GLuint uniID;

		Edit edit_type;
	};
}