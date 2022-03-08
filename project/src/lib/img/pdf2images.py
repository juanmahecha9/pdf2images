import os
from PIL import Image
import fitz
from numpy import rint

def pdf2img(pdfsPath: str, imagesPath: str, compression:any):
    print(f"Listing files of {pdfsPath}")
    count = 0
    arr = []

    """Open PDF files"""
    files = os.listdir(pdfsPath)
    for file in files:
        count += 1
        pdfFile = os.path.join(pdfsPath, file)

        split = file.split('.')
        imageName = split[0] + ".png"
        newImage = os.path.join(imagesPath, imageName)
        
        arr.append(newImage)
        """Converting files"""
        convert(pdfFile, newImage, compression)

def convert(file: str, imagesPath: str, compression):
    try:
        zoom = 2
        mat = fitz.Matrix(zoom, zoom)

        doc = fitz.open(file)
        imageList = []

        for page in doc:
            pix = page.get_pixmap(matrix = mat)
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            imageList.append(image)

        if imageList:
            imageList[0].save(
                imagesPath,
                save_all=True,
                append_images=imageList[1:],
                compression=compression,
                dpi=(300, 300),
            )
    except Exception as err:
        print(err)