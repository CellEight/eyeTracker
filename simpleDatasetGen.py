from random import shuffle
import cv2

camera = cv2.VideoCapture(0)

cv2.namedWindow("test")

quadrants = [0,1,2,3]*25
shuffle(quadrants)
count = [0,0,0,0]

for i, quad in enumerate(quadrants):
    input(f"{i}/100 - Please look at quadrent {quad} and press enter.")
    _, im = camera.read()
    cv2.imwrite(f'./simple/{quad}/{count[quad]}.jpg', im)
    cv2.imshow("test", im)
    count[quad] += 1
camera.release()

print("All done! Thanks :)")
