import numpy as np
from PIL import Image

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]

tile1 = [ # 2x2 image of black-white checkerboard
    [black, white],
    [white, black],
]

tile2 = [ # 2x2 image of red-blue checkerboard
    [red, blue],
    [blue, red],
]

tiles = np.array([tile1, tile2], np.uint8)

# Generate 3x1 row of tiles, where its tile1 then tile2 then tile1
row = np.array([0, 1, 0])

arr = np.hstack(tiles[row])

# arr looks like this
# arr = np.array([
#     [black, white, red, blue, black, white],
#     [white, black, blue, red, white, black],
# ], np.uint8)

im = Image.fromarray(arr, 'RGB')

# Scale up by a factor of 100 so we can actually see it
im = im.resize((im.width * 100, im.height * 100), Image.NEAREST)

im.save('test.png')