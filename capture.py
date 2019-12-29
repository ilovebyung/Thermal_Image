import cv2
import time

# first viceo device is 0
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # When 's' is pressed, save and quit
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # formatting date objects into file_name
        now = time.strftime("%Y_%m_%d-%H_%M_%S")
        file_name = now + '.png'
        # write to a file
        cv2.imwrite(file_name, frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
