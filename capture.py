import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(1)

while (True):
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # When 's' is pressed, save and quit
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # formatting date objects into file_name
        now = datetime.datetime.now()
        YYYYMMDDHHMM = now.strftime('%Y') + now.strftime('%m') + \
            now.strftime('%d') + now.strftime('%H') + now.strftime('%M')
        file_name = str(YYYYMMDDHHMM) + '.png'
        # write to a file
        cv2.imwrite(file_name, frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
