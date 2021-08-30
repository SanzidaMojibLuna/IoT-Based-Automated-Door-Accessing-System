import face_recognition
import imutils
import pickle
import time
import cv2
import os
 
def process_image():
	cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
	faceCascade = cv2.CascadeClassifier(cascPathface)
	data = pickle.loads(open('face_enc', "rb").read())
	image = cv2.imread('captured/saved_img.jpg')
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(60, 60),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
	cv2.imshow("Frame", image)
	cv2.waitKey(0)
 
	encodings = face_recognition.face_encodings(rgb)
	names = []
	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],encoding)
		name = "Unknown"
		if True in matches:
			name = data["names"]
            		counts[name] = counts.get(name, 0) + 1
            		name = max(counts, key=counts.get)
 
		names.append(name)
		break
	return names
