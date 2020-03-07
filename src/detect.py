import numpy as np
import matplotlib.pyplot as plt
import cv2


stop_cascade = cv2.CascadeClassifier('../data/traffic_cascades/Speedlimit_24_15Stages.xml')
captura = cv2.VideoCapture(0)


def detect_stop(imagen):
    imagen1 = imagen.copy()
    rectangulos = stop_cascade.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1, (x,y), (x+w, y+h), (255,0,0), 10)
    return imagen1


while True:
    res,video = captura.read(0)
    video = detect_stop(video)
    cv2.imshow('Detectar stop', video)
    tecla = cv2.waitKey(1)
    if tecla == 27:
        break

captura.release()
cv2.destroyAllWindows() 