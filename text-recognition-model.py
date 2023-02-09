import pytesseract
from PIL import Image

# Open the image and convert it to grayscale
image = Image.open("sample.png").convert("L")

# Use pytesseract to extract the text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
