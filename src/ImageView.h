#pragma once
#include <imgui.h>
#include <imgui_internal.h>
#include <string>
#include <functional>
#include <filesystem>

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

#if _MSC_VER
        void setImageLoadCallback(const std::function<void(const std::wstring&)>& callback);
		void OpenImage(const std::wstring& filepath);
#else
        void setImageLoadCallback(const std::function<void(const std::string&)>& callback);
		void OpenImage(const std::string& filepath);
#endif // _MSC_VER

		Style* getStyle()
		{ return style; }

		void RenderImage();

		ImGui::FileBrowser dialog;

	protected:
#if _MSC_VER
        std::function<void(const std::wstring&)> ImageLoadCallback;
        std::wstring current_file;
#else
        std::function<void(const std::string&)> ImageLoadCallback;
        std::string current_file;
#endif // _MSC_VER

		Shader* shader;

	private:
		Style* style;
		Texture* tex;
		int position[2] = { 0, 0 };
		int dsize[2] = { 0, 0 };
		float scale;
	};
}
