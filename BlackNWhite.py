#Import the necesseray Packages
from cv2 import cv2

class BlacknWhite:
    @staticmethod
    def TurnBlacknWhite(filename):
        #filename = "bf478.jpg"
        originalImage = cv2.imread(filename)
        cv2.imshow('234',originalImage)
        # duplicateImage = cv2.imread(filename)
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

        #Make Image Black and White    change ThreshholdValue to your preference
        # ThreshholdValue = 100
        # (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, ThreshholdValue, 255, cv2.THRESH_BINARY)

        #To Make GrayImage Black and White and removing the background gradient
        BlockSize = 11
        Constant = 3
        atmc = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, BlockSize, Constant)

        #Display All the Image Varients

        # cv2.imshow('Original image',originalImage)
        # cv2.imshow('Black white image', blackAndWhiteImage)
        # cv2.imshow('Gray image', grayImage)
        cv2.imshow('atmc', atmc)
        newfilename = filename[:-4]+"_bw"+filename[-4:]
        cv2.imwrite(newfilename,atmc)

        cv2.waitKey(0)
        cv2.destroyAllWindows()