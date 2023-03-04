#pragma once
#include <string>

namespace bt {
	class Window
	{
	public:
		virtual void* getNativeWindow() = 0;
		virtual void setNativeWindow(void* window) = 0;

		virtual void OnScroll(float delta) = 0;
		virtual void OnKey(int key, int scan_code, int action, int mods) = 0;
		virtual void OnResize(int width, int height) = 0;
		virtual void OnClose() = 0;

		std::string title;
	};
}