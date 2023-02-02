#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <glm/glm.hpp>
#include <string>

#include "StyleView.h"
#include "Texture.h"
#include "shaderClass.h"

namespace bt
{
	class ImageView
	{
	public:
		ImageView(Shader* shader);
		~ImageView();

		bool Open(std::string name);
		
		Style* getStyle()
		{ return style; }

		void Render();

	private:
		std::string name;
		Style* style;
		Texture* tex;
		int position[2];
		int dsize[2];
		float scale;
		Shader* shader = nullptr;
	};
}