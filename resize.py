import cv2
import os
import numpy as np
path=os.path.join('assets','resize')
output_path='resized'
for filename in os.listdir(path):
    image_path=os.path.join(path,filename)
    image=cv2.imread(image_path)
    resized=cv2.resize(image,(256,256))
    op_path=os.path.join(output_path,filename)
    cv2.imwrite(op_path,resized)
    print('done')


