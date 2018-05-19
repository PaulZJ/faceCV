#coding=utf-8

import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

img = cv2.imread("img/xingye-1.png")

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if(isinstance(img, numpy.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

img = cv2ImgAddText(img, "这是测试文字~~", 140, 60, (255, 255, 0), 20)

cv2.imshow("IMg", img)
cv2.waitKey(0)
cv2.destroyWindow()
