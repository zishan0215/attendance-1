import numpy as np
import cv2
import time
import glob
import os


def rmfaces():
    for i in glob.glob('../extras/download/*/face/*.jpg'):
        print i
        os.remove(i)


def one_hot_names():
    lst = []
    with open("../traintest/lfwpeople.txt",'r') as f:
        for line in f:
            lst += [line.split(',')[1]]
    print one_hot(",".join(lst), 5749, split=",")[:10]
    print lst[:10]


def preprocess():
    
    with open("../traintest/classtrain.txt",'w') as f:
        for image in glob.glob("newtest/*/*.jpg"):
            print image.split('/')[2].split('.')[0]+","+image.split('/')[1]
            f.write(image.split('/')[2].split('.')[0]+","+image.split('/')[1]+'\n')


def encode():
    lst = []
    l1 = []
    with open("../traintest/classtrain.txt",'r') as f:
        for i in f:
            if i.split(',')[1].split('\n')[0] not in l1:
                l1.append(i.split(',')[1].split('\n')[0])
            lst.append([i.split(',')[1].split('\n')[0], i.split(',')[0]])

    print l1

    with open("train.txt",'w') as f:
        for i in lst:
            print str(i[1])+","+str(l1.index(i[0]))
            f.write(i[1]+","+str(l1.index(i[0]))+'\n')
            

def image():
    # Load an color image in grayscale

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # print img.shape
    for image in glob.glob("../extras/faceScrub/download/*/*.jpg"):
        start = time.time()
        img = cv2.imread(image)
        # res = cv2.resize(img, (227, 227), interpolation=cv2.INTER_CUBIC)

        FACE_DETECTOR_PATH = "../extras/haarcascade_frontalface_default.xml"

        detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
        rects = detector.detectMultiScale(img, scaleFactor=1.4, minNeighbors=1,
                                          minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # construct a list of bounding boxes from the detection
        # rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]

        # update the data dictionary with the faces detected
        # data.update({"num_faces": len(rects), "faces": rects, "success": True})

        print "time", time.time() - start
        for (x, y, w, h) in rects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = img[y:y + h, x:x + w]
            cv2.imshow('image', roi_color)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def video():
    FACE_DETECTOR_PATH = "../extras/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)

    video_capture = cv2.VideoCapture('rtsp://admin:admin12345@192.168.1.64:554/Output.h264')

    i = 601
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        image = frame

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=1,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        start = time.time()
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img = image[y:y + h, x:x + w]

        # if time.time()-start >= 20:  
        # print "Taken image", i
        # cv2.imwrite('newtest/%s.jpg' % i , img)
        
        # if i%20==0 and i!=0:
        #     # i=0
        #     # i+=1
        #     time.sleep(10)
        #     start = time.time()
        #     # break
        # i+=1
        # time.sleep(20)
        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    rmfaces()