import cv2
from pyzbar import pyzbar
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

def compare_faces(img1):
    {
        

    }
    return True
    

while True:
    ret, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        data = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (10,5,2), 2)
        path=str(data)
        path=path.replace("/","_")
        extension=".png";
        b="Student_images\\"
        path=b+path+extension
        print(data)
        print(path);
        img = cv2.imread(path);
        plt.imshow(img)
        while True :
            cv2.imshow('result',img)
            if cv2.waitKey(2)==27 :
             break
        
        
    cv2.imshow("Barcode Scanner", frame)
    if cv2.waitKey(1)==27:
        break
cap.release()

cv2.destroyAllWindows()