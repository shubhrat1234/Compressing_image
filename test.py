import time
from memory_profiler import profile
from PIL import Image
from flask import Flask, request
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=100)
app = Flask(__name__)
count = 0
active_threads = 0


@profile
def resize(file_path):
    image = Image.open(file_path)
    image = image.resize((700, 700))
    path = "/Users/shubhrat/Downloads/crpd.jpg"
    image.save(path)
    image.close()


@app.route("/resize")
def resize_image():
    number_of_threads = int(request.args['threads'])
    file_remote_path = request.args['path']
    for i in range(1, number_of_threads):
        executor.submit(resize, file_remote_path)
        print('pending:', executor._work_queue.qsize(), 'jobs')
        print('threads:', len(executor._threads))
    print(active_threads)
    print(count)
    return "Hello"


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5002, debug=True)
    count=0
    start = time.time()
    file_path = "/Users/shubhrat/Downloads/compi2-30.jpg"
    resize(file_path)
    print(time.time()-start)