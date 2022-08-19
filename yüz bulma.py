import cv2

camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("frontalface.xml")

while True:
    _,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+y,y+h),(0,255,0),2)
    cv2.imshow("camera",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()