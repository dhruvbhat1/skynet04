import cv2
import numpy as np

#The image of our car

img_file = 'Car Image.jpg'


video = cv2.VideoCapture(0)


# pretrained car classifier

car_tracker_file = 'car_detector.xml'
pedestrian_tracker_file = 'pedestrian.xml'
cat_tracker_file = 'cat.xml'
traffic_tracker_file = 'traffic.xml'
stop_tracker_file = 'stop.xml'
bump_tracker_file = 'bumper.xml'
bus_tracker_file = 'bus.xml'
bike_tracker_file = 'bike.xml'





car_tracker = cv2.CascadeClassifier(car_tracker_file)

pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

cat_tracker = cv2.CascadeClassifier(cat_tracker_file)

traffic_tracker = cv2.CascadeClassifier(traffic_tracker_file)
stop_tracker = cv2.CascadeClassifier(stop_tracker_file)
bump_tracker = cv2.CascadeClassifier(bump_tracker_file)
bus_tracker = cv2.CascadeClassifier(bus_tracker_file)
bike_tracker = cv2.CascadeClassifier(bike_tracker_file)



while True:
    (read_successful, frame) = video.read()

    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    ped = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    cats = cat_tracker.detectMultiScale(grayscaled_frame)
    traffics = traffic_tracker.detectMultiScale(grayscaled_frame)
    stops = stop_tracker.detectMultiScale(grayscaled_frame)
    bumps = bump_tracker.detectMultiScale(grayscaled_frame)
    buss = bus_tracker.detectMultiScale(grayscaled_frame)
    bikes = bike_tracker.detectMultiScale(grayscaled_frame)
  
  

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(frame, 'Cars', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    for (x, y, w, h) in ped:
        cv2.rectangle(frame, (x+2,y+2), (x+w, y+h), (255, 0, 0), 2)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, '!!PEPOLE!!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    
    for (x, y, w, h) in cats:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 0), 2)
        cv2.putText(frame, '!!Animal!!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

    for (x, y, w, h) in traffics:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (247, 61, 253), 2)
        cv2.putText(frame, 'Signal', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (247, 61, 253), 2)

    for (x, y, w, h) in stops:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (61, 73, 253), 2)
        cv2.rectangle(frame, (x+2,y+2), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, '!STOP!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (61, 73, 253), 2)
    
    for (x, y, w, h) in bumps:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (150, 78, 223), 2)
        cv2.putText(frame, '!Bumper Ahead!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (150, 78, 223), 2)

    for (x, y, w, h) in bikes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (169, 162, 177), 2)
        
        cv2.putText(frame, '*bikes*', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (169, 162, 177), 2)

    for (x, y, w, h) in buss:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        
        cv2.putText(frame, '*Bus*', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)


    cv2.imshow('skynet camera',frame)

    #wait here in the code and listen for a key press
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

video.release()

"""
# create open cv image

img = cv2.imread(img_file)


#chnage to black and white
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car_tracker = cv2.CascadeClassifier(classifier_file)

cars = car_tracker.detectMultiScale(black_n_white)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)



cv2.imshow('skynet camera', img)

#wait here in the code and listen for a key press
cv2.waitKey()

"""
