import cv2
from deepface import DeepFace as df
img1=cv2.imread(".\\1_20_FET_BCS_139.png")
img2=cv2.imread(".\\1_20_FET_BCS_139.png")
result=df.verify(img1,img2)
print (result)

# import cv2
# import face_recognition

# # Load the images of the two faces to compare
# image1 = face_recognition.load_image_file(".\\1_20_FET_BCS_139.png")
# image2 = face_recognition.load_image_file(".\\1_20_FET_BCS_139.png")

# # Get the face encodings of the two images
# face_encoding1 = face_recognition.face_encodings(image1)[0]
# face_encoding2 = face_recognition.face_encodings(image2)[0]

# # Compare the face encodings using the compare_faces method
# results = face_recognition.compare_faces([face_encoding1], face_encoding2)

# # Print the results
# if results[0] == True:
#     print("The two faces are the same person")
# else:
#     print("The two faces are not the same person")
