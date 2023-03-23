add_executable(
${PROJECT_NAME}
resource.h
main.cpp
Style.cpp
Style.h
Curves.cpp
Curves.h
DockWidget.cpp
DockWidget.h
EBO.cpp
EBO.h
Font.cpp
Font.h
FontPanel.cpp
FontPanel.h
FontView.cpp
FontView.h
glad.c
ImageView.cpp
ImageView.h
MainWindow.cpp
MainWindow.h
SceneView.cpp
SceneView.h
shaderClass.cpp
shaderClass.h
stb.cpp
StyleView.cpp
StyleView.h
Texture.cpp
Texture.h
TextView.cpp
TextView.h
VAO.cpp
VAO.h
VBO.cpp
VBO.h
Window.cpp
Window.h
../external/include/glad/glad.h
../external/include/imgui/imgui.cpp
../external/include/imgui/imgui_draw.cpp
../external/include/imgui/imgui_tables.cpp
../external/include/imgui/imgui_widgets.cpp
../external/include/imgui/backends/imgui_impl_glfw.cpp
../external/include/imgui/backends/imgui_impl_opengl3.cpp
)

if(MSVC)
	if(NOT "${CMAKE_GENERATOR}" MATCHES "(Win64|IA64)")
		target_link_libraries(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/../external/lib/glfw3Rel64.lib)
	endif()

	if("${CMAKE_SIZEOF_VOID_P}" STREQUAL "4")
		target_link_libraries(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/../external/lib/glfw3Rel32.lib)
	endif()
else()
	target_link_libraries(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/../external/lib/libglfw3.a)
	#target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)
	set(CMAKE_CXX_FLAGS "-std=c++17 -g")	
	target_link_libraries(${PROJECT_NAME} dl m GL GLU X11 pthread stdc++fs)
endif()

target_include_directories(${PROJECT_NAME} PRIVATE ../src)
target_include_directories(${PROJECT_NAME} PRIVATE ../external/include)
target_include_directories(${PROJECT_NAME} PRIVATE ../external/include/imgui)
target_include_directories(${PROJECT_NAME} PRIVATE ../external/include/FileBrowser)
