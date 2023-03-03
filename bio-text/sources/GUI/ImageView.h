#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <glm/glm.hpp>
#include <string>
#include <functional>

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

		void setImageLoadCallback(const std::function<void(const std::string&)>& callback);
		void Open(const std::string& filepath);
		
		Style* getStyle()
		{ return style; }

		void RenderImage();

		ImGui::FileBrowser dialog;

	protected:
		std::function<void(const std::string&)> ImageLoadCallback;

		Shader* shader;
		std::string current_file;

	private:
		Style* style;
		Texture* tex;
		int position[2] = { 0, 0 };
		int dsize[2] = { 0, 0 };
		float scale;
	};
}