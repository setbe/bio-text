#include "FontView.h"

using namespace bt;

inline ImVec2 cnvPoint(ImVec4 canvas, ImVec2 point)
{
    return { canvas.x + point.x * (canvas.z + 1e-5f), canvas.y + point.y * (canvas.w + 1e-5f) };
}

inline ImVec2 ntvPoint(ImVec4 canvas, ImVec2 point)
{
    return { (point.x) / (canvas.z + 1e-5f), (point.y) / (canvas.w + 1e-5f) };
}

void FontView::HelpManipulateControlPoint(const ImVec4 canvas)
{
    int curve_n;            // counts curves
    int bezier_n;           // counts bezier curves
    int point_index = 0;    // BezierPoint has 3 points. point_index iterates these points
    std::list<BezierPoint> points;
    ImVec2* p;

    if (ImGui::IsItemHovered() && ImGui::IsMouseClicked(ImGuiMouseButton_Right))
    {
        if (ImGui::IsKeyPressed(ImGuiKey_LeftShift) && curves.size() < 50)     // create new curve
        {
            ImVec2 p = { ImGui::GetMousePos().x - ImGui::GetWindowPos().x - 7.0f, ImGui::GetMousePos().y - ImGui::GetWindowPos().y - 7.0f };
            ImVec2 p_left = { p.x - 10.0f, p.y };
            ImVec2 p_right = { p.x + 10.0f, p.y };
            
            Curve new_curve = Curve();
            new_curve.AddPoint(BezierPoint(ntvPoint(canvas, p_left), ntvPoint(canvas, p), ntvPoint(canvas, p_right)));
            curves.push_back(new_curve);
            selected_curve = &curves.back();
        }

        if (!ImGui::IsKeyPressed(ImGuiKey_LeftAlt) && selected_curve->points.size() < 50)      // create new point on selected curve
        {
            ImVec2 p = { ImGui::GetMousePos().x - ImGui::GetWindowPos().x - 7.0f, ImGui::GetMousePos().y - ImGui::GetWindowPos().y - 7.0f };
            ImVec2 p_left = { p.x - 10.0f, p.y };
            ImVec2 p_right = { p.x + 10.0f, p.y };

            selected_curve->AddPoint(BezierPoint(ntvPoint(canvas, p_left), ntvPoint(canvas, p), ntvPoint(canvas, p_right)));
        }
    }

    curve_n = 0;
    for (Curve& curve : curves)
    {
        bezier_n = 0;
        for (BezierPoint& bp : curve.points)
        {
            for (int i = 0; i < 3; i++)
            {
                p = i == 0 ? &bp.left : i == 1 ? &bp.point : &bp.right;

                static int selected_control_point = -1;

                // current point control
                ImVec2 point = ImVec2(canvas.x + p->x * canvas.z, canvas.y + p->y * canvas.w);

                bool hovered = false;
                if (ImGui::IsItemHovered())
                {
                    if (ImGui::IsMouseHoveringRect(
                        ImVec2(point.x - 10 * 0.5f, point.y - 10 * 0.5f),
                        ImVec2(point.x + 10 * 0.5f, point.y + 10 * 0.5f)))
                    {
                        hovered = true;

                        // select if active and no point was selected before
                        // for have only one point movable at same time
                        if (selected_control_point < 0 && ImGui::IsItemActive())
                            selected_control_point = point_index;
                    }
                }

                ImDrawList* draw_list = ImGui::GetWindowDrawList();
                // draw point edge
                if (i == 1)                             // bezier's point (green)
                {
                    draw_list->AddRect({ point.x - 5, point.y - 5 }, { point.x + 5, point.y + 5 }, (selected_control_point == point_index) ? IM_COL32(135, 255, 175, 255) :
                        (hovered) ? IM_COL32(48, 119, 71, 255) : IM_COL32(48, 119, 71, 155), 0.0f, 0, 1.0f);
                }
                else if (&curve == selected_curve)       // direct point (gray)
                {
                    draw_list->AddRect({ point.x - 5, point.y - 5 }, { point.x + 5, point.y + 5 }, (selected_control_point == point_index) ? IM_COL32(255, 255, 255, 100) :
                        (hovered) ? IM_COL32(155, 155, 155, 100) : IM_COL32(0, 0, 0, 155), 0.0f, 0, 1.0f);
                }

                // unselect point
                if (ImGui::IsMouseReleased(ImGuiMouseButton_Left))
                    selected_control_point = -1;

                // move point, will be updated on next frame
                if (selected_control_point == point_index &&
                    ImGui::IsMouseDragging(ImGuiMouseButton_Left, 0.0f) &&
                    ImGui::IsItemHovered())
                {
                    selected_curve = &curve;
                    ImGuiIO& io = ImGui::GetIO();
                    if (i != 1 && !ImGui::IsKeyDown(ImGuiKey_Space))
                    {
                        if (ImGui::IsKeyDown(ImGuiKey_LeftCtrl))    // direction point move
                        {
                            p->x += io.MouseDelta.x / (canvas.z + 1e-5f);
                            p->y += io.MouseDelta.y / (canvas.w + 1e-5f);
                        }
                        else
                        {
                            float x = io.MouseDelta.x / (canvas.z + 1e-5f);
                            float y = io.MouseDelta.y / (canvas.w + 1e-5f);

                            if (i == 0)                             // if left, move left as control point, else right
                            {
                                bp.left.x += x;
                                bp.left.y += y;

                                bp.RotateRightOppositeLeft();
                            }
                            else
                            {
                                bp.right.x += x;
                                bp.right.y += y;

                                bp.RotateLeftOppositeRight();
                            }
                        }
                    }
                    else                                            // if main point
                    {
                        if (ImGui::GetKeyPressedAmount(ImGuiKey_LeftAlt, 0.5f, 0.5f))   // delete point or curve
                        {
                            if (curve.points.size() > 1)
                            {
                                curve.DeletePoint(bezier_n);
                            }
                            else
                            {
                                auto it = curves.begin();
                                std::advance(it, curve_n);
                                curves.erase(it);

                                if (!curves.empty()) selected_curve = &curves.back();
                            }
                            selected_control_point = -1;
                            return;
                        }

                        float x = io.MouseDelta.x / (canvas.z + 1e-5f);
                        float y = io.MouseDelta.y / (canvas.w + 1e-5f);

                        bp.left.x += x;
                        bp.left.y += y;

                        bp.right.x += x;
                        bp.right.y += y;

                        bp.point.x += x;
                        bp.point.y += y;
                    }
                }
                point_index++;
            
            }
            bezier_n++;
        }
        curve_n++;
    }
}

void FontView::Render()
{
    ImGui::SetCursorScreenPos({ ImGui::GetCursorScreenPos().x, ImGui::GetCursorScreenPos().y + 13.0f });
    ImVec2 canvas_p0 = ImGui::GetCursorScreenPos();      // ImDrawList API uses screen coordinates!
    ImVec2 canvas_sz = ImGui::GetContentRegionAvail();   // Resize canvas to what's available
    
    if (canvas_sz.x < 50.0f) 
        canvas_sz.x = 50.0f;
    
    if (canvas_sz.x > canvas_sz.y) 
    {
        canvas_sz.x = canvas_sz.y;
    }
    else
    {
        canvas_sz.y = canvas_sz.x;
    }

    ImGuiIO& io = ImGui::GetIO();
    ImDrawList* draw_list = ImGui::GetWindowDrawList();

    // padding
    float padding = 10.0f;
    canvas_p0.x += padding;
    canvas_p0.y += padding;
    

    // scale
    if (ImGui::IsWindowHovered())
    {
        if (ImGui::GetIO().MouseWheel != 0)							// resize font edit with mouse wheel
        {
            bool up = ImGui::GetIO().MouseWheel > 0 ? true : false;

            if (up)
            {
                if (ui_scale > 1.2f)
                    ui_scale -= 0.2f;
            }
            else if (ui_scale < 2.5f)
                ui_scale += 0.2f;
        }
    }
    // resize to left dock
    canvas_sz.x /= ui_scale;
    canvas_sz.y /= ui_scale;
    ImVec2 canvas_p1 = ImVec2(canvas_p0.x + canvas_sz.x - padding, canvas_p0.y + canvas_sz.x - padding);

    // left background (editor)
    draw_list->AddRectFilled(canvas_p0, canvas_p1, IM_COL32(30, 30, 31, 255), 4.0f);


    ImGui::InvisibleButton("canvas", canvas_sz, ImGuiButtonFlags_MouseButtonLeft);
    ImVec4 canvas_rc = ImVec4(canvas_p0.x, canvas_p0.y, (canvas_p1.x - canvas_p0.x) * 2.0f, (canvas_p1.y - canvas_p0.y) * 0.2f);

    draw_list->PushClipRect(canvas_p0, canvas_p1, true); // canvas clipping
    {
        draw_list->ChannelsSplit(2); // split channels

         // calc and render control point in top layer
        draw_list->ChannelsSetCurrent(1);

        HelpManipulateControlPoint(canvas_rc);

        // render curve and edges in bottom layer
        draw_list->ChannelsSetCurrent(0);
        const ImU32 curve_color = IM_COL32(80, 200, 120, 255);

        if (!curves.empty() && !curves.front().points.empty())
        {
            BezierPoint last;
            for (const Curve& curve : curves)               // draw all curves
            {
                last = curve.points.front();
                auto it = curve.points.begin();
                std::advance(it, 1);

                for (; it != curve.points.end(); it++)
                {
                    ImVec2 vec1 = cnvPoint(canvas_rc, last.point);
                    ImVec2 vec2 = cnvPoint(canvas_rc, last.right);
                    ImVec2 vec3 = cnvPoint(canvas_rc, it->left);
                    ImVec2 vec4 = cnvPoint(canvas_rc, it->point);

                    draw_list->AddBezierCubic(vec1, vec2, vec3, vec4, curve_color, 2.0f, 20);

                    last = *it;
                }
            }
                                    
            last = selected_curve->points.front();          // draw directional lines for selected curve
            auto it = selected_curve->points.begin();
            std::advance(it, 1);

            for (; it != selected_curve->points.end(); it++)
            {
                ImVec2 vec1 = cnvPoint(canvas_rc, last.point);
                ImVec2 vec2 = cnvPoint(canvas_rc, last.right);
                ImVec2 vec3 = cnvPoint(canvas_rc, it->left);
                ImVec2 vec4 = cnvPoint(canvas_rc, it->point);

                draw_list->AddLine(vec1, vec2, IM_COL32(255, 255, 255, 20), 1.0f);
                draw_list->AddLine(vec3, vec4, IM_COL32(255, 255, 255, 20), 1.0f);
                draw_list->AddLine(cnvPoint(canvas_rc, last.left), cnvPoint(canvas_rc, last.point), IM_COL32(255, 255, 255, 20), 1.0f);
                draw_list->AddLine(cnvPoint(canvas_rc, it->point), cnvPoint(canvas_rc, it->right), IM_COL32(255, 255, 255, 20), 1.0f);

                last = *it;
            }
        }
        
        // right background (preview)
        canvas_sz.x *= 3.0f;
        canvas_sz.y *= 3.0f;
        canvas_p1.x += canvas_sz.x;
        canvas_p1.y += canvas_sz.y;

        //draw_list->AddRectFilled(canvas_p0, canvas_p1, IM_COL32(30, 30, 31, 255), 4.0f);




        draw_list->ChannelsMerge(); // merge channels
    }
    draw_list->PopClipRect();
    //ImGui::PopStyleVar();
}