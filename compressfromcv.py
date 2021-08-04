from PIL import Image, ImageFont, ImageDraw
import math
from io import BytesIO
import sys
import time
limit=500000
def resize1(image,maxwidth,maxheight):
    start1=time.time()
    ratiogiven=float(maxwidth/maxheight)
    width, height = image.size
    print(width, height)
    print(1)
    ratio=float(width/height)
    if ratiogiven > ratio:
        newWidth=int(maxheight*ratio)
        image=image.resize((newWidth,maxheight))
    else:
        newHeight=int(maxwidth/ratio)
        image=image.resize((maxwidth,newHeight))
    end1=time.time()
    print(f"Time in resizing is {end1 - start1}")
    return image

def compressionbyquality(image,x,maxwidth,maxheight):
    quality=90
    while x > limit:
        out = BytesIO()
        image.save(out,quality=quality,format='JPEG')
        out.seek(0)
        image=Image.open(out)
        x=len(image.fp.read())
        quality-=10
        if quality < 80:
            break
    image=resize1(image,maxwidth,maxheight)
    image.save("/Users/shubhrat/Downloads/Finaloutput.jpg")
    return


def convertTojpeg(image):
    if image.format!='JPEG':
        out=BytesIO()
        image.save(out, format='JPEG')
        out.seek(0)
        image = Image.open(out)
        return image

    else:
        return image

def compress(path, maxwidth, maxheight):
    image=Image.open(path)
    imag1=resize1(image,maxwidth,maxheight)
    imag1.save("/Users/shubhrat/Downloads/Bypillowi2.jpg")
    im=convertTojpeg(image)
    sizeOfImage=len(im.fp.read())
    #print(si)
    if limit > sizeOfImage:
        image=resize1(image,maxwidth,maxheight)
        image.save(("/Users/shubhrat/Downloads/Finaloutput.jpg"))
    else:
        compressionbyquality(image,sizeOfImage,maxwidth,maxheight)






if __name__ == '__main__':
    start=time.time()
    path="/Users/shubhrat/Downloads/i2.jpg"
    maxwidth=1200
    maxheight=1200
    compress(path, maxwidth, maxheight)
    end=time.time()
    print(f"Total Time is {end - start}")
