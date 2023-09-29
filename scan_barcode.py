import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        data = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (10,5,2), 2)
        print(data)
    cv2.imshow("Barcode Scanner", frame)
    if cv2.waitKey(1)==27:
        break
cap.release()

cv2.destroyAllWindows()