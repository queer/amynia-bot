from xdo import Xdo
import os
import imutils
import cv2

import time

# We time when each last keypress was, and then we make sure to wait at least 32ms
# (2 frames @ 60FPS) so that we don't get multiple keypresses
currentTimeMillis = lambda: int(round(time.time() * 1000))
sTime = currentTimeMillis()
dTime = currentTimeMillis()
fTime = currentTimeMillis()
spaceTime = currentTimeMillis()
jTime = currentTimeMillis()
kTime = currentTimeMillis()
lTime = currentTimeMillis()
WAIT_TIME_MILLIS = 80
xdo = Xdo()
window_id = xdo.search_windows(winname=bytes('osu!cuttingedge', 'utf-8'))[0]

mode = ''

cap = cv2.VideoCapture()
print('Waiting on video...')
cap.open('udp://127.0.0.1:1234/')
if not cap.open:
    print("Not open")
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
            # Holy FUCK do sliders kill us to death @_@
            M = cv2.moments(c)
            epsilon = 0.1 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)
            if len(approx) == 4:
                # Height
                if abs(30 - abs(approx[0][0][1] - approx[1][0][1])) < 5:
                    # Width
                    if abs(70 - abs(approx[0][0][0] - approx[2][0][0])) < 10:
                        ypos = abs(approx[1][0][1])
                        # TODO: Should adjust this based on the last position...
                        # Current best settings: 880~895
                        if ypos > 885 and ypos < 895:
                            #
                            # 4K mode
                            #
                            xpos = abs(approx[0][0][0])
                            # D~10 F~80 J~160 K~240
                            key = 'UNKNOWN'
                            if mode == '4K':
                                # D F J K
                                if abs(170 - xpos) < 5 and abs(dTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'D'
                                    xdo.send_keysequence_window(window_id, 'd'.encode('utf-8'))
                                    dTime = currentTimeMillis()
                                elif abs(240 - xpos) < 5 and abs(fTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'F'
                                    xdo.send_keysequence_window(window_id, 'f'.encode('utf-8'))
                                    fTime = currentTimeMillis()
                                elif abs(320 - xpos) < 5 and abs(jTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'J'
                                    xdo.send_keysequence_window(window_id, 'j'.encode('utf-8'))
                                    jTime = currentTimeMillis()
                                elif abs(400 - xpos) < 5 and abs(kTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'K'
                                    xdo.send_keysequence_window(window_id, 'k'.encode('utf-8'))
                                    kTime = currentTimeMillis()
                            elif mode == '7K':
                                # S D F (space) J K L
                                if abs(56 - xpos) < 5 and abs(sTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'S'
                                    xdo.send_keysequence_window(window_id, 's'.encode('utf-8'))
                                    sTime = currentTimeMillis()
                                if abs(136 - xpos) < 5 and abs(dTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'D'
                                    xdo.send_keysequence_window(window_id, 'd'.encode('utf-8'))
                                    dTime = currentTimeMillis()
                                elif abs(205 - xpos) < 5 and abs(fTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'F'
                                    xdo.send_keysequence_window(window_id, 'f'.encode('utf-8'))
                                    fTime = currentTimeMillis()
                                elif abs(289 - xpos) < 5 and abs(spaceTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = '(space)'
                                    xdo.send_keysequence_window(window_id, 'space'.encode('utf-8'))
                                    spaceTime = currentTimeMillis()
                                elif abs(360 - xpos) < 5 and abs(jTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'J'
                                    xdo.send_keysequence_window(window_id, 'j'.encode('utf-8'))
                                    jTime = currentTimeMillis()
                                elif abs(440 - xpos) < 5 and abs(kTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'K'
                                    xdo.send_keysequence_window(window_id, 'k'.encode('utf-8'))
                                    kTime = currentTimeMillis()
                                elif abs(515 - xpos) < 5 and abs(lTime - currentTimeMillis()) > WAIT_TIME_MILLIS:
                                    key = 'L'
                                    xdo.send_keysequence_window(window_id, 'l'.encode('utf-8'))
                                    fTime = currentTimeMillis()
                            # If we don't know what something is, just outright ignore it and hope for the best
                            if key == 'UNKNOWN':
                                continue
                            print('click ' + key + ' @ (' + str(xpos) + ', ' + str(ypos) + ').')
                else:
                    height = abs(approx[0][0][1] - approx[1][0][1])
                    if abs(140 - height) < 20:
                        width = abs(approx[0][0][0] - approx[2][0][0])
                        xpos = abs(approx[0][0][0])
                        if abs(56 - xpos) < 5:
                            if mode != '7K':
                                mode = '7K'
                        elif abs(170 - xpos) < 5:
                            if mode != '4K':
                                mode = '4K'
                        #key_size_guess = width / 70.0
                        #if key_size_guess > 6 and key_size_guess < 8:
                        #    print('Guessing that 7K')
                        #elif key_size_guess > 3 and key_size_guess < 5:
                        #    print('Guessing that 4K')
                        #else:
                        #    print('?K: width=' + str(width) + ', key_size_guess=' + str(key_size_guess) + ', xpos=' + str(abs(approx[0][0][0])) + ', ypos=' + str(abs(approx[1][0][1])))

