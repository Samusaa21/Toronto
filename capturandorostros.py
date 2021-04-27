import cv2
import os
import imutils

personName = 'Samuel'
dataPath = 'C:/Users/jpaon/OneDrive/Escritorio/Reconocimiento Facial/Data'
personPath = dataPath + '/' + personName
#print(personPath)
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)

cap = cv2.VideoCapture('Samuel.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0
    

    
     
    
        


    
        


