#include"Texture.h"

#if _MSC_VER
Texture::Texture(const wchar_t* image, GLenum texType, GLenum slot, GLenum format, GLenum pixelType, int* w, int* h)
#else
Texture::Texture(const char* image, GLenum texType, GLenum slot, GLenum format, GLenum pixelType, int* w, int* h)
#endif // _MSC_VER
{
	// Assigns the type of the texture ot the texture object
	type = texType;

	// Stores the width, height, and the number of color channels of the image
	//int widthImg, heightImg, numColCh;
	// Flips the image so it appears right side up
	//stbi_set_flip_vertically_on_load(true);
	// Reads the image from a file and stores it in bytes
	//unsigned char* bytes = stbi_load(image, &widthImg, &heightImg, &numColCh, 0);

	// Generates an OpenGL texture object
	glGenTextures(1, &ID);
	// Assigns the texture to a Texture Unit
	glActiveTexture(slot);
	glBindTexture(texType, ID);

	// Configures the type of algorithm that is used to make the image smaller or bigger
	glTexParameteri(texType, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_LINEAR);
	glTexParameteri(texType, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

	// Configures the way the texture repeats (if it does at all)
	glTexParameteri(texType, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameteri(texType, GL_TEXTURE_WRAP_T, GL_REPEAT);

	// Extra lines in case you choose to use GL_CLAMP_TO_BORDER
	// float flatColor[] = {1.0f, 1.0f, 1.0f, 1.0f};
	// glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, flatColor);
	if (!w) *w = 0;
	if (!h) *h = 0;

	int imgch;
#if _MSC_VER
    FILE* image_file;
	image_file = _wfopen(image, L"rb");
	unsigned char* bytes = stbi_load_from_file(image_file, w, h, &imgch, 0);
	fclose(image_file);
#else
    unsigned char* bytes = stbi_load(image, w, h, &imgch, 0);
#endif // _MSC_VER


	// Assigns the image to the OpenGL Texture object
	glTexImage2D(texType, 0, GL_RGB, *w, *h, 0, format, pixelType, bytes);
	// Generates MipMaps
	glGenerateMipmap(texType);

	// Unbinds the OpenGL Texture object so that it can't accidentally be modified
	glBindTexture(texType, 0);

	stbi_image_free(bytes);
}

void Texture::texUnit(Shader* shader, const char* uniform, GLuint unit)
{
	// Gets the location of the uniform
	GLuint texUni = glGetUniformLocation(shader->ID, uniform);
	// Shader needs to be activated before changing the value of a uniform
	shader->Activate();
	// Sets the value of the uniform
	glUniform1i(texUni, unit);
}

void Texture::Bind()
{
	glBindTexture(type, ID);
}

void Texture::Unbind()
{
	glBindTexture(type, 0);
}

void Texture::Delete()
{
	glDeleteTextures(1, &ID);
	delete this;
}
