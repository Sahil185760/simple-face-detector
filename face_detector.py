"""Find faces in an image and draw green rectangles around them."""

import argparse

import cv2


def main():
    # Read the image path supplied on the command line.
    parser = argparse.ArgumentParser(description="Detect faces in an image.")
    parser.add_argument("image_path", help="Path to the image to examine")
    args = parser.parse_args()

    image = cv2.imread(args.image_path)
    if image is None:
        parser.error("Could not read the image. Check the path and image format.")

    # OpenCV includes this pre-trained classifier, so no download is needed.
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        parser.error("Could not load OpenCV's face classifier.")

    # The classifier works with a grayscale version of the image.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # Each detection contains the rectangle's position, width, and height.
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

    print(f"Faces detected: {len(faces)}")
    cv2.imshow("Detected faces - press any key to close", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
