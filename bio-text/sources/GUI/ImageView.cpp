#include "ImageView.h"

namespace bt
{
	ImageView::ImageView() : DockWidget("Image")
	{
		position[0] = 0;
		position[1] = 0;
	}

	ImageView::~ImageView()
	{

	}

	void ImageView::Render()
	{
		ImGui::Begin(getName());
		ImGui::SliderInt2("Position", position, -500, 500);
		ImGui::End();
	}
}