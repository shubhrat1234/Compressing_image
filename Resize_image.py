from PIL import Image
import cv2
from skimage import io, transform
import mahotas
from pgmagick import Image
import time
from memory_profiler import profile


@profile
def resize_cv(file_path, count):
    image = cv2.imread(file_path)
    image = cv2.resize(image, (700, 700))
    print(image.shape)
    path = "/Users/shubhrat/Desktop/temp/cv1{}.jpg".format(count)
    cv2.imwrite(path, image)


@profile
def resize_skimage(file_path, count):
    image = io.imread(file_path)
    image = transform.resize(image, (700, 700))
    path = "/Users/shubhrat/Desktop/temp/skimage {}.jpg".format(count)
    io.imsave(path, image)


@profile
def resize_pillow(file_path):
    image = Image.open(file_path)
    image = image.resize((700, 700))
    path = "/Users/shubhrat/Downloads/crpd1.jpg"
    image.save(path)

@profile
def resize_mahotas(file_path, count):
    image = mahotas.imread(file_path)
    print(image.shape)
    image = mahotas.imresize(image, [700, 700, 3])
    print(image.shape)
    path = "/Users/shubhrat/Desktop/temp/mahotas {}.jpg".format(count)
    mahotas.imsave(path, image)


@profile
def resize_pgmagick(file_path, count):
    image = Image(file_path)
    image.resize('600x600')
    path = "/Users/shubhrat/Desktop/temp/pgmagick {}.jpg".format(count)
    image.write(path)


if __name__ == '__main__':
    count = 0
    while count < 10:
        start = time.time()
        resize_cv("/Users/shubhrat/Desktop/Images/pillow-{}.jpg".format(count))
        print(time.time()-start)
        count += 1






