#include "MainWindow.h"

namespace bt
{
    extern unsigned char logo[];

    void delay()
    {
        auto start = std::chrono::high_resolution_clock::now();
        auto stop = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        while (true)
        {
            stop = std::chrono::high_resolution_clock::now();
            duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
            if (duration.count() >= 10000)
            {
                return;
            }
            else
                std::this_thread::sleep_for(std::chrono::milliseconds(12));
        }
    }

    MainWindow::MainWindow()
    {
        this->window = nullptr;
        this->io = nullptr;
        this->running = false;
        this->success = false;

        if (glfwInit())
        {
            const char* glsl_version = "#version 330";
            glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
            glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
            glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

            this->window = glfwCreateWindow(1200, 600, "BioText", NULL, NULL);
            if (this->window)
            {
                init(this);
                glfwSetKeyCallback(window, OnKeyCallback);
                glfwSetScrollCallback(window, OnScrollCallback);
                glfwSetWindowSizeCallback(window, OnWindowResizeCallback);
                glfwSetWindowCloseCallback(window, OnWindowCloseCallback);
                glfwSetWindowSizeLimits(window, 880, 500, 999999, 999999);

                glfwMakeContextCurrent(this->window);
                glfwSwapInterval(1); // Enable vsync

                // Setup Dear ImGui context
                IMGUI_CHECKVERSION();
                ImGui::CreateContext();
                this->io = &(ImGui::GetIO()); (void)io;
#if _MSC_VER
                io->Fonts->AddFontFromFileTTF("C:\\Windows\\Fonts\\arial.ttf", 15.0f, NULL, io->Fonts->GetGlyphRangesCyrillic());
#else
                io->Fonts->AddFontFromFileTTF("Ubuntu-L.ttf", 15.0f, NULL, io->Fonts->GetGlyphRangesCyrillic());
#endif // _MSC_VER

                this->io->IniFilename = nullptr;

                io->ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;
                io->ConfigFlags |= ImGuiConfigFlags_DockingEnable;
                io->ConfigFlags |= ImGuiConfigFlags_ViewportsEnable;

                //ImGui::StyleColorsDark();
                UseDarkTheme();

                ImGui_ImplGlfw_InitForOpenGL(this->window, true);
                ImGui_ImplOpenGL3_Init(glsl_version);

                GLFWimage img;
                img.height = 32;
                img.width = 32;
                img.pixels = logo;
                glfwSetWindowIcon(window, 1, &img);

                this->clear_color = ImVec4(0.1f, 0.1f, 0.1f, 1.00f);
                this->success = true;

                gladLoadGL();

                this->scene_view = std::make_unique<SceneView>();
            }
            else
            {
                this->success = false;
            }
        }
        else
        {
            this->success = false;
        }
    }

    void MainWindow::Loop()
    {
        if (this->success)
        {
            this->running = true;

            while (!glfwWindowShouldClose(this->window) && this->running)
            {
                glfwPollEvents();
                Render();
            }
        }
    }

    void MainWindow::Render()
    {
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();

        if (!error_ocurred)
        {
            try
            {
                RenderGUI();
            }
            catch (const std::exception& e)
            {
                exception = e;
                error_ocurred = true;
            }
        }
        else
        {
            ImGui::Begin("Error");

            ImGui::TextColored({ 1.0f, 0.0f, 0.0f, 1.0f }, "Error occurred: %s", exception.what());

            ImGui::End();
        }
        ImGui::Render();

        int display_w, display_h;
        glfwGetFramebufferSize(this->window, &display_w, &display_h);
        glViewport(0, 0, display_w, display_h);
        glClearColor(clear_color.x * clear_color.w, clear_color.y * clear_color.w, clear_color.z * clear_color.w, clear_color.w);
        glClear(GL_COLOR_BUFFER_BIT);
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());



        if (this->io->ConfigFlags & ImGuiConfigFlags_ViewportsEnable)
        {
            GLFWwindow* backup_current_context = glfwGetCurrentContext();
            ImGui::UpdatePlatformWindows();
            ImGui::RenderPlatformWindowsDefault();
            glfwMakeContextCurrent(backup_current_context);
        }

        glfwSwapBuffers(this->window);
        delay();
    }

    void MainWindow::RenderGUI()
    {
        ImGuiViewport* viewport = ImGui::GetMainViewport();
        ImGui::SetNextWindowPos(viewport->Pos);
        ImGui::SetNextWindowSize(viewport->Size);
        ImGui::SetNextWindowViewport(viewport->ID);

        ImGuiID id = ImGui::DockSpaceOverViewport(nullptr, ImGuiDockNodeFlags_NoDockingInCentralNode | ImGuiDockNodeFlags_PassthruCentralNode, nullptr);
        ImGuiDockNode* node = ImGui::DockBuilderGetCentralNode(id);

        static auto first_time = true;
        if (first_time)
        {
            first_time = false;
            ImGui::DockBuilderRemoveNode(id);
            ImGui::DockBuilderAddNode(id, ImGuiDockNodeFlags_PassthruCentralNode | ImGuiDockNodeFlags_DockSpace);
            ImGui::DockBuilderSetNodeSize(id, viewport->Size);
            ImGuiID left_id = ImGui::DockBuilderSplitNode(id, ImGuiDir_Left, 0.2f, nullptr, &id);
            ImGuiID right_id = ImGui::DockBuilderSplitNode(id, ImGuiDir_Right, 0.25f, nullptr, &id);

            scene_view->style_view->Dock(right_id);
            scene_view->text_view->Dock(left_id);
            scene_view->font_panel->Dock(left_id);
            ImGui::DockBuilderFinish(id);
            scene_view->font_panel->UpdateFontNames();
        }
        ImGuiWindowClass centralAlways = {};
        centralAlways.DockNodeFlagsOverrideSet |= ImGuiDockNodeFlags_NoTabBar;
        ImGui::SetNextWindowClass(&centralAlways);
        ImGui::SetNextWindowDockID(node->ID, ImGuiCond_Always);
        scene_view->Render();

        RenderMenu();
    }

    void MainWindow::RenderMenu()
    {
        ImGui::PushStyleVar(ImGuiStyleVar_ItemSpacing, { 15.0f, 8.0f });
        ImGui::PushStyleVar(ImGuiStyleVar_WindowBorderSize, 0.0f);
        if (ImGui::BeginMainMenuBar())
        {
            if (ImGui::BeginMenu("File"))
            {
                if (ImGui::BeginMenu("Open"))
                {
                    if (ImGui::MenuItem("Image", "Ctrl + O"))
                    {
                        scene_view->dialog.Open();
                    }
                    ImGui::MenuItem("Font", "Ctrl + [");
                    ImGui::EndMenu();
                }

                bool close_button_disabled = scene_view->getCurrentEditType() == Edit::None ? false : true;
                if (ImGui::MenuItem("Close", "Ctrl + W", nullptr, close_button_disabled))
                {
                    scene_view->setEditType(Edit::None);
                }

                ImGui::EndMenu();
            }

            if (ImGui::BeginMenu("Edit"))
            {
                if (ImGui::MenuItem("Image##editor"))
                    scene_view->setEditType(Edit::Image);

                if (ImGui::MenuItem("Font##editor"))
                    scene_view->setEditType(Edit::Font);

                ImGui::EndMenu();
            }
            ImGui::EndMainMenuBar();
        }
        ImGui::PopStyleVar(2);
    }

    MainWindow::~MainWindow()
    {
        scene_view->Delete();
        ImGui_ImplOpenGL3_Shutdown();
        ImGui_ImplGlfw_Shutdown();
        ImGui::DestroyContext();

        glfwDestroyWindow(this->window);
        glfwTerminate();
    }

    void MainWindow::init(Window* window)
    {
        window->setNativeWindow(this->window);
        glfwSetWindowUserPointer(this->window, window);
    }

    void MainWindow::OnScroll(float delta)
    {

    }

    void MainWindow::OnKey(int key, int scan_code, int action, int mods)
    {

    }

    void MainWindow::OnResize(int width, int height)
    {
        this->Render();
    }

    void MainWindow::OnClose()
    {
        running = false;
    }

    static void OnKeyCallback(GLFWwindow* window, int key, int scan_code, int action, int mods)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnKey(key, scan_code, action, mods);
    }

    static void OnScrollCallback(GLFWwindow* window, double x_offset, double y_offset)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnScroll(y_offset);
    }

    static void OnWindowResizeCallback(GLFWwindow* window, int width, int height)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnResize(width, height);
    }

    static void OnWindowCloseCallback(GLFWwindow* window)
    {
        auto window_ptr = static_cast<Window*>(glfwGetWindowUserPointer(window));
        window_ptr->OnClose();
    }
}
