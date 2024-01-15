import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces
chhatrapti_shivaji_raje_image = face_recognition.load_image_file("8-face-recognition-attendance/faces/AMAR.png")
raje_encoding = face_recognition.face_encodings(chhatrapti_shivaji_raje_image)

if not raje_encoding:
    print("No faces detected in chhatrapti_shivaji_raje_image")
    exit()


mastar_image = face_recognition.load_image_file("8-face-recognition-attendance/faces/mastar.jpg")
mastar_encoding = face_recognition.face_encodings(mastar_image)[0]

known_face_encodings = [raje_encoding, mastar_encoding]
known_face_names = ["chatrapati shivaji raje", "shashi bagal"]

# list of mastermind
mastarmind = known_face_names.copy()

face_location = []
face_encoding = []

# get the current date and time
now = datetime.now()
current_date = datetime.now().strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
   _, frame = video_capture.read()
   small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
   rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

   # Recognize faces
   face_locations = face_recognition.face_locations(rgb_small_frame)
   face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

   for face_encoding in face_encodings:
        # Check if any faces were detected
      # if not known_face_encodings:
      #    continue
      if len(known_face_encodings[0]) != len(face_encoding):
            continue

      matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
      face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
      best_match_index = np.argmin(face_distance)

      if matches[best_match_index]:
         name = known_face_names[best_match_index]

      # Add the text if person is present
      if name in known_face_names:
                
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " Present ", bottomLeftCornerOfText, font, fontScale, fontColor,
                            thickness, lineType)

                if name in mastarmind:
                    mastarmind.remove(name)
                    current_time = now.strftime("%H-%M%S")
                    lnwriter.writerow([name, current_time])
   for name in mastarmind:
        current_time = datetime.now().strftime("%H-%M%S")
        lnwriter.writerow([name, current_time])
   cv2.imshow("Attendance", frame)
   if cv2.waitKey(1) & 0xFF == ord("q"):
      break

video_capture.release()
cv2.destroyAllWindows()
f.close()