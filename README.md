# skynet04

**This is opencv based people and car detection system** 

This has been used in autopilot cars.

Here i have used the images of car and pedestrian in form of xml file which reads the co-ordinates of the object creates a square around it.

I first learnt open cv and python and tried the syntax which i used in face recognition system

**Instruction**

Download all the files in single folder in your studio (Here i have used Visual Code 2019)

S1:Open the skycam.py in visual studio code

S2:Using your inbuilt terminal in studio or CMD run command **python skycam.py**

S3:Allow access to camera

S4:Run the command

S5:Here i have shown video using my phone 

S6:The pedestrian are showns using red and blue rectangle,while the cars are shown using yellow rectangle,you can use another dataset of potholes and show it in different color.

S7:This system is not 100% accurate but it work faster according to my calculations.

![My Testing images](\latest\components\b1.png)


Haar feature
Haar-like  features  were  proposed  by  Viola  and Jones [7]  as  an  alternative  method  for  face detection. The  general  idea  was  to  describe  an  object  as  a cascade  of  simple  feature  classifiers  organized  into several stages. This  is a very fast method, performing face detection as effectively as any other methods. As stated in [7], in the  CMU+MIT reference test  set,  the method  performed  15  times  faster  than  the  Baluja-Kanade  detector  and  about 600  times  faster  than  the Schneiderman-Kanade detector. The classification of images is based on the value of simple  basic  features.  Features  are  used  instead  of simple raw pixel values generally because they can act to encode  ad-hoc  domain  knowledge  but  also,  in  this particular  case,  because  they  are  much  faster  to process. 

![Haar Features](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQAX7WHLxJXYqJaTma5tg75wYZay0G--Z7xMw&usqp=CAU)

Feature of car
An intelligent traffic surveillance system, equipped with electronic devices, works by communicating with moving vehicles about traffic conditions, monitor rules and regulations and avoid collision between cars. Therefore the first step in this process is the detection of cars. The system uses Haar like features for vehicle detection, which is generally used for face detection. Haar feature-based cascade classifiers are an effective object detection method first proposed by Viola and Jones. It's a machine learning based technique which uses a set of positive and negative images for training purpose. Results show this method is quite fast and effective in detecting cars in real time CCTV footages.

![of a car](https://www.researchgate.net/publication/315137877/figure/fig2/AS:614297159872520@1523471264588/Haar-like-features-Top-row-basic-forms-of-Haar-like-features-Bottom-row-vehicle-rear.png)

