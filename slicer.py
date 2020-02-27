from PIL import Image
import os, sys
import math
from slicemap import slicemap

infile = 'pattern.png'
outpath = 'tiles'

def load_file( path ):
	img = Image.open(path)
	width, height = img.size
	return img

def slice_file(img=None):
	try:
		os.makedirs(outpath)
	except OSError:
		pass

	for k in slicemap.keys():
		print("creating tileset '" + k + "' ")
		for s in slicemap[k]:
			fname = os.path.join(outpath, "%s-%d-%d.png" % (k, s[0][0], s[0][1])) 
			print ("Creating tile:" + fname)

			slice_h = s[1][1] - s[0][1]
			slice_w = s[1][0] - s[0][0]

			buffer = Image.new("RGBA", [slice_w, slice_h], (255, 255, 255, 0))
			tile = img.crop((s[0][0], s[0][1], s[1][0], s[1][1]))
			buffer.paste(tile, (0, 0))
			buffer.save(fname, "PNG")

myimg = load_file('pattern.png')
slice_file(myimg)