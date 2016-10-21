# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
        help="path to the input image")
args = vars(ap.parse_args())
# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
im2, cnts, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    M = cv2.moments(c)
    epsilon = 0.1 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4:
        # Height
        if abs(30 - abs(approx[0][0][1] - approx[1][0][1])) < 5:
            # Width
            if abs(70 - abs(approx[0][0][0] - approx[2][0][0])) < 10:
                color = (0, 255, 0)
                print(abs(900 - approx[1][0][1]))
                if abs(900 - approx[1][0][1]) < 100:
                    color = (0, 0, 255)
                cv2.drawContours(image, [approx], 0, color, 3)

cv2.imshow('image', image)
cv2.waitKey(100000)
