# Text Recognition Model

Train a text recognition model that extracts textual information from images using the Tesseract module. Use any image of your choice for this challenge. 

# About

This code uses the `Image` module from the `Python Imaging Library (PIL)` to open and convert an image to `grayscale`, and the `pytesseract` module to extract text from the image. The `image_to_string` function from the pytesseract module is used to extract the text, which is then printed.

## Note
Note that the accuracy of text recognition using the Tesseract module can be improved by pre-processing the image and providing appropriate configuration options to the image_to_string function. You can find more information on how to use the Tesseract module and improve its accuracy in the official documentation: https://tesseract-ocr.github.io/
