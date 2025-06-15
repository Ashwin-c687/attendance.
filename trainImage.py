import os
import cv2
import numpy as np
from PIL import Image

def TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message, text_to_speech):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Ids = getImagesAndLabels(trainimage_path)
    recognizer.train(faces, np.array(Ids))
    recognizer.save(trainimagelabel_path)
    res = "Image Trained successfully"
    message.configure(text=res)
    text_to_speech(res)

def getImagesAndLabels(path):
    newdir = [os.path.join(path, d) for d in os.listdir(path)]
    image_paths = [os.path.join(newdir[i], f) for i in range(len(newdir)) for f in os.listdir(newdir[i])]
    faces = []
    Ids = []
    for image_path in image_paths:
        pil_image = Image.open(image_path).convert("L")
        image_np = np.array(pil_image, "uint8")
        Id = int(os.path.split(image_path)[-1].split("_")[1])
        faces.append(image_np)
        Ids.append(Id)
    return faces, Ids

