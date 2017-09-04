import cv2
import numpy as np
import os


indir = "G:/Projects/ai_game_test/cactus"
pic_num = 121

for fn in os.listdir(indir):
    print(fn)
    jpg = fn[-3:-1]
    if jpg == "jp":

        img = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (42,79))
        resized_image = cv2.flip(resized_image,1)
        cv2.imwrite("neg/" + str(pic_num) +'.jpg',resized_image)
        pic_num += 1

