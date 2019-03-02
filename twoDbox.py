

import matplotlib.pyplot as pyplot
import matplotlib.patches as patches
import numpy as np
from PIL import Image
import sys

w = 450
h = 100

def boxDraw(argv):	

	imageFile = argv
	img = np.array(Image.open(imageFile),dtype=np.uint8)

	fig,ax = pyplot.subplots(1)

	ax.imshow(img)

	rectangle = patches.Rectangle((0.09193398058414459 + w, 0.5268091559410095 + h),150,h,linewidth=1,edgecolor='r',facecolor='none')

	ax.add_patch(rectangle)

	pyplot.show()


boxDraw(sys.argv[1])

