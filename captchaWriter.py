from cv2 import cv2
import numpy as np
from MappingLetters import MapLetters as Mapping

class CaptchaWriter:

    #findMatch Matches the template to letter
    @staticmethod
    def findMatch(filename,sourceImage):
        #print(filename)
        template = cv2.imread(filename,0)
        # cv2.imshow('sjo',template)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(sourceImage, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        #print(res)
        location = np.where(res >= threshold)
        if len(location[1])==0:
            return -1
        for point in zip(*location[::-1]):
            # cv2.rectangle(sourceImage,point,(point[0]+w,point[1]+h), (0,0,255),1)
            # cv2.imshow('sjo',sourceImage)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            return point[0]+w
        return 0

    #captchaResult returns the decoded Captcha
    @staticmethod
    def captchaResult(captchaCropped, letter):
        captcha = ""
        i=0
        while i<5:
            #print(i)
            for fname in Mapping.Map:
                width1, height1 = captchaCropped.shape[::-1] 
                #cv2.imshow("im",im)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                flag = False
                for fnameIndex in fname:
                    val = CaptchaWriter.findMatch(fnameIndex,letter)
                    #print(val,fnameIndex)
                    if val > 0:
                        #print(val)
                        # print(val,fnameIndex)
                        captchaCropped = captchaCropped[0:height1,val:width1]
                        #cv2.imshow("img1",img1)
                        if fnameIndex[-6] == 'm' or fnameIndex[-6]=='w':
                            letter = captchaCropped[0:height1,0:52]
                        else:
                            letter = captchaCropped[0:height1,0:45]
                        # cv2.imshow("im",letter)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                        #print(val)
                        #print(fname[0][-6])
                        captcha += fnameIndex[-6]
                        print(captcha)
                        flag = True
                        break
                if flag==True:
                    break
            i+=1
        return captcha