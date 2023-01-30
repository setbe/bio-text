#include "MainWindow.h"

namespace bt 
{
    void delay()
    {
        auto start = std::chrono::high_resolution_clock::now();
        auto stop = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        while (true)
        {
            stop = std::chrono::high_resolution_clock::now();
            duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
            if (duration.count() >= 20000)
            {
                return;
            }
            else
                std::this_thread::sleep_for(std::chrono::milliseconds(10));
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

                glfwMakeContextCurrent(this->window);
                glfwSwapInterval(1); // Enable vsync

                // Setup Dear ImGui context
                IMGUI_CHECKVERSION();
                ImGui::CreateContext();
                this->io = &(ImGui::GetIO()); (void)io;
                this->io->Fonts->AddFontFromFileTTF("C:\\Windows\\Fonts\\arial.ttf", 14.0f, NULL, io->Fonts->GetGlyphRangesCyrillic());
                this->io->IniFilename = nullptr;
                
                io->ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;
                io->ConfigFlags |= ImGuiConfigFlags_DockingEnable;
                io->ConfigFlags |= ImGuiConfigFlags_ViewportsEnable;

                //ImGui::StyleColorsDark();
                UseDarkTheme();

                ImGui_ImplGlfw_InitForOpenGL(this->window, true);
                ImGui_ImplOpenGL3_Init(glsl_version);

                this->clear_color = ImVec4(0.1f, 0.1f, 0.1f, 1.00f);
                this->success = true;
                this->scene_view = std::make_unique<SceneView>();
                this->image_view = std::make_unique<ImageView>();
                this->style_view = std::make_unique<StyleView>();
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
            bool sff = true;
            int counter = 0;
            float some_float = 0.4;
            
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

        RenderGUI();
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

        //ImGui::PushStyleVar(ImGuiStyleVar_WindowRounding, 0.0f);
        //ImGui::PushStyleVar(ImGuiStyleVar_WindowBorderSize, 0.0f);
        //ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, ImVec2(0.0f, 0.0f));

        ImGuiID id = ImGui::DockSpaceOverViewport(nullptr, ImGuiDockNodeFlags_NoDockingInCentralNode | ImGuiDockNodeFlags_PassthruCentralNode, nullptr);
        ImGuiDockNode* node = ImGui::DockBuilderGetCentralNode(id);

        static auto first_time = true;
        if (first_time)
        {
            first_time = false;
            ImGui::DockBuilderRemoveNode(id);
            ImGui::DockBuilderAddNode(id, ImGuiDockNodeFlags_PassthruCentralNode | ImGuiDockNodeFlags_DockSpace);
            ImGui::DockBuilderSetNodeSize(id, viewport->Size);
            //ImGuiID left_id = ImGui::DockBuilderSplitNode(id, ImGuiDir_Left, 0.3f, nullptr, &id);
            //ImGuiId r_id;
            ImGuiID right_id = ImGui::DockBuilderSplitNode(id, ImGuiDir_Right, 0.3f, nullptr, &id);

            ImGui::DockBuilderDockWindow(image_view->getName(), right_id);
            ImGui::DockBuilderDockWindow(style_view->getName(), right_id);
            ImGui::DockBuilderFinish(id);
        }
        ImGuiWindowClass centralAlways = {};
        centralAlways.DockNodeFlagsOverrideSet |= ImGuiDockNodeFlags_NoTabBar | ImGuiDockNodeFlags_NoDockingOverMe;
        ImGui::SetNextWindowClass(&centralAlways);
        ImGui::SetNextWindowDockID(node->ID, ImGuiCond_Always);
        //ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, { 0, 0 });
        scene_view->Render();
        image_view->Render();
        style_view->Render();
    }

    void MainWindow::RenderGL()
    {

    }

    MainWindow::~MainWindow()
    {
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
        this->size.x = width;
        this->size.y = height;
        //this->scene_view->Resize(width, height);
        //this->image_view->Resize(width, height);
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