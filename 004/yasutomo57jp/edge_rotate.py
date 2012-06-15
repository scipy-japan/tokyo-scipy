#!/usr/bin/env python

import Image
import ImageFilter

img = Image.open("lena.jpg")

eimg = img.filter(ImageFilter.FIND_EDGES)

rimg = eimg.rotate(45)

rimg.save("lena_edge_rotate.jpg")

