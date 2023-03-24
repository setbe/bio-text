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

	void Save();
	
	void setName(std::string name);
	std::string getName();

private:
	std::string name;

};