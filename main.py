from biotext import TextDraw
from PIL import Image, ImageDraw

width, height = 200, 200
im = Image.new('RGBA', (width, height), (0, 0, 0, 0)) 

draw = TextDraw(im)
draw.draw('а')

im = im.resize((width // 2, height // 2), resample=Image.Resampling.ANTIALIAS)
im.show()