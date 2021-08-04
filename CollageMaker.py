import cv2
import numpy as np
import time

def temp1(images):
    images[0]=cv2.resize(images[0],(800,1200))
    images[1]=cv2.resize(images[1],(266,400))
    images[2]=cv2.resize(images[2],(266,400))
    images[3]=cv2.resize(images[3],(268,400))
    Horizontal1=np.hstack([images[0]])
    Horizontal2=np.hstack([images[1],images[2],images[3]])
    Vertical_attachment=np.vstack([Horizontal1,Horizontal2])
    filename='savedcollage1.jpg'
    cv2.imwrite(filename,Vertical_attachment)
    return

def temp2(images):
    start=time.time()
    images[0]=cv2.resize(images[0],(675,1200))
    images[1]=cv2.resize(images[1],(450,800))
    images[2]=cv2.resize(images[2],(225,400))
    images[3]=cv2.resize(images[3],(225,400))
    Horizontal1=np.hstack([images[2],images[3]])
    Vertical1=np.vstack([images[1],Horizontal1])
    Vertical_attachment=np.hstack([images[0],Vertical1])
    filename='savedcollage2.jpg'
    cv2.imwrite(filename,Vertical_attachment)
    end=time.time()
    print(f"Time in resizing is {end - start}")
    return

def temp3(images):
    images[0]=cv2.resize(images[0],(675,1200))
    images[1]=cv2.resize(images[1],(225,400))
    images[2]=cv2.resize(images[2],(225,400))
    images[3]=cv2.resize(images[3],(225,400))
    Vertical1=np.vstack([images[1],images[2],images[3]])
    Vertical_attachment=np.hstack([images[0],Vertical1])
    filename='savedcollage3.jpg'
    cv2.imwrite(filename,Vertical_attachment)
    return

def temp4(images):
    images[0]=cv2.resize(images[0],(280,500))
    images[1]=cv2.resize(images[1],(280,500))
    Vertical_attachment=np.hstack([images[0],images[1]])
    filename='savedcollage4.jpg'
    cv2.imwrite(filename,Vertical_attachment)
    return

def temp5(images):
    images[0]=cv2.resize(images[0],(170,250))
    images[1]=cv2.resize(images[1],(170,250))
    Vertical_attachment=np.vstack([images[0],images[1]])
    filename='savedcollage5.jpg'
    cv2.imwrite(filename,Vertical_attachment)
    return

def temp6(images):
    images[0]=cv2.resize(images[0],(600,900))
    images[1]=cv2.resize(images[1],(300,450))
    images[2]=cv2.resize(images[2],(300,450))
    Horizontal1=np.hstack([images[1],images[2]])
    Vertical_attachment=np.vstack([images[0],Horizontal1])
    filename='savedcollage6.jpg'
    cv2.imwrite(filename,Vertical_attachment)
    return

def temp7(images):
    images[0]=cv2.resize(images[0],(675,1200))
    images[1]=cv2.resize(images[1],(337,600))
    images[2]=cv2.resize(images[2],(337,600))
    Horizontal1=np.vstack([images[1],images[2]])
    Vertical_attachment=np.hstack([images[0],Horizontal1])
    filename='savedcollage7.jpg'
    cv2.imwrite(filename,Vertical_attachment)
    return







image1=cv2.imread("/Users/shubhrat/Downloads/i1.jpg")
image2=cv2.imread("/Users/shubhrat/Downloads/i2.jpg")
image3=cv2.imread("/Users/shubhrat/Downloads/i3.jpg")
image4=cv2.imread("/Users/shubhrat/Downloads/i4.jpg")
images=[]
images.append(image1)
images.append(image2)
#images.append(image3)
#images.append(image4)
x=len(images)
y=int(input("Enter a value :"))

if(x==4):
    y=y%3
    if(y==1):
        temp1(images)
    elif(y==2):
        temp2(images)
    else:
        temp3(images)
elif(x==3):
    y=y%2
    if(y==1):
        temp6(images)
    else:
        temp7(images)
else:
    y=y%2
    if(y==1):
        temp4(images)
    else:
        temp5(images)


