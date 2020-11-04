from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open("image.png"),lang="eng",config=' -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789'))
