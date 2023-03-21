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
#include "TextView.h"
#include "FontPanel.h"

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

		void setEditType(Edit value);
		Edit getCurrentEditType() { return edit_type; }

		// image
		std::unique_ptr<StyleView> style_view;
		std::unique_ptr<TextView> text_view;

		// font
		std::unique_ptr<FontView> font_view;
		std::unique_ptr<FontPanel> font_panel;

	private:
		void RenderGUI() override;

		VAO* vao;
		VBO* vbo;
		EBO* ebo;
		GLuint uniID;

		Edit edit_type;
	};
}