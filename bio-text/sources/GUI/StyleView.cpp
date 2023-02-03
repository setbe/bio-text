#include "StyleView.h"

namespace bt
{
	void StyleView::RenderGUI()
	{
		int* font_size = style->getFontSize();
		float size_coef = (float)(*font_size) / 10;
		style->CorrectToFontSize();

		ImGui::Begin(getName());
		if (ImGui::CollapsingHeader("Standard"))
		{
			ImGui::SliderInt("Font Size", font_size, 10, 200);
			ImGui::SliderInt("Cursive", style->getCursive(), -(*font_size), *font_size);
			ImGui::SliderFloat("Thickness", style->getThickness(), 0.1f, size_coef);
			ImGui::SliderFloat("Curl", style->getCurl(), 0.0f, size_coef);
			ImGui::ColorEdit4("Color", style->getColor());
			ImGui::NewLine();
		}

		if (ImGui::CollapsingHeader("Random"))
		{
			ImGui::SliderInt("Font Size##r", style->getFontSizeRandom(), 0, (*font_size));
			ImGui::SliderInt("Cursive##r", style->getCursiveRandom(), 0, (*font_size));
			ImGui::SliderFloat("Thickness##r", style->getThicknessRandom(), 0.0f, size_coef);
			ImGui::SliderFloat("Curl##r", style->getCurlRandom(), 0.0f, size_coef);

			ImGui::ColorEdit4("Color##r", style->getColorRandom());
			ImGui::SliderInt("Seed", style->getSeed(), 0, 9999);
		}
		ImGui::End();
	}
}