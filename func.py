from time import sleep
from PIL import Image
import os
import natsort

def counting():
    c = 0
    while c != 20:
        c += 1
        print(c)
        sleep(1)
        continue

def img_con(src, dest):
    # print(src, dest)
    img_in = (natsort.natsorted(os.listdir(src)))
    try:
        for f in img_in:
            image_1 = Image.open(src+f)
            im_1 = image_1.convert('RGB')
            im_1.save(dest+f.split('.')[-2]+'.pdf')
            continue
    except:
        print(Exception)