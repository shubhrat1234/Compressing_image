from PIL import Image, ImageFont, ImageDraw
import math
from io import BytesIO
import sys
import time
import io

def resize_to_maxsize(image, maxwidth: int, maxheight: int):
    ratiogiven = float(maxwidth / maxheight)
    width, height = image.size
    ratio = float(width / height)
    if ratiogiven > ratio:
        width = min(int(maxheight * ratio),width)
        height=min(height,maxheight)
    else:
        height = min(int(maxwidth / ratio),height)
        width=min(width,maxwidth)
    image = image.resize((width, height))
    out = io.BytesIO()
    image.save(out, format='JPEG')
    out.seek(0)
    image = Image.open(out)
    return image


def compressionbyquality(image, x):
    quality = 90
    limit = 500000
    while x > limit:
        out = io.BytesIO()
        image.save(out, quality=quality, format='JPEG')
        out.seek(0)
        image = Image.open(out)
        x = len(image.fp.read())
        quality -= 10
        if quality < 70:
            break
    image.save("/Users/shubhrat/Downloads/Finaloutput3.jpg")
    return


def convertTojpeg(image):
    if image.format != 'JPEG':
        out = io.BytesIO()
        image.save(out, format='JPEG')
        out.seek(0)
        image = Image.open(out)
        return image
    else:
        return image


def compress(path, maxwidth, maxheight):
    image = Image.open(path)
    limit=500000
    image = convertTojpeg(image)
    size_of_image = len(image.fp.read())
    image = resize_to_maxsize(image, maxwidth, maxheight)
    size_of_image = len(image.fp.read())
    if limit > size_of_image:
        image.save(("/Users/shubhrat/Downloads/Finaloutput3.jpg"))
    else:
        compressionbyquality(image, size_of_image)


if __name__ == '__main__':
    start=time.time()
    path="/Users/shubhrat/Downloads/i8.jpg"
    maxwidth=2000
    maxheight=2000
    compress(path, maxwidth, maxheight)
    end=time.time()
    print(f"Total Time is {end - start}")
