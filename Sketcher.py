import numpy as np
from PIL import Image


IMAGE_SORCE = Image.open("photo.jpg")


def getdiff(im1, x, y):
    l1 = np.array(im1.getpixel((x, y)))
    l2 = np.array(im1.getpixel((x, y+1)))
    result = np.abs(np.subtract(l1, l2))
    diff = np.sum(result)
    per_diff = (diff / np.sum(l1)) * 100
    return per_diff


def makeskrtch(im1):
    array = []
    for i in range(im1.size[1]-1):
        for j in range(im1.size[0]):
            per_diff = getdiff(im1, j, i)
            if per_diff > 15:
                array.append((0, 0, 0))
            elif per_diff > 10:
                array.append((169, 169, 169))
            elif per_diff > 5:
                array.append((192, 192, 192))
            elif per_diff > 1:
                array.append((211, 211, 211))
            else:
                array.append((255, 255, 255))
    return array


output = makeskrtch(IMAGE_SORCE)
im2 = Image.new(IMAGE_SORCE.mode, IMAGE_SORCE.size)
im2.putdata(output)
im2.save("result.png")
im2.show()