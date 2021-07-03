# Dependencies
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import os

class HappyFace:

    def __init__(self, known_person_path_file, unknown_images_path_file, known_name=None):
        self.known_person_path_file = known_person_path_file
        self.unknown_images_path_file = unknown_images_path_file
        self.known_name = known_name or 'Found U!'

    # Converts the known image for usability
    def converted_known_image(self):
        return face_recognition.load_image_file(self.known_person_path_file)

    # Displays the known image
    def display_known_im(self):
        Image.fromarray(self.converted_known_image()).show(self.converted_known_image())

    # Detects the face of the known image
    def detects_known_face(self):

        face_locations = face_recognition.face_locations(self.converted_known_image())

        for face_location in face_locations:
            top, right, bottom, left = face_location
            Image.fromarray(self.converted_known_image()[top:bottom, \
                            left:right]).show(self.converted_known_image()[top:bottom, left:right])

    # Detects the face of the unknown image(s)
    def detects_unknown_faces(self):

        for file in os.listdir(self.unknown_images_path_file):
            if file[0] != '.':     #Sometimes there are hidden files, they start with a dot --.--
                im = face_recognition.load_image_file(self.unknown_images_path_file + '/' + file)
                face_locations = face_recognition.face_locations(im)

                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    Image.fromarray(im[top:bottom, \
                    left:right]).show(im[top:bottom, left:right])

    def recognize_faces(self):

        for file in os.listdir(self.unknown_images_path_file):
            if file[0] != '.':  #So we don't display hidden files nor remove them.
                known_image = self.converted_known_image()
                known_image_encoding = face_recognition.face_encodings(known_image)[0]
                known_face_encodings = [known_image_encoding]
                known_face_names = [self.known_name]

                # Load the image with the unknown face
                unknown_image = face_recognition.load_image_file(self.unknown_images_path_file + '/' + file)

                # Find all the faces and face encodings in the unknown image
                face_locations = face_recognition.face_locations(unknown_image)
                face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

                # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
                pil_image = Image.fromarray(unknown_image)

                # Create a Pillow ImageDraw Draw instance to draw with
                draw = ImageDraw.Draw(pil_image)

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "STRANGER!"
                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    # Draw a box around the face using the Pillow module
                    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

                    # Draw a label with a name below the face
                    text_width, text_height = draw.textsize(name)
                    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
                    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

                # Remove the drawing library from memory as per the Pillow docs
                del draw

                # Display the resulting image
                pil_image.show()






