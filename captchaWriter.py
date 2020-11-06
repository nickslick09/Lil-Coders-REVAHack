from cv2 import cv2
import numpy as np
from MappingLetters import MapLetters as Mapping

class CaptchaWriter:
    # def __init__(self):
    #     print("Hello")
    
    #findMatch Matches the template to letter
    @staticmethod
    def findMatch(filename,sourceImage):
    #print(filename)
        template = cv2.imread(filename,0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(sourceImage, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        #print(res)
        location = np.where(res >= threshold)
        if len(location[1])==0:
            return -1
        for point in zip(*location[::-1]):
            #cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h), (0,0,255),1)
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
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                val = CaptchaWriter.findMatch(fname[0],letter)
                #print(val,fname[0])
                if val > 0:
                    #print(val)
                    captchaCropped = captchaCropped[0:height1,val:width1]
                    #cv2.imshow("img1",img1)
                    letter = captchaCropped[0:height1,0:45]
                    # cv2.imshow("im",im)
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
                    #print(val)
                    #print(fname[0][-6])
                    captcha += fname[0][-6]
                    break
                else:
                    val = CaptchaWriter.findMatch(fname[1],letter)
                    if val > 0:
                        #print(fname[1][-6])
                        break
            i+=1
        return captcha