from PIL import Image, ImageDraw, ImageFilter
import math
from style import TextStyle

def ave(p1: tuple, p2: tuple):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
class TextDraw():
    def __init__(self, style: TextStyle):
        self.im = None
        self.canvas = None
        self.last_pos = []
        self.x_margin, self.y_margin = 0, 0
        if style:
            self.style = style
        else:
            self.style = TextStyle()

    def func(self, cords: list, t):
        new_cords = []
        for cord in cords:
            new_cords.append(((cord[0] * self.style.get_size()) / 100 + self.x_margin, (cord[1] * self.style.get_size()) / 100))

        cords = new_cords
        return (
            math.pow((1 - t), 3) * cords[0][0] + 3* math.pow((1-t), 2) * t * cords[1][0] + 3 * (1-t)*math.pow(t, 2) * cords[2][0] + math.pow(t, 3) * cords[3][0],
            math.pow((1 - t), 3) * cords[0][1] + 3* math.pow((1-t), 2) * t * cords[1][1] + 3 * (1-t)*math.pow(t, 2) * cords[2][1] + math.pow(t, 3) * cords[3][1]
        )
    
    def bezier(self, cords: list):
        for cord in cords:
            curve = []
            t = 0
            while (t < 1):
                curve.append(self.func(cord, t))
                t += 0.01

            while (t > 0):
                bezier = self.func(cord, t)
                curve.append((bezier[0] + self.style.get_thickness(), bezier[1] + math.pow(self.style.get_thickness(), math.cos(t))))
                t -= 0.01

            self.last_pos = [curve[-1][0], curve[-1][1]]
            self.canvas.polygon(curve, self.style.color)

    def divide_func(self, xy0, xym, xy: tuple, xy2: tuple):
        return (ave(xy0, xym, xy[0], xy[1]), ave(xy0, xym, xy2[0], xy2[1]))

    def divide(self, cords: list, local_margin: list, divide = 0):
        for i in cords:
            for j in i:
                print(local_margin)
                j[0] += local_margin[0]
                j[1] += local_margin[1]

        new_cords = []
        if divide > 0:
            for cord in cords:
                cords_list = []
                cords_list.append((cord[0][0]+self.style.get_curl(), cord[0][1]+self.style.get_curl()))
                cords_list.append(ave(cord[0], cord[1]))
                cords_list.append((cord[1][0]+self.style.get_curl(), cord[1][1]+self.style.get_curl()))
                cords_list.append(ave(cord[1], cord[2]))
                new_cords.append(cords_list)

                cords_list = []
                cords_list.append(ave(cord[1], cord[2]))
                cords_list.append((cord[2][0]+self.style.get_curl(), cord[2][1]+self.style.get_curl()))
                cords_list.append(ave(cord[2], cord[3]))
                cords_list.append((cord[3][0]+self.style.get_curl(), cord[3][1]+self.style.get_curl()))
                new_cords.append(cords_list)
                
            return self.divide(new_cords, divide-1)
        return cords

    def curve(self, cords: list, local_margin, divide = 0):
        self.bezier(self.divide(cords, local_margin, divide))

    def curve0(self, cords, divide):
        new_cords = []
        if divide > 0:
            for cord in cords:
                cords_list = []
                cords_list.append((cord[0][0]+self.style.get_curl(), cord[0][1]+self.style.get_curl()))
                cords_list.append(ave(cord[0], cord[1]))
                cords_list.append((cord[1][0]+self.style.get_curl(), cord[1][1]+self.style.get_curl()))
                cords_list.append(ave(cord[1], cord[2]))
                new_cords.append(cords_list)

                cords_list = []
                cords_list.append(ave(cord[1], cord[2]))
                cords_list.append((cord[2][0]+self.style.get_curl(), cord[2][1]+self.style.get_curl()))
                cords_list.append(ave(cord[2], cord[3]))
                cords_list.append((cord[3][0]+self.style.get_curl(), cord[3][1]+self.style.get_curl()))
                new_cords.append(cords_list)

    def continue_(self, cords: list, divide = 0):
        cords[0][0] = (self.last_pos[0] - self.x_margin, self.last_pos[1])
        self.curve(cords, divide)

    def draw_char(self, char, resize = 0, local_margin = [0, 0], divide = 0):
        keys = self.style.font[char].keys()
        self.style.fontsize += resize
        if "margin" in keys:
            local_margin = self.style.font[char]["margin"]
            print("local: ", local_margin)
        if "reduce" in keys:
            self.draw_char(self.style.font[char]["reduce"][0], self.style.font[char]["reduce"][1])
        elif "depend" in keys:
            self.draw_char(self.style.font[char]["depend"])
        if "right" in keys:
            self.x_margin += self.style.font[char]["right"]
        if "left" in keys:
            self.x_margin += self.style.font[char]["left"]
        if "curve" in keys:
            self.curve(self.style.font[char]["curve"], local_margin, divide = divide)
        self.style.fontsize -= resize

    def draw(self, string: str, divide: int = 0, is_export = False):
        w = len(string) * self.style.get_size()
        h = self.style.get_size() + self.style.get_curl()
        self.x_margin, self.y_margin = 0, 0

        self.im = Image.new("RGBA", (int(w), int(h)), color=(0,0,0,0))
        self.canvas = ImageDraw.Draw(self.im, "RGBA")
        #self.canvas.rectangle((0,0,w,h), (70, 0, 0, 60))

        for char in string:
            if char in self.style.font.keys():
                self.draw_char(char, divide = divide)
                self.x_margin += self.style.get_size() / 2

        if is_export:
            blur = self.im.filter(ImageFilter.GaussianBlur(2))
            print("export")
            self.im.paste(blur)
            self.im = self.im.resize((int(w // 2), int(h // 2)), Image.BICUBIC)
        else:
            self.im = self.im.filter(ImageFilter.SMOOTH_MORE)

        return self.im