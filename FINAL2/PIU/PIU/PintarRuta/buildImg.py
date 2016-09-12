import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


img = Image.open('sample.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 32)

# Pintamos la Fecha y Hora
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
horafecha = time.strftime("   %d/%m/%Y                                          %H:%M")
draw.text((0, 0),horafecha,font=font)
draw.line((0,25, 320,25), fill=(255,255,255))

# Pintamos la tabla
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 32)
i = 30
with open('tablaBus.txt') as f:
	for line in f:
		draw.text((0, i),line,font=font)
		i = i + 30

if (i==0):
	print 'El fichero de rutas esta vacio.'
else:
	img.save('out.bmp')



