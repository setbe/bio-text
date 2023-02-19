#include "StyleView.h"

namespace bt
{
	void StyleView::RenderGUI()
	{
		int* font_size = style->getFontSize();
		float size_coef = (float)(*font_size) / 10;
		style->CorrectToFontSize();

		ImGui::Begin(getName());
		if (ImGui::CollapsingHeader("General##Style"))
		{
			ImGui::SliderInt("Font Size##Style", font_size, 10, 200);
			ImGui::SliderInt("Cursive##Style", style->getCursive(), -(*font_size), *font_size);
			ImGui::SliderFloat("Thickness##Style", style->getThickness(), 0.1f, size_coef);
			ImGui::SliderFloat("Curl##Style", style->getCurl(), 0.0f, size_coef);
			ImGui::ColorEdit4("Color##Style", style->getColor());
			ImGui::NewLine();
		}

		if (ImGui::CollapsingHeader("Random##Style"))
		{
			ImGui::SliderInt("Font Size##sr", style->getFontSizeRandom(), 0, (*font_size));
			ImGui::SliderInt("Cursive##sr", style->getCursiveRandom(), 0, (*font_size));
			ImGui::SliderFloat("Thickness##sr", style->getThicknessRandom(), 0.0f, size_coef);
			ImGui::SliderFloat("Curl##sr", style->getCurlRandom(), 0.0f, size_coef);

			ImGui::ColorEdit4("Color##sr", style->getColorRandom());
			ImGui::SliderInt("Seed##sr", style->getSeed(), 0, 9999);
		}
		ImGui::End();
	}
}