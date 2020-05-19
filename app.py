# import cv2

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == ord('q'): # exit on ESC
#         break

# vc.release()
# cv2.destroyWindow("preview")


############################################


# import cv2, time

# video=cv2.VideoCapture(0)
# a=0

# while True:
#     a=a+1

#     check, frame = video.read()

#     print(check)
#     print(frame)

#     gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow("Capturing",gray)

#     # cv2.waitKey(0)
#     key=cv2.waitKey(1)

#     if key == ord('q'):
#         break

# print(a)

# video.release()
# cv2.destroyWindow()


##########################################


# import cv2
# import numpy as np

# video = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

# while True:
#     rval, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     out.write(frame)

#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# video.release()
# out.release()
# cv2.destroyAllWindows()


#############################################

# import cv2
# import numpy as np

# video = cv2.VideoCapture(0)
# # fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))
# a = 0

# while True:
#     rval, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)

#     keycap = cv2.waitKey(1)
#     if keycap == ord('c'):
#         fourcc = cv2.VideoWriter_fourcc(*'XVID')
#         out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
#         out.write(frame)

#     keyquit = cv2.waitKey(1)
#     if keyquit == ord('q'):
#         break

# video.release()
# out.release()
# cv2.destroyAllWindows()

#####################################

# import cv2
# import numpy as np

# video = cv2.VideoCapture(0)
# # fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

# while True:
#     rval, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # out.write(frame)

#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)

#     k = cv2.waitKey(1)
#     if k == 27:         # wait for ESC key to exit
#         video.release()
#         cv2.destroyAllWindows()
#     elif k == ord('s'): # wait for 's' key to save and exit
#         cv2.imwrite('messigray.png',frame)

# video.release()
# out.release()
# cv2.destroyAllWindows()

#############################################

import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)

while True:
    rval, frame = video.read()
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:         # wait for ESC key to exit
        video.release()
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        tm = time.strftime('%d-%b-%Y-%H-%M-%S')
        name ="C:/Users/Atif Jabbar/Desktop/Laptop Camera/" + tm + '.png'
        # print(name)
        cv2.imwrite(name,frame)