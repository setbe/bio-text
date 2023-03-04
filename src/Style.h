#ifndef STYLE_H
#define STYLE_H
#include "imgui.h"
#include <stdint.h>

namespace bt {
	constexpr ImVec4 ColorFromBytes(uint8_t r, uint8_t g, uint8_t b, uint8_t a = 255);
	void UseDarkTheme();

	class Style
	{
	public:
		Style();
		~Style();

		void CorrectToFontSize();

		int* getFontSize();
		int* getCursive();
		float* getThickness();
		float* getCurl();
		float* getColor();

		int* getFontSizeRandom();
		int* getCursiveRandom();
		float* getThicknessRandom();
		float* getCurlRandom();

		float* getColorRandom();
		int* getSeed();

		

	private:
		// general
		int fontsize;
		int cursive;
		float thickness;
		float curl;
		float* color;

		// random
		int fontsize_random;
		int cursive_random;
		float thickness_random;
		float curl_random;
		float* color_random;
		int seed;
	};
}

#endif // STYLE_H