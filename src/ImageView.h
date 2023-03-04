#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <string>
#include <functional>

#include "StyleView.h"
#include "Texture.h"
#include "shaderClass.h"
#include "FileBrowser/ImFileBrowser.h"

namespace bt
{
	class ImageView
	{
	public:
		ImageView();
		~ImageView();

		void setImageLoadCallback(const std::function<void(const std::wstring&)>& callback);
		void OpenImage(const std::wstring& filepath);
		
		Style* getStyle()
		{ return style; }

		void RenderImage();

		ImGui::FileBrowser dialog;

	protected:
		std::function<void(const std::wstring&)> ImageLoadCallback;

		Shader* shader;
		std::wstring current_file;

	private:
		Style* style;
		Texture* tex;
		int position[2] = { 0, 0 };
		int dsize[2] = { 0, 0 };
		float scale;
	};
}