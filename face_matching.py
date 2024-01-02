from deepface import DeepFace
import cv2

def face_comparision(path1,path2):
    
    image1 = "Student_images\1_20_FET_BCS_139.jpg"
    image2 = "Student_images\temp.jpg"
    img1=cv2.imread("image1.jpg")
    img2=cv2.imread("image2.jpg")
    is_same_person = DeepFace.verify(img1, img2)
    if is_same_person:
        print("The two faces are the same person.")
    else:
        print("The two faces are not the same person.")
