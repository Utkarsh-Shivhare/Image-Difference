import cv2
from pdf2image import convert_from_path
import numpy as np

def convert_pdf_to_images(pdf_file):
    return convert_from_path(pdf_file)

def preprocess_image(image):
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    resized_image = cv2.resize(gray_image, (800, 800))  # Adjust size as needed
    return resized_image

def compare_images(image1, image2):
    diff = cv2.absdiff(image1, image2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 200:  # Minimum area threshold
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 0, 255), 2)

    return image2

# Convert PDFs to images
images1 = convert_pdf_to_images('file_1.pdf')
images2 = convert_pdf_to_images('file_2.pdf')

# Preprocess images
preprocessed_image1 = preprocess_image(images1[0])
preprocessed_image2 = preprocess_image(images2[0])

# Compare and highlight differences
result_image = compare_images(preprocessed_image1, preprocessed_image2)

# Save and/or display the result
cv2.imwrite('result_image.png', result_image)
cv2.imshow('Differences', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
