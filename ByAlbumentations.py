import cv2
from PIL import Image
import threading

import requests

garbage = []


def make_request(i: int):
    h = str(i * 2 + 500)
    requests.get(
        "http://192.168.0.112:5002/media/v1/load/company/45b47d82-beb2-4b08-9d31-3dbf63ea9e55/catalog/070bc164-1526-4999-9630-2714ad174ba8.jpg?h={}".format(
            h))


#
#
# @profile()
def crop_image(file_path):
    image = cv2.imread(file_path)
    width, height = image.shape[0], image.shape[1]
    print(width, height)
    image1 = image[0:int(width/2), 0:int(height/2)]
    cv2.imwrite("/Users/shubhrat/Downloads/cropped1.jpg", image1)
#     # im = Image.open(file_path)


if __name__ == '__main__':
    crop_image("/Users/shubhrat/Downloads/i1.jpg")
