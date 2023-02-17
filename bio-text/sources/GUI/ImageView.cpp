#include "ImageView.h"

namespace bt
{
	ImageView::ImageView()
	{
		scale = 0.4f;
		this->position[0] = this->position[1] = 0;
		style = new Style();
		tex = nullptr;
		shader = nullptr;
	}

	bool ImageView::Open(std::string name)
	{
		this->name = name;
		if (tex)
			return false;

		tex = new Texture(name.c_str(), GL_TEXTURE_2D, GL_TEXTURE0, GL_RGB, GL_UNSIGNED_BYTE, &dsize[0], &dsize[1]);
		this->tex->texUnit(shader, "tex0", 0);

		return true;
	}

	ImageView::~ImageView()
	{
		delete style;
		if (tex)
			tex->Delete();
	}

	void ImageView::RenderImage()
	{
		/*ImGui::SliderInt2("Position", position, -(ImGui::GetWindowSize().x - dsize[0] * scale), ImGui::GetWindowSize().x - dsize[0] * scale);
		ImGui::SliderFloat("Scale", &scale, 0.2f, 5.0f);
		ImGui::NewLine();

		float center_x = (ImGui::GetWindowSize().x - dsize[0] * scale + position[0]) * 0.5f;
		float center_y = (ImGui::GetWindowSize().y - dsize[1] * scale + position[1]) * 0.5f;

		ImGui::SetCursorPos( {center_x, center_y} );
		ImGui::Image((void*)(GLuint)tex->ID, { dsize[0] * scale, dsize[1] * scale });*/
	}
}