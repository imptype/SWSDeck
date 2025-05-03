import io
import string
import numpy as np
from PIL import Image
from starlette.applications import Starlette
from starlette.responses import Response, FileResponse

default = '-'
w, h = 139, 166
sheet = Image.open('assets/cards.png')
chars = list(string.digits + string.ascii_lowercase + string.ascii_uppercase + default)

icons = np.array([
  sheet.crop((x, y, x + w, y + h))
  for y in range(0, sheet.height, h)
  for x in range(0, sheet.width, w)
])

app = Starlette()

@app.route('/')
async def root(request):
  if request.query_params:

    row = np.sort(np.array([
      chars.index(char)
      if char in chars else len(chars) - 1 
      for char in str(request.query_params)[:8].ljust(8, default)
    ]))

    im = Image.fromarray(np.hstack(icons[row]), 'RGB')
    
    buffer = io.BytesIO()
    im.save(buffer, 'PNG')
    return Response(buffer.getvalue(), media_type = 'image/png')
  else:
    return FileResponse('assets/cardsinfo.png')