#include "Application.h"

namespace bt {
	App::App()
	{
		window = new MainWindow();
	}

	App::~App()
	{
		delete window;
	}

	void App::Run()
	{
		window->Loop();
	}
}