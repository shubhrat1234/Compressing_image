from PIL import Image, ImageFont, ImageDraw
import time
path="/Users/shubhrat/Downloads/i1.jpg"
image=Image.open(path)
print(image.size)
count=0
avgTime=0
while count < 1000:
    image=Image.open("/Users/shubhrat/Downloads/i1.jpg")
    start=time.time()
    image=image.resize((400,400))
    end=time.time()
    print(f"Total Time is {end - start}")
    count+=1
    avgTime=float((avgTime+(end-start))/2)


print(f"Average Time is {avgTime}")
image.save("/Users/shubhrat/Downloads/ByPillow.jpg")
image=Image.open("/Users/shubhrat/Downloads/ByPillow.jpg")
print(image.size)


