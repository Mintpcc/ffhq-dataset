import cv2
import os
from glob import glob

filelists = glob(os.path.join('./images1024x1024', '*.png'))
new_img_path = '/home/mint/PycharmProjects/dataset/ffhq-256/'
new_size = 256
if not os.path.exists(new_img_path):
    os.mkdir(new_img_path)

for i in range(len(filelists)):
    img = cv2.imread(filelists[i])
    img_name = filelists[i].split('/')[-1]
    img = cv2.resize(img, (new_size, new_size), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(new_img_path + img_name, img)