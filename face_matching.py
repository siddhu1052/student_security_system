from deepface import DeepFace
import cv2

image1 = "image1.jpg"
image2 = "image2.jpg"


img1=cv2.imread("image1.jpg")
img2=cv2.imread("image2.jpg")


is_same_person = DeepFace.verify(img1, img2)


if is_same_person:
    print("The two faces are the same person.")
else:
    print("The two faces are not the same person.")
