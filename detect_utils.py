import numpy as np
import cv2, pickle, keras
from keras.preprocessing.image import ImageDataGenerator

# Cargamos las variables que vamos a necesitar
# Modelo para clasificar:
# model = keras.models.load_model("../data/model/model_train.h5")
# El diccionario con el código de las señales
labels = pickle.load(open('data/data8.pickle','rb'))["labels"]
# Nombre de la ventana.
window_name = 'Detect traffic signs'
datagen = ImageDataGenerator(featurewise_center=True, featurewise_std_normalization=True)



def is_this_sign(sign, ids_sign):
    return True in [sign == i for i in ids_sign]



def put_name_sign(image, sign, location=(50, 50), fontScale=0.5, color=(0, 0, 255), font=cv2.FONT_HERSHEY_SIMPLEX, thickness=1):
    width, heigh = cv2.getTextSize(sign, cv2.FONT_HERSHEY_SIMPLEX, fontScale, thickness)[0]
    location = (location[0]-width, location[1]+heigh+3)
    image = cv2.putText(image, sign, location, font, fontScale, color, thickness, cv2.LINE_AA) 



def capture_sign(image, x, y , w, h):
    if x+w > image.shape[1]:
        w = image.shape[1] - x
    if y+h > image.shape[0]:
        h = image.shape[0] - y
    sign_arr = np.array([image[y:y+h,x:x+w,:]])
    if sign_arr.shape[0] > 0 and sign_arr.shape[1] > 0:
        sign_scale = np.array([cv2.resize(sign_arr[0], (32,32))])[:,:,:,0:1]
        datagen.fit(sign_scale)
        model = keras.models.load_model("data/model/model_train.h5")
        return np.argmax(model.predict(sign_scale))
    return None


def detect_sign(imag=[], cascade="stop_cascade.xml", ids_sign = [14], color_box=(0, 0, 255), color_text=(0, 0, 255), thickness=2):
    URL = 'data/traffic_cascades/'
    sign_cascade = cv2.CascadeClassifier(f'{URL}{cascade}')
    imag1 = imag.copy()
    rectangles = sign_cascade.detectMultiScale(imag1, 1.05, 3)
    for (x,y,w,h) in rectangles:
        sign = capture_sign(imag1,x,y,w,h)
        if is_this_sign(sign, ids_sign):
            cv2.rectangle(imag1, (x,y), (x+w, y+h), color_box, thickness)
            put_name_sign(imag1, labels[sign], location=(x+w//2, y+h), color=color_text)
    return imag1



def run_video_capture(stop=True, speed_limit=False, triangle_sign=False):
    capt = cv2.VideoCapture(0)
    while True:
        _,video = capt.read(0)
        if stop:
            video = detect_sign(video)
        if speed_limit:
            video = detect_sign(video, "speed_limit_es.xml", [1,2,3,4,5,6,8,9], (255,0,0), (255,0,0))
        if triangle_sign:
            video = detect_sign(video, "triangular_cascade.xml", [12,14,19,20,21,22,23,24,25,26,27,28,29,30,31,32], (0,255,0), (0,255,0))
        cv2.imshow(window_name, video)
        key = cv2.waitKey(1)
        if key == 27:
            break
    capt.release()
    cv2.destroyAllWindows()

