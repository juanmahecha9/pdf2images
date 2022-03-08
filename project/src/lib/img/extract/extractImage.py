from email.mime import image
from traceback import print_tb
import fitz 
from PIL import Image 
import os
import uuid
import datetime

def extractImage(pdfsPath: str, imagesPath: str):
    print("Extracting image...")
    files = os.listdir(pdfsPath)
    for file in files:
        pdf = fitz.open(pdfsPath + "/" + file)
        #Sellect the page number 
        imageList = pdf.getPageImageList(0)

        #Extract the image
        for image in imageList:
            xref = image[0]
            pix = fitz.Pixmap(pdf, xref)
            myUUID = uuid.uuid4()
            now = str(datetime.datetime.now())
            now_ = now.replace(":", "")
            #Validate name

            if pix.n < 5:
                pix.writePNG(f'{imagesPath}/{myUUID}-{now_}.png')    
            else:
                pix1 = fitz.open(fitz.csRGB, pix)
                pix1.writePNG(f'{imagesPath}/{myUUID}.png')
                pix1 = None
            pix = None
        #print the images
        print(len(imageList), 'detected')