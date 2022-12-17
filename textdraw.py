from PIL import Image, ImageDraw, ImageFilter
import math
from style import TextStyle, TextRandom
    
class TextDraw():
    def __init__(self, style: TextStyle = None) -> None:
        self.im = None
        self.canvas = None

        self.style = style if style else TextStyle()
        self.curve_quality = 0.05

        self.offset_x, self.offset_y = 0, 0
        self.local_size = [1, 1]
        self.local_offset = [0, 0]

    '''
    returns point for quadratic bezier
    takes 4 points
    '''
    def bezier_func(self, t, points) -> tuple:      # quadratic bezier function
        resized_points = []
        for point in points:
            resized_points.append(((point[0] * self.style.get_size()) / 100 / self.local_size[0] + self.offset_x + self.local_offset[0],
            (point[1] * self.style.get_size()) / 100 / self.local_size[1] + self.offset_y + self.local_offset[1] ))

        return (
            math.pow((1 - t), 3) * resized_points[0][0] + 3* math.pow((1-t), 2) * t * 
            resized_points[1][0] + 3 * (1-t)*math.pow(t, 2) * resized_points[2][0] + math.pow(t, 3) * resized_points[3][0],

            math.pow((1 - t), 3) * resized_points[0][1] + 3* math.pow((1-t), 2) * t * 
            resized_points[1][1] + 3 * (1-t)*math.pow(t, 2) * resized_points[2][1] + math.pow(t, 3) * resized_points[3][1]
        )

    '''
    draws quadratic bezier curve
    takes 4 points
    '''
    def quadratic_bezier(self, points) -> None:
        curve = []
        t = 0
        while (t < 1):
            curve.append(self.bezier_func(t, points))
            t += self.curve_quality

        while (t > 0):          # draw for thickness
            bezier = self.bezier_func(t, points)
            curve.append((bezier[0] + self.style.get_thickness(), bezier[1] + math.pow(self.style.get_thickness(), math.cos(t))))
            t -= self.curve_quality

        self.canvas.polygon(curve, self.style.color)
    
    '''
    draws bezier curve from splines
    takes 3x+1 points, where x > 0
    '''
    def curve(self, curves: list) -> None:
        for curve in curves:                    # curves are sets of splines
            first_spline = self.curl(curve[:4])             # draws first full spline, example: [ [0, 0], [0, 0], [0, 0], [0, 0] ]
            self.quadratic_bezier(first_spline)
            last_point = first_spline[3]
            curve = curve[3:]                               # makes non-full spline (example: [ [0, 0], [0, 0], [0, 0] ]) to 
                                                            #               full spline by taking point from previous spline
            max_splines = len(curve) // 3
            for i in range(max_splines):
                spline = self.curl(curve[:4])
                spline[0] = last_point
                last_point = spline[-1]
                self.quadratic_bezier(spline)
                curve = curve[3:]

    '''
    curles the spline
    returns curled spline
    '''
    def curl(self, spline):
        curled_spline = []
        for i in range(0, 4):
            curled_spline.append([spline[i][0] + self.style.get_curl(), spline[i][1] + self.style.get_curl()])
        return curled_spline

    '''
    draws character
    '''
    def draw_char(self, char, no_margin = False) -> None:
        value = self.style.font[char]
        keys = value.keys()
        if "curl" in keys:
            self.style.local_curl = value["curl"]
        if "margin-up" in keys:
            self.local_offset[1] = value["margin-up"]
        if "depend-on" in keys:
            if "depend-offset" in keys:
                self.local_offset = value["depend-offset"]
            self.draw_char(value["depend-on"], no_margin=True)
        if "reduce" in keys:
            self.local_size = value["reduce"][1]
            self.curve(self.curve_from(value["reduce"][0]))
        if "curve" in keys:
            self.curve(value["curve"])
        if not no_margin and "width" in keys:
            self.offset_x += value["width"]
        self.local_offset = [0, 0]
        self.local_size = [1, 1]
        self.style.local_curl = 0

    def curve_from(self, char):
        return self.style.font[char]["curve"]
            

    '''
    draws string
    returns PIL Image
    '''
    def draw(self, string: str) -> Image:
        w = len(string) * self.style.get_size()
        h = self.style.get_size() + self.style.get_curl() + 40
        self.offset_x, self.offset_y = 0, 0

        self.im = Image.new("RGBA", (int(w), int(h)), color=(0,0,0,0))
        self.canvas = ImageDraw.Draw(self.im, "RGBA")
        #self.canvas.rectangle((0,0,w,h), (70, 0, 0, 60))

        for char in string:
            if char in self.style.font.keys():
                self.draw_char(char)

        self.im = self.im.filter(ImageFilter.SMOOTH_MORE)

        return self.im