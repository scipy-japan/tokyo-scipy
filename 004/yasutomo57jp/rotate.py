#!/usr/bin/env python

import Image
import ImageFilter

img = Image.open("lena.jpg")

rimg = img.rotate(45)

rimg.save("lena_rotate.jpg")

img.show()
rimg.show()
