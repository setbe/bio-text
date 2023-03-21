#include <string>
#include <vector>
#include <filesystem>
#include "imgui.h"
#include "imgui_internal.h"

class Font
{
public:
	Font();
	~Font();

	std::string getName();
	void Save();

private:
	std::string name;

};