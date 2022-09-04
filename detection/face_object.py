class Face:
    def __init__(self, face, landmarks):
        self.width = face.right() - face.left()
        self.height = face.bottom() - face.top()
        if self.width != 0 and self.height != 0:
            self.ratio = self.width / self.height
        else:
            self.ratio = 0
        self.left_eye = Eye(landmarks.part(39).x - landmarks.part(36).x, landmarks.part(41).y - landmarks.part(37).y)
        self.right_eye = Eye(landmarks.part(45).x - landmarks.part(42).x, landmarks.part(46).y - landmarks.part(44).y)
        self.mouth = Mouth(landmarks.part(64).x - landmarks.part(60).x, landmarks.part(66).y - landmarks.part(62).y,
                           landmarks.part(54).x - landmarks.part(48).x, landmarks.part(57).y - landmarks.part(51).y)

    def to_string(self):
        return "Face\n  width: %d\n  height: %d\nEye\n  Left\n    width: %d\n    height: %d\n    ratio: %f\n  Right\n " \
               "   width: %d\n    height: %d\n    radio: %f\nMouth\n  Inside\n    width: %d\n    height: %d\n    " \
               "ratio: %f\n  Outside\n    width: %d\n    height: %d\n    ratio: %f\n" % (
                   self.width, self.height, self.left_eye.width, self.left_eye.height, self.left_eye.ratio,
                   self.right_eye.width, self.right_eye.height, self.right_eye.ratio, self.mouth.inside_width,
                   self.mouth.inside_height, self.mouth.inside_ratio, self.mouth.outside_width,
                   self.mouth.outside_height, self.mouth.outside_ratio)


class Eye:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if width != 0 and height != 0:
            self.ratio = width / height
        else:
            self.ratio = 0


class Mouth:
    def __init__(self, inside_width, inside_height, outside_width, outside_height):
        self.inside_width = inside_width
        self.inside_height = inside_height
        if inside_width != 0 and inside_height != 0:
            self.inside_ratio = inside_width / inside_height
        else:
            self.inside_ratio = 0
        self.outside_width = outside_width
        self.outside_height = outside_height
        if outside_width != 0 and outside_height != 0:
            self.outside_ratio = outside_width / outside_height
        else:
            self.outside_ratio = 0
