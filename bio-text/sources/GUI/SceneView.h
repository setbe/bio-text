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

namespace bt
{
	class SceneView : public DockWidget
	{
	public:
		SceneView();

		void Render() override;
		void Delete();

		std::unique_ptr<StyleView> style_view;
	private:
		std::unique_ptr<ImageView> image_view;
		VAO* vao;
		VBO* vbo;
		EBO* ebo;
		Shader* shader_program;
		GLuint uniID;
	};
}