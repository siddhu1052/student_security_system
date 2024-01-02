import face_recognition
from PIL import Image, ImageDraw

def load_and_encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)
    if face_encoding:
        return face_encoding[0]
    return None

def compare_faces(image_path1, image_path2):
    # Load and encode faces
    face_encoding1 = load_and_encode_image(image_path1)
    face_encoding2 = load_and_encode_image(image_path2)

    if face_encoding1 is None or face_encoding2 is None:
        return False  # Unable to find faces in one or both images

    # Compare faces
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)
    return results[0]

def draw_rectangle_on_face(image_path, face_location):
    image = face_recognition.load_image_file(image_path)
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    top, right, bottom, left = face_location
    draw.rectangle([left, top, right, bottom], outline="red", width=2)
    pil_image.show()

# Example usage
image_path1 = r'Student_images\1_20_FET_BCS_139.png'
image_path2 = r'Student_images\temp.png'

are_same_person = compare_faces(image_path1, image_path2)

if are_same_person:
    print("The two photos are of the same person.")
else:
    print("The two photos are of different people.")

