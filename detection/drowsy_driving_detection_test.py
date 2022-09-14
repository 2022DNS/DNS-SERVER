import cv2
import dlib
import face_object
import time

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

eye_close_frame_count = 0

frame_count = 0

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    start = time.time()

    faces = detector(gray)
    i = 0
    for face in faces:
        i += 1
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(gray, (x1, y1), (x2, y2), (0, 0, 0), 3)
        landmarks = predictor(gray, face)

        n = 0
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(gray, (x, y), 1, (255, 255, 255), -1)

        if n > 0:
            faceInfo = face_object.Face(face, landmarks)
            cv2.putText(gray, "Left Eye Ratio: %f" % faceInfo.left_eye.ratio, (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(gray, "Right Eye Ratio: %f" % faceInfo.right_eye.ratio, (10, 140), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 0), 1, cv2.LINE_AA)

            if faceInfo.left_eye.ratio > 5 or faceInfo.right_eye.ratio > 5:
                cv2.putText(gray, "Close!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                eye_close_frame_count = eye_close_frame_count + 1
                cv2.imwrite("image/close_%d.jpg" % frame_count, gray)
                frame_count = frame_count + 1
            else:
                cv2.putText(gray, "Open!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                eye_close_frame_count = 0
                cv2.imwrite("image/open_%d.jpg" % frame_count, gray)
                frame_count = frame_count + 1

            print(faceInfo.to_string())

            if eye_close_frame_count > 3:
                cv2.putText(gray, "Warning!", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    cv2.imshow("Frame", gray)

    key = cv2.waitKey(1)

    if key == 27:
        break

      # time.sleep(0.05)
#
# frame = cv2.imread('image/123.jpg', cv2.IMREAD_GRAYSCALE)
# gray = frame
#
# start = time.time()
#
# faces = detector(gray)
# i = 0
# for face in faces:
#     i += 1
#     x1 = face.left()
#     y1 = face.top()
#     x2 = face.right()
#     y2 = face.bottom()
#     cv2.rectangle(gray, (x1, y1), (x2, y2), (0, 0, 0), 3)
#     landmarks = predictor(gray, face)
#
#     for n in range(0, 68):
#         x = landmarks.part(n).x
#         y = landmarks.part(n).y
#         cv2.circle(gray, (x, y), 1, (255, 255, 255), -1)
#
#     if landmarks.num_parts > 0:
#         faceInfo = face_object.Face(face, landmarks)
#         cv2.putText(gray, "Left Eye Ratio: %f" % faceInfo.left_eye.ratio, (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
#                     (0, 0, 0), 1, cv2.LINE_AA)
#         cv2.putText(gray, "Right Eye Ratio: %f" % faceInfo.right_eye.ratio, (10, 140), cv2.FONT_HERSHEY_SIMPLEX,
#                     0.5, (0, 0, 0), 1, cv2.LINE_AA)
#
#         if faceInfo.left_eye.ratio > 5 or faceInfo.right_eye.ratio > 5:
#             cv2.putText(gray, "Close!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#             eye_close_frame_count = eye_close_frame_count + 1
#             cv2.imwrite("image/close_%d.jpg" % frame_count, gray)
#             frame_count = frame_count + 1
#         else:
#             cv2.putText(gray, "Open!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#             eye_close_frame_count = 0
#             cv2.imwrite("image/open_%d.jpg" % frame_count, gray)
#             frame_count = frame_count + 1
#
#         print(faceInfo.to_string())
#
#         if eye_close_frame_count > 3:
#             cv2.putText(gray, "Warning!", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#
# cv2.imshow("Frame", gray)
#
# key = cv2.waitKey(1)
#
# time.sleep(0.05)
#