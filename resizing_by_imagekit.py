from imagekitio import ImageKit
from memory_profiler import profile
import time

start = time.time()
imagekit = ImageKit(
    private_key='private_5cPShZTsDj******************',
    public_key='public_OA0FI7PdSHP5m2dtlGI2iQZdBPw=',
    url_endpoint='https://ik.imagekit.io/shubhrat123'
)

image_url = imagekit.url({
    "src": "https://ik.imagekit.io/shubhrat123/girl.jpg",
    "transformation": [{
        "height": "300",
        "width": "400"
    }],
    "signed": True,
    "expire_seconds": 5
})
print("Total time is: {}".format(time.time() - start))
