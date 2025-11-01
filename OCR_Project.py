!pip install easyocr opencv-python matplotlib

import cv2
import matplotlib.pyplot as plt
import easyocr
import os

# Initialize the EasyOCR reader for English language
reader = easyocr.Reader(['en'])

image_path = "/content/ocr_images/sample_text.jpg"

# Load image using OpenCV
img = cv2.imread(image_path)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("Input Image")
plt.show()

# Perform OCR
results = reader.readtext(image_path)

# Display detected text and bounding boxes
for (bbox, text, prob) in results:
    print(f"Detected: {text} (Confidence: {prob:.2f})")

for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Detected Text Regions")
plt.axis('off')
plt.show()

output_file = "/content/extracted_text.txt"
with open(output_file, "w") as f:
    for (bbox, text, prob) in results:
        f.write(f"{text}\n")
print("Extracted text saved to:", output_file)
