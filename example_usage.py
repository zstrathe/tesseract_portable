####################################################################
##  Example usage for Pytesseract and the portable tesseract.exe  ##
##     to use with PyInstaller                                    ##
####################################################################
import sys
import os
import pytesseract
import pyautogui

# Setup resource path, a relative path for use with PyInstaller
# When the output .exe from PyInstaller runs, it will extract all files to a temp folder (sys._MEIPASS) in Windows
# The 'resource_path' function sets the file path to the sys._MEIPASS location if it was created by PyInstaller
# For development (i.e., not using a .exe output from PyInstaller), this sets up the file path normally
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Configure Tesseract path for PyTesseract
pytesseract.pytesseract.tesseract_cmd = resource_path(r'tess\tesseract.exe')

## Take a screenshot with PyAutoGUI and use PyTesseract to perform OCR and convert the image into a string
im = pyautogui.screenshot(region=(0,0,100,100)) # take a 100x100 pixel screenshot at location 0,0 on the primary monitor | region=(LEFT, TOP, WIDTH, HEIGHT)
im_scale = 3 # scale for resizing the screenshot (I found that sometimes tesseract works better if you are trying to use OCR on smaller text
im_newsize = (im.size[0]*im_scale,im.size[1]*im_scale) 
im = im.resize(im_newsize, Image.ANTIALIAS) # resize the image
#im.save('test.png') # Uncomment to save the screenshot to check positioning
image_str = pytesseract.image_to_string(im,config='--psm 6 -c preserve_interword_spaces=1').strip() # call PyTesseract on the screenshot image, and save the output as a string

print(image_str)