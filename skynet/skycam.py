import cv2

#The image of our car

img_file = 'Car Image.jpg'


video = cv2.VideoCapture(0)


# pretrained car classifier

car_tracker_file = 'car_detector.xml'
pedestrian_tracker_file = 'pedestrian.xml'




car_tracker = cv2.CascadeClassifier(car_tracker_file)

pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)




while True:
    (read_successful, frame) = video.read()

    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    ped = pedestrian_tracker.detectMultiScale(grayscaled_frame)
  
  

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)

    for (x, y, w, h) in ped:
        cv2.rectangle(frame, (x+2,y+2), (x+w, y+h), (255, 0, 0), 2)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        
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
