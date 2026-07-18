import cv2
import os
detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cv2.namedWindow("Face Detection system",cv2.WINDOW_NORMAL)
cam=cv2.VideoCapture(0)
while True:
    rect,frame=cam.read()
    face=detector.detectMultiScale(frame,1.2)
    print(len(face))
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,100),3)
    cv2.imshow("Face Detection system",frame)
    if cv2.waitKey(4)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

# Detect Face
def face_detect(frame):
    detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    faces=detector.detectMultiScale(frame,1.2)
    return faces

# Gray Scale
def gray_scale(image):
    cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Cut Face
def cut_face(image,face):
    cut_faces = []
    for (x,y,w,h) in face_coord:
        face = image[y:y+h,x:x+w]
        cut_faces.append(face)
    return cut_faces

#Resize
def resize(image,scale = (80,100)):
    resized_images =[]
    for face in image:
        resized_face = cv2.resize(image, size)
        resized_images.append(img)
    return resized_images

# Normalize Intensity
def normalize_intensity(image):
    normalized_faces = []
    for face in image:
        normalized_faces.append(cv2.equalizeHist(img))
    return normalized_faces  

# Image Plot
import matplotlib.pyplot as plt
def plot(image,title=''):
    plt.figure(figsize=(10,10))
    if image.shape == 3:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.imshow(image, c= 'gray')
    plt.title()
    plt.axis('off')
    plt.show()

# Pipeline
def pipeline(image, face_coord):
    faces = cut_face(image,face_coord)
    faces = resize(faces)
    faces = normalize_intensity(faces)
    return faces

# Draw Rectangle
def draw_rectangle(frame,coords):
    for (x,y,w,h) in coords:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,100),2)
    return frame

# Let's Create our own dataset
name = input("Enter your name: ")
no_Samples = int(input("Enter number of samples: "))
folder = "DataSet/"+name.lower()
if os.path.exists(folder):
    print("Folder already exists")
else:
    os.mkdir(folder)
    start_cap = False
    sample = 1

    cam = cv2.VideoCapture(0)
    while True:
        rect,frame = cam.read()
        gray = gray_scale(frame)
        coords = face_detect(frame)
        if len(coords) > 0:
            faces = pipeline(gray, coords)
            image_name = folder+"/" + str(sample) + ".jpg"
            cv2.imread(img, image_name,0)

        else:
            print("No face Found!")
