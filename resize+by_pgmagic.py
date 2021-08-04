import time

from pgmagick import Image, DrawableCircle, DrawableText
from pgmagick import  Geometry, Color
from memory_profiler import profile
# draw the image of dimension 600 * 600
# @profile()
def resize_by_pgmagick(file_path):
    start = time.time()
    img = Image(file_path)
    img.resize('600x600')
    # invoke write function along with filename
    img.write("/Users/shubhrat/Downloads/conv1.jpg")
    print("Total time is: {}".format(time.time()-start))


if __name__ == '__main__':
    count=0
    while count < 10:
        resize_by_pgmagick("/Users/shubhrat/Desktop/Images/pillow-{}.jpg".format(count))
        count += 1
