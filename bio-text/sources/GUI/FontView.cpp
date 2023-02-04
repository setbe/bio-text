#include "FontView.h"

using namespace bt;

static std::list<ImVec2> HelpManipulateControlPoint(Curve* curve, const ImVec4 canvas)
{
    int point_index = 0;
    std::list<ImVec2> points;
    ImVec2 p;

    for (BezierPoint& bp : curve->points)
    {
        for (int i = 0; i < 3; i++)
        {
            switch (i)
            {
            case 0:
                p = bp.left;
                break;
            case 1:
                p = bp.point;
                break;
            case 2:
                p = bp.right;
                break;

            default:
                break;
            }
            static int selected_control_point = -1;

            // current point control
            ImVec2 point = ImVec2(canvas.x + p.x * canvas.z, canvas.y + p.y * canvas.w);

            bool hovered = false;
            if (ImGui::IsItemHovered())
            {
                if (ImGui::IsMouseHoveringRect(
                    ImVec2(point.x - 7 * 0.5f, point.y - 7 * 0.5f),
                    ImVec2(point.x + 7 * 0.5f, point.y + 7 * 0.5f)))
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
            draw_list->AddRect({ point.x - 5, point.y - 5 }, { point.x + 5, point.y + 5 }, (selected_control_point == point_index) ? IM_COL32(255, 255, 255, 100) :
                (hovered) ? IM_COL32(155, 155, 155, 100) : IM_COL32(0, 0, 0, 155), 0.0f, 0, 1.0f);

            // unselect point
            if (ImGui::IsMouseReleased(ImGuiMouseButton_Left))
                selected_control_point = -1;

            // move point, will be updated on next frame
            if (selected_control_point == point_index &&
                ImGui::IsMouseDragging(ImGuiMouseButton_Left, 0.0f))
            {
                ImGuiIO& io = ImGui::GetIO();
                p.x += io.MouseDelta.x / (canvas.z + 1e-5f);
                p.y += io.MouseDelta.y / (canvas.w + 1e-5f);
            }
            point_index++;

            points.push_back(point);
        }
    }
    return points;
}

ImVec2 ImQuadBezierCalc(const ImVec2& p1, const ImVec2& p2, const ImVec2& p3, float t)
{
    float u = 1.0f - t;
    float w1 = u * u;
    float w2 = 2 * u * t;
    float w3 = t * t;
    return ImVec2(w1 * p1.x + w2 * p2.x + w3 * p3.x, w1 * p1.y + w2 * p2.y + w3 * p3.y);
}

static void PathQuadBezierToCasteljau(ImVector<ImVec2>* path, float x1, float y1, float x2, float y2, float x3, float y3, float tess_tol, int level)
{
    float dx = x3 - x1, dy = y3 - y1;
    float det = (x2 - x3) * dy - (y2 - y3) * dx;
    if (det * det * 4.0f < tess_tol * (dx * dx + dy * dy))
    {
        path->push_back(ImVec2(x3, y3));
    }
    else if (level < 10)
    {
        float x12 = (x1 + x2) * 0.5f, y12 = (y1 + y2) * 0.5f;
        float x23 = (x2 + x3) * 0.5f, y23 = (y2 + y3) * 0.5f;
        float x123 = (x12 + x23) * 0.5f, y123 = (y12 + y23) * 0.5f;
        PathQuadBezierToCasteljau(path, x1, y1, x12, y12, x123, y123, tess_tol, level + 1);
        PathQuadBezierToCasteljau(path, x123, y123, x23, y23, x3, y3, tess_tol, level + 1);
    }
}

void FontView::Render()
{
    // canvas from last tab
    // Using InvisibleButton() as a convenience 1) it will advance the layout cursor and 2) allows us to use IsItemHovered()/IsItemActive()
    ImVec2 canvas_p0 = ImGui::GetCursorScreenPos();      // ImDrawList API uses screen coordinates!
    ImVec2 canvas_sz = ImGui::GetContentRegionAvail();   // Resize canvas to what's available
    if (canvas_sz.x < 50.0f) canvas_sz.x = 50.0f;
    if (canvas_sz.y < 50.0f) canvas_sz.y = 50.0f;
    ImVec2 canvas_p1 = ImVec2(canvas_p0.x + canvas_sz.x, canvas_p0.y + canvas_sz.y);

    // Draw border and background color
    ImGuiIO& io = ImGui::GetIO();
    ImDrawList* draw_list = ImGui::GetWindowDrawList();
    draw_list->AddRectFilled(canvas_p0, canvas_p1, IM_COL32(50, 50, 50, 255));
    draw_list->AddRect(canvas_p0, canvas_p1, IM_COL32(255, 255, 255, 255));

    // This will catch our interactions, only left button, no scrolling on this one
    ImGui::InvisibleButton("canvas", canvas_sz, ImGuiButtonFlags_MouseButtonLeft);
    ImVec4 canvas_rc = ImVec4(canvas_p0.x, canvas_p0.y, canvas_p1.x - canvas_p0.x, canvas_p1.y - canvas_p0.y);

    draw_list->PushClipRect(canvas_p0, canvas_p1, true); // canvas clipping
    {
        draw_list->ChannelsSplit(2); // split channels

         // calc and render control point in top layer
        draw_list->ChannelsSetCurrent(1);

        auto points = HelpManipulateControlPoint(curve.get(), canvas_rc);

        // render curve and edges in bottom layer
        draw_list->ChannelsSetCurrent(0);
        const ImU32 curve_color = IM_COL32(255, 255, 0, 255);
       
        if (points.size() > 1)
        {
            for (size_t i = 0; i < points.size() / 3; i++)
            {
                std::list<ImVec2> vecs = curve->GetPointsToDraw(points, i);
                auto it = vecs.begin();

                ImVec2 vec1 = *it; ++it;
                ImVec2 vec2 = *it; ++it;
                ImVec2 vec3 = *it; ++it;
                ImVec2 vec4 = *it;
                draw_list->AddBezierCubic(vec1, vec2, vec3, vec4, curve_color, 2.0f, 15);
                draw_list->AddLine(vec1, vec2, IM_COL32(255, 255, 255, 20), 1.0f);
                draw_list->AddLine(vec2, vec3, IM_COL32(255, 255, 255, 20), 1.0f);
            }
        }
        draw_list->ChannelsMerge(); // merge channels
    }
    draw_list->PopClipRect();
}