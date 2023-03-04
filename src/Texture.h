#ifndef TEXTURE_CLASS_H
#define TEXTURE_CLASS_H

#include<glad/glad.h>
#include<stb/stb_image.h>
#pragma warning (disable : 4996)
#include <filesystem>

#include"shaderClass.h"

class Texture
{
public:
	GLuint ID;
	GLenum type;

#if _MSC_VER
    Texture(const wchar_t* image, GLenum texType, GLenum slot, GLenum format, GLenum pixelType, int* w, int* h);
#else
    Texture(const char* image, GLenum texType, GLenum slot, GLenum format, GLenum pixelType, int* w, int* h);
#endif // _MSC_VER

	// Assigns a texture unit to a texture
	void texUnit(Shader* shader, const char* uniform, GLuint unit);
	// Binds a texture
	void Bind();
	// Unbinds a texture
	void Unbind();
	// Deletes a texture
	void Delete();
};
#endif
