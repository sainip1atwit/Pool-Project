import cv2 as cv
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

def mask_obj():
    frame = cv.imread('data/poolpic-1ball.jpg')

    gaussian_blur = cv.GaussianBlur(frame, (11, 11), 0)
    cv.imshow('blurred', gaussian_blur)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)

    yellow = [0, 255, 255]
    lower, upper = get_limits(yellow)

    mask = cv.inRange(hsv, upper, lower)
    cv.imshow('Mask', mask)

    cv.waitKey(0)
    cv.destroyAllWindows()

mask_obj()