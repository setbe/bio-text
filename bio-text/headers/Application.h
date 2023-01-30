#ifndef APPLICATION_H
#define APPLICATION_H
#include "MainWindow.h"
#include "SceneView.h"
#include "ImageView.h"
#include "StyleView.h"
#include <memory>

namespace bt 
{
	class App
	{
	public:
		App();
		~App();

		void Run();

	private:
		MainWindow* window;
	};
}

#endif // APPLICATION_H