import cv2 
def capture_image():
	key = cv2. waitKey(1)
	webcam = cv2.VideoCapture(0)
	while True:
    	try:
        	check, frame = webcam.read()
        	print(check) #prints true as long as the webcam is running
        	print(frame) #prints matrix values of each framecd 
        	cv2.imshow("Capturing", frame)
        	key = cv2.waitKey(1)
        	if key == ord('s'): 
            	cv2.imwrite(filename='saved_img.jpg', img=frame)
            	webcam.release()
            	img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            	img_new = cv2.imshow("Captured Image", img_new)
            	cv2.waitKey(1650)
            	cv2.destroyAllWindows()
            	print("Processing image...")
            	img_ = cv2.imread('captured/saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            	webcam.release()
            	print("Camera off.")
            	print("Program ended.")
            	cv2.destroyAllWindows()
            	break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break