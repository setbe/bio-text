# А Б В Г Ґ Д Е Є Ж З И І Ї Й К Л М 
#   Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ю Я

# а б в г ґ д е є ж з и і ї й к л м 
#   н о п р с т у ф х ц ч ш щ ь ю я

from PIL import Image, ImageDraw
from random import randint


LARGE_UPCASES = ['Б', 'Г', 'Ґ', 'Д', 'Ж', 'И', 
                 'Й', 'М', 'О', 'П', 'У', 'Ф', 
                 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ю']

class TextDraw():
    def __init__(self, image: Image, fontsize = 100, thickness = 1, random = [0, 0], curl = [2, 5], cursive = [4, 9]):
        self.fontsize = fontsize
        self.curl = curl
        self.cursive = cursive
        self.random = random
        self.thickness = thickness
        self.canvas = ImageDraw.Draw(image);
        self.ts = [t/float(self.fontsize) for t in range(self.fontsize+1)]
        self.points = []
    
    def make_bezier(self, xys):
        n = len(xys)
        combinations = self.pascal_row(n-1)
        def bezier(ts):
            result = []
            for t in ts:
                tpowers = (t**i for i in range(n))
                upowers = reversed([(1-t)**i for i in range(n)])
                coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
                result.append(
                    tuple(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
            return result
        return bezier
    
    def pascal_row(self, n, memo={}):
        if n in memo:
            return memo[n]
        result = [1]
        x, numerator = 1, n
        for denominator in range(1, n//2+1):
            x *= numerator
            x /= denominator
            result.append(x)
            numerator -= 1
        if n&1 == 0:
            result.extend(reversed(result[:-1]))
        else:
            result.extend(reversed(result))
        memo[n] = result
        return result

    def thickness_bezier(self, xyz):
        self.points = xyz
        xyz = self.norm_size([(xyz[0][0], xyz[0][1]), 
                              (xyz[1][0], xyz[1][1]), 
                              (xyz[2][0], xyz[2][1])])
        #self.points = self.curl_it(xyz)
        self.draw_points()

    def line(self):
        self.thickness_bezier([(50, 99), (56, 50), (58, 1)])
        self.thickness_bezier([(50, 99), (40, 95), (25, 90)])

    def draw(self, char: str):
        if char == 'І':
            self.line()
            self.thickness_bezier([(58, 1), (50, 18), (45, 20)])
        elif char == 'А':
            self.thickness_bezier([(50,1),(35,35),(20,97)])
            self.thickness_bezier([(35,50),(35,55),(65,42)])
            self.thickness_bezier([(50,1),(65,65),(80,97)])
        elif char == 'а':
            self.o()
            #self.thickness_bezier([(62,5),(63,20),(64,50)])
            #self.thickness_bezier([(64,50),(69,74),(99,99)])

    def draw_points(self):
        self.quality_once(4)
        self.ts = [t/float(self.fontsize) for t in range(self.fontsize+1)]
        c = 2
        while (c < len(self.points)):
            self.canvas.polygon([self.points[c-2], self.points[c-1], self.points[c]], fill="red")
            #self.canvas.polygon([self.points[c-5], self.points[c-4], self.points[c-3], self.points[c-2], self.points[c-1], self.points[c]], fill="red")
            c += 3
        self.points = []

    def norm_size(self, xyz: list):
        return [(xyz[0][0] * self.fontsize / 100, xyz[0][1] * self.fontsize / 100), 
                (xyz[1][0] * self.fontsize / 100, xyz[1][1] * self.fontsize / 100), 
                (xyz[2][0] * self.fontsize / 100, xyz[2][1] * self.fontsize / 100)]

    def curl_it(self, xyz: list):
        return [(xyz[0][0] - self.thickness, xyz[0][1] - self.thickness), 
                (self.thickness + xyz[1][0], self.thickness + xyz[1][1]), 
                (randint(self.curl[0], self.curl[1]) + xyz[2][0] - self.thickness, randint(self.curl[0], self.curl[1]) + xyz[2][1] - self.thickness)]

    def quality_once(self, value: int):
        if value > 0:
            points = []
            c = 2
            while (c < len(self.points)):
                points.append(self.points[c-2])
                points.append(((self.points[c-1][0] / 2 + self.points[c-2][0] / 2) / 2 + self.rand(), (self.points[c-1][1] / 2 + self.points[c-2][1] / 2) + self.rand()))
                points.append((self.points[c-1][0], self.points[c-1][1]))
                points.append((self.points[c-1][0], self.points[c-1][1]))
                #points.append((self.points[c-1][0] + self.rand(), self.points[c-1][1] + self.rand()))
                points.append(((self.points[c][0] / 2 + self.points[c-1][0] / 2) / 2 + self.rand(), (self.points[c][1] / 2 + self.points[c-1][1] / 2) + self.rand()))
                points.append((self.points[c][0], self.points[c][1]))
                c += 3
            self.points = points
            self.quality_once(value-1)
        #[(10, 10), (60,40), (100,90)]
        #[(10, 10), (30,20), (60,40), (60,40), (80,65), (100,90)]

    
    def o(self):
        self.thickness_bezier([(50,0),(0,50),(50,100)])
        #self.thickness_bezier([(50,0),(25,15),(0,50)])
        #self.thickness_bezier([(0,50),(25,80),(50,100)])

    def rand(self):
        return randint(self.random[0], self.random[1])

class Text():
    def __init__(self, canvas: TextDraw, text: str): # offset max 3 elements
        self.text = text;
        self.canvas = canvas

    def draw(self):
        pass