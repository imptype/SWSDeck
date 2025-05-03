import os
import string
from PIL import Image, ImageDraw, ImageFont

folder = 'screenshots'
x, y, w, h = 108, 145, 1112, 166

im = Image.new('RGB', (w, h * len(os.listdir(folder))))
for i, filename in enumerate(sorted(os.listdir(folder))):
    screenshot = Image.open(f'{folder}/{filename}')
    rect = screenshot.crop((x, y, x + w, y + h))
    im.paste(rect, (0, i * h))

im.save('assets/cards.png')

w = 139
default = '-'
chars = list(reversed(string.digits + string.ascii_lowercase + string.ascii_uppercase + default))
overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
font_path = 'assets/Arial-Unicode-MS.ttf'
font = ImageFont.truetype(font_path, 72)

height = sum(font.getmetrics())

for oy in range(im.height // h):
  for ox in range(im.width // w):
    char = chars and chars.pop() or default
    x0, y0, x1, y1 = font.getbbox(char)
    px = ox * w + (w - (x1 - x0)) // 2
    py = oy * h + (h - height) // 2
    draw.text((px, py), char, (255, 0, 0, int(255 * 0.8)), font)

font = ImageFont.truetype(font_path, 15)
draw.text((0, im.height - sum(font.getmetrics())), 'https://github.com/imptype/SWSDeck', (0, 0, 0, int(255 * 0.5)), font)

im = Image.alpha_composite(im.convert('RGBA'), overlay)
im.save('assets/cardsinfo.png')