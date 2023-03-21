#ifndef MAIN_WINDOW_H
#define MAIN_WINDOW_H
#include "glad/glad.h"
#include "imgui.h"
#include "backends/imgui_impl_glfw.h"
#include "backends/imgui_impl_opengl3.h"
#include <stdio.h>
#include <memory>
#include <vector>
#define GL_SILENCE_DEPRECATION
#include "GLFW/glfw3.h"

#include "Style.h"
#include "Window.h"

#include "SceneView.h"
#include "TextView.h"
#include <chrono>
#include <thread>

#if defined(_MSC_VER) && (_MSC_VER >= 1900) && !defined(IMGUI_DISABLE_WIN32_FUNCTIONS)
#pragma comment(lib, "legacy_stdio_definitions")
#endif

namespace bt {
    class MainWindow : Window
    {
    public:
        MainWindow();
        ~MainWindow();

        void Loop();
        void Render();
        void Quit() { running = false; }

        bool isRunning() { return running; }


        void* getNativeWindow() override { return window; }
        
        void setNativeWindow(void* window) override 
        { this->window = (GLFWwindow*)window; }

        void OnScroll(float delta) override;
        void OnKey(int key, int scan_code, int action, int mods) override;
        void OnResize(int width, int height) override;
        void OnClose() override;

    private:
        void init(Window* window);

        void RenderGUI();
        void RenderMenu();

        GLFWwindow* window;
        bool success;
        bool running;
        ImVec4 clear_color;
        ImGuiIO* io;
        std::unique_ptr<SceneView> scene_view;

        bool error_ocurred = false;
        std::exception exception;
    };

    static void OnKeyCallback(GLFWwindow* window, int key, int scan_code, int action, int mods);
    static void OnScrollCallback(GLFWwindow* window, double x_offset, double y_offset);
    static void OnWindowResizeCallback(GLFWwindow* window, int width, int height);
    static void OnWindowCloseCallback(GLFWwindow* window);

}

#endif // MAIN_WINDOW_H