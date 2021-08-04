from imagekitio import ImageKit
import urllib.request
from PIL import Image
import time
start=time.time()
imagekit = ImageKit(
    private_key='your private_key',
    public_key='your public_key',
    url_endpoint = 'your url_endpoint'
)
#https://ik.imagekit.io/shubhrat123/girl.jpeg
imagekit_url = imagekit.url({
    "path": "girl.jpeg",
    "url_endpoint": "https://ik.imagekit.io/shubhrat123/",
    "transformation": [{"height": "800", "width": "1200", "quality": "95", "aspect_ratio": "1.5", "focus": "auto"}],
}
)

print(imagekit_url)
end=time.time()
urllib.request.urlretrieve(
    imagekit_url,
    "/Users/shubhrat/Downloads/output1.jpg")

im1 = Image.open("/Users/shubhrat/Downloads/output1.jpg")
print(im1.size)

print(f"Runtime of the program is {end - start}")
