#include "FontView.h"

using namespace bt;

bool isPointOnCanvas(ImVec4 canvas, ImVec2 point)
{
    

    return false;
}

inline ImVec2 cnvPoint(ImVec4 canvas, ImVec2 point)
{
    return { canvas.x + point.x * (canvas.z + 1e-5f), canvas.y + point.y * (canvas.w + 1e-5f) };
}

inline ImVec2 ntvPoint(ImVec4 canvas, ImVec2 point)
{
    return { (point.x) / (canvas.z + 1e-5f), (point.y) / (canvas.w + 1e-5f) };
}

static void HelpManipulateControlPoint(Curve* curve, const ImVec4 canvas)
{
    int count = 0;
    int point_index = 0;
    std::list<BezierPoint> points;
    ImVec2* p;

    if (ImGui::IsItemHovered())
    {
        if (!ImGui::IsKeyPressed(ImGuiKey_LeftAlt) && ImGui::IsKeyPressed(ImGuiKey_LeftCtrl) && ImGui::IsMouseClicked(ImGuiMouseButton_Right))
        {
            ImVec2 p = { ImGui::GetMousePos().x - ImGui::GetWindowPos().x - 7.0f, ImGui::GetMousePos().y - ImGui::GetWindowPos().y - 7.0f };
            ImVec2 p_left = { p.x - 20.0f, p.y };
            ImVec2 p_right = { p.x + 20.0f, p.y };

            curve->AddPoint(BezierPoint(ntvPoint(canvas, p_left), ntvPoint(canvas, p), ntvPoint(canvas, p_right)));
        }
    }

    for (BezierPoint& bp : curve->points)
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
            if (i != 1)         // directional bezier's point
            {
                draw_list->AddRect({ point.x - 5, point.y - 5 }, { point.x + 5, point.y + 5 }, (selected_control_point == point_index) ? IM_COL32(255, 255, 255, 100) :
                    (hovered) ? IM_COL32(155, 155, 155, 100) : IM_COL32(0, 0, 0, 155), 0.0f, 0, 1.0f);
            }
            else                // main bezier's point
            {
                draw_list->AddRect({ point.x - 5, point.y - 5 }, { point.x + 5, point.y + 5 }, (selected_control_point == point_index) ? IM_COL32(80, 200, 120, 255) :
                    (hovered) ? IM_COL32(48, 119, 71, 255) : IM_COL32(48, 119, 71, 155), 0.0f, 0, 1.0f);
            }

            // unselect point
            if (ImGui::IsMouseReleased(ImGuiMouseButton_Left))
                selected_control_point = -1;

            // move point, will be updated on next frame
            if (selected_control_point == point_index &&
                ImGui::IsMouseDragging(ImGuiMouseButton_Left, 0.0f) &&
                ImGui::IsItemHovered())
            {
                ImGuiIO& io = ImGui::GetIO();
                if (i != 1 && !ImGui::IsKeyDown(ImGuiKey_Space))
                {
                    if (ImGui::IsKeyDown(ImGuiKey_LeftCtrl))
                    {
                        p->x += io.MouseDelta.x / (canvas.z + 1e-5f);
                        p->y += io.MouseDelta.y / (canvas.w + 1e-5f);
                    }
                    else
                    {
                        float x = io.MouseDelta.x / (canvas.z + 1e-5f);
                        float y = io.MouseDelta.y / (canvas.w + 1e-5f);

                        if (i == 0)
                        {
                            bp.left.x += x;   
                            bp.left.y += y;
                            
                            bp.right.x -= x;   
                            bp.right.y -= y;
                        }
                        else
                        {
                            bp.right.x += x;
                            bp.right.y += y;

                            bp.left.x -= x;
                            bp.left.y -= y;
                        }
                    }
                }
                else
                {
                    if (ImGui::IsKeyDown(ImGuiKey_LeftAlt))
                    {
                        curve->DeletePoint(count);
                        return;
                    }

                    float x = io.MouseDelta.x / (canvas.z + 1e-5f);
                    float y = io.MouseDelta.y / (canvas.w + 1e-5f);

                    bp.left.x += x;    
                    bp.left.y += y;
                    
                    if (!ImGui::IsKeyDown(ImGuiKey_LeftCtrl))
                    {
                        bp.point.x += x;
                        bp.point.y += y;
                    }

                    bp.right.x += x;   
                    bp.right.y += y;
                }
            }
            point_index++;
        }
        count++;
    }
    return;
}

void FontView::Render()
{
    // canvas from last tab
    // Using InvisibleButton() as a convenience 1) it will advance the layout cursor and 2) allows us to use IsItemHovered()/IsItemActive()
    ImGui::SetCursorPosY(ImGui::GetCursorPosY() + 13.0f);
    ImVec2 canvas_p0 = ImGui::GetCursorScreenPos();      // ImDrawList API uses screen coordinates!
    ImVec2 canvas_sz = ImGui::GetContentRegionAvail();   // Resize canvas to what's available
    if (canvas_sz.x < 50.0f) canvas_sz.x = 50.0f;
    if (canvas_sz.y < 50.0f) canvas_sz.y = 50.0f;
    ImVec2 canvas_p1 = ImVec2(canvas_p0.x + canvas_sz.x, canvas_p0.y + canvas_sz.x);

    // Draw border and background color
    ImGuiIO& io = ImGui::GetIO();
    ImDrawList* draw_list = ImGui::GetWindowDrawList();
    draw_list->AddRectFilled(canvas_p0, canvas_p1, IM_COL32(33, 33, 34, 255));
    //draw_list->AddRect(canvas_p0, canvas_p1, IM_COL32(255, 255, 255, 255));

    // This will catch our interactions, only left button, no scrolling on this one
    ImGui::InvisibleButton("canvas", canvas_sz, ImGuiButtonFlags_MouseButtonLeft);
    ImVec4 canvas_rc = ImVec4(canvas_p0.x, canvas_p0.y, canvas_p1.x - canvas_p0.x, canvas_p1.y - canvas_p0.y);

    draw_list->PushClipRect(canvas_p0, canvas_p1, true); // canvas clipping
    {
        draw_list->ChannelsSplit(2); // split channels

         // calc and render control point in top layer
        draw_list->ChannelsSetCurrent(1);

        HelpManipulateControlPoint(curve.get(), canvas_rc);

        // render curve and edges in bottom layer
        draw_list->ChannelsSetCurrent(0);
        const ImU32 curve_color = IM_COL32(80, 200, 120, 255);

        BezierPoint last = curve->points.front();

        auto it = curve->points.begin();
        std::advance(it, 1);

        for (; it != curve->points.end(); it++)
        {
            ImVec2 vec1 = cnvPoint(canvas_rc, last.point);
            ImVec2 vec2 = cnvPoint(canvas_rc, last.right);
            ImVec2 vec3 = cnvPoint(canvas_rc, it->left);
            ImVec2 vec4 = cnvPoint(canvas_rc, it->point);

            draw_list->AddBezierCubic(vec1, vec2, vec3, vec4, curve_color, 2.0f, 20);

            draw_list->AddLine(vec1, vec2, IM_COL32(255, 255, 255, 20), 1.0f);
            draw_list->AddLine(vec3, vec4, IM_COL32(255, 255, 255, 20), 1.0f);
            draw_list->AddLine(cnvPoint(canvas_rc, last.left), cnvPoint(canvas_rc, last.point), IM_COL32(255, 255, 255, 20), 1.0f);
            draw_list->AddLine(cnvPoint(canvas_rc, it->point), cnvPoint(canvas_rc, it->right), IM_COL32(255, 255, 255, 20), 1.0f);

            last = *it;
        }
        draw_list->ChannelsMerge(); // merge channels
    }
    draw_list->PopClipRect();
}