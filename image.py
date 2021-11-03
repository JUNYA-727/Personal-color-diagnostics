import cv2
import dlib
from imutils import face_utils

def image_create(path):
    predict_image=cv2.resize(path,dsize=(300,300))
    predict_image=predict_image/255.0
    predict_image=predict_image.reshape(1,300,300,3)
    return predict_image

def face(path):
    face_detector = dlib.get_frontal_face_detector()
    predictor_path = 'shape_predictor_68_face_landmarks.dat'
    face_predictor = dlib.shape_predictor(predictor_path)
    img=cv2.imread(path)
    faces=face_detector(img,1)
    if len(faces)>0:
        for face in faces:
            landmark=face_predictor(img,face)
            landmark = face_utils.shape_to_np(landmark)
            if landmark[19][1]>=landmark[24][1]:
                top=landmark[19][1]
            else:
                top=landmark[24][1] 
            bottom=landmark[8][1]
            left=landmark[0][0]
            right=landmark[16][0]
            FACE=img[top:bottom,left:right]
  #facesが0の場合
    else:
        FACE=img

    return FACE

if __name__=='__main__':
    image_create()
    face()