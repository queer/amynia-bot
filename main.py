import os
import imutils
import cv2

cap = cv2.VideoCapture()
cap.open('udp://127.0.0.1:1234/')
if not cap.open:
    print("Not open")
print('Waiting on video...')
while True:
    # widthxheight+x+y
    # 322x1078+793+0
    err,img = cap.read()
    #if err:
        #print(err)
    if img.shape != (0,0):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
                        ypos = abs(approx[1][0][1])
                        if ypos > 840 and ypos < 860:
                            xpos = abs(approx[0][0][0])
                            # D~10 F~80 J~160 K~240
                            key = 'UNKNOWN'
                            if abs(10 - xpos) < 5:
                                key = 'D'
                                os.system('xdotool key --window "$(xdotool search --name \'osu!cuttingedge\')" d')
                            elif abs(80 - xpos) < 5:
                                key = 'F'
                                os.system('xdotool key --window "$(xdotool search --name \'osu!cuttingedge\')" f')
                            elif abs(160 - xpos) < 5:
                                key = 'J'
                                os.system('xdotool key --window "$(xdotool search --name \'osu!cuttingedge\')" j')
                            elif abs(240 - xpos) < 5:
                                key = 'K'
                                os.system('xdotool key --window "$(xdotool search --name \'osu!cuttingedge\')" k')
                            print('click ' + key)
