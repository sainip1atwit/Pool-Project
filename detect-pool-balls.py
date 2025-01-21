import cv2 as cv
import numpy as np

def mask_obj():
    frame = cv.imread('data/poolpic-1ball.jpg')

    gaussian_blur = cv.GaussianBlur(frame, (11, 11), 0)
    cv.imshow('blurred', gaussian_blur)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)

    lower = np.array([0,0,168])
    upper = np.array([172, 111, 255])

    mask = cv.inRange(hsv, lower, upper)
    cv.imshow('Mask', mask)

    cv.waitKey(0)
    cv.destroyAllWindows()

mask_obj()