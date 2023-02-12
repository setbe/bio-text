#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <glm/glm.hpp>
#include <string>

#include "StyleView.h"
#include "Texture.h"
#include "shaderClass.h"
#include "File Browser/ImFileBrowser.h"

namespace bt
{
	class ImageView
	{
	public:
		ImageView();
		~ImageView();

		bool Open(std::string name);
		
		Style* getStyle()
		{ return style; }

		void RenderImage();

		ImGui::FileBrowser dialog;
		std::function<void(const std::string&)> ImageLoadCallback;


	protected:
		Shader* shader;
	
	private:
		std::string name;
		Style* style;
		Texture* tex;
		int position[2];
		int dsize[2];
		float scale;
	};
}