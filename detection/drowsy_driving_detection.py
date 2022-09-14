import base64
import io
import cv2
import dlib
import json

from detection import face_object


# Class for constant results.
class DnsResult():
    __slots__ = ()
    failed_to_detect_face = -1
    failed_to_detect_face_landmarks = -2
    detect_face_landmarks_not_correctly = -3
    drowsy_driving_not_detected = 0
    drowsy_driving_detected = 1


dns_result = DnsResult()

# Face detector.
detector = dlib.get_frontal_face_detector()

# Face landmark detector.
predictor = dlib.shape_predictor("model/shape_predictor_68_face_landmarks.dat")

# Eye width/height ratio limit to be perceived as closed.
eye_closed_ratio_limit = 5


# Check drowsy driving from received images.
# This function detect drowsy driving only by eye size and eye closed.
# Required parameter: json data: { byte_images: [ "img_data", ..., "img_data" ] }
# Return value: int value(dns_result)
def check_drowsy_driving_based_on_eye_condition(encoded_image_list):
    # Change

    eye_close_frame_count = 0
    for encoded_image in encoded_image_list:
        # Get each image from encoded image list and change to be usable in OpenCV.
        decoded_image = cv2.imread(io.BytesIO(base64.b64decode(encoded_image)))

        faces = detector(decoded_image)

        # If detect face failed.
        if faces == 0:
            return dns_result.failed_to_detect_face

        # Use first face in list.
        face = faces[0]
        landmarks = predictor(decoded_image, face)
        # Draw circle of landmarks.
        # for landmark_index in range(0, 68):
        #     cv2.circle(decoded_image, (landmarks.part(landmark_index).x, landmarks.part(landmark_index).x), 1,
        #                (255, 255, 255), -1)

        if landmarks.num_parts == 0:
            return dns_result.failed_to_detect_face_landmarks

        # Create face object when face landmark detected.
        face_info = face_object.Face(face, landmarks)

        if face_info.left_eye.ratio == 0 or face_info.right_eye.ratio == 0:
            return dns_result.detect_face_landmarks_not_correctly

        if face_info.left_eye.ratio > eye_closed_ratio_limit or face_info.right_eye.ratio > eye_closed_ratio_limit:
            # If it is determined that the eyes are dozing.
            eye_close_frame_count += 1
        else:
            # If the eyes are normally open even once, the sleepiness detect count is reset to 0.
            eye_close_frame_count = 0

    if eye_close_frame_count < 4:
        # If eyes are closed for more than 4 consecutive frames, assess the driver as drowsy driving.
        return dns_result.drowsy_driving_not_detected

    return dns_result.drowsy_driving_detected
