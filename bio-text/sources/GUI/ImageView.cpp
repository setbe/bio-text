#include "ImageView.h"

namespace bt
{
	void ImageView::setImageLoadCallback(const std::function<void(const std::string&)>& callback)
	{
		ImageLoadCallback = callback;
	}

	ImageView::ImageView()
	{
		current_file = "< ... >";
		dialog.SetTitle("Open image");
		dialog.SetFileFilters({".png", ".jpg"});

		scale = 0.4f;
		style = new Style();
		tex = nullptr;
		shader = nullptr;
	}

	void ImageView::Open(const std::string& filepath)
	{
		this->current_file = filepath;
		if (tex)
			tex->Delete();

		std::string s = filepath;
		std::string delimiter = ".";

		size_t pos = 0;
		std::string token;
		while ((pos = s.find(delimiter)) != std::string::npos) {
			token = s.substr(0, pos);
			s.erase(0, pos + delimiter.length());
		}

		if (s == "png")
		{
			tex = new Texture(current_file.c_str(), GL_TEXTURE_2D, GL_TEXTURE0, GL_RGBA, GL_UNSIGNED_BYTE, &dsize[0], &dsize[1]);
		}
		else
		{
			tex = new Texture(current_file.c_str(), GL_TEXTURE_2D, GL_TEXTURE0, GL_RGB, GL_UNSIGNED_BYTE, &dsize[0], &dsize[1]);
		}
		this->tex->texUnit(shader, "tex0", 0);
	}

	ImageView::~ImageView()
	{
		delete style;
		if (tex)
			tex->Delete();
	}

	void ImageView::RenderImage()
	{
		if (current_file != "< ... >")
		{
			if (ImGui::IsWindowHovered())
			{
				if (ImGui::GetIO().MouseWheel != 0)							// resize image with mouse wheel
				{
					bool up = ImGui::GetIO().MouseWheel > 0 ? true : false;

					if (up)
					{
						if (scale < 4.0f)
							scale += 0.2f;
					}
					else if (scale > 0.4f)
						scale -= 0.2f;
				}
				if (ImGui::IsMouseDragging(ImGuiMouseButton_Left, 0.0f))	// move image by dragging
				{
					ImVec2 delta = ImGui::GetIO().MouseDelta;
					position[0] += delta.x;
					position[1] += delta.y;
				}
			}

			float center_x = (ImGui::GetWindowSize().x - dsize[0] * scale + position[0]) * 0.5f;
			float center_y = (ImGui::GetWindowSize().y - dsize[1] * scale + position[1]) * 0.5f;

			ImGui::SetCursorPos({ center_x, center_y });
			ImGui::Image((void*)(GLuint)tex->ID, { dsize[0] * scale, dsize[1] * scale });

		}
	}
}