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

	class SceneView : public DockWidget, public ImageView
	{
	public:
		SceneView();

		void Delete();

		std::unique_ptr<StyleView> style_view;

		void ChangeEditType(Edit value);
		Edit getCurrentEditType() { return edit_type; }

		std::unique_ptr<FontView> font_view;

	private:
		void RenderGUI() override;

		VAO* vao;
		VBO* vbo;
		EBO* ebo;
		GLuint uniID;

		Edit edit_type;
	};
}