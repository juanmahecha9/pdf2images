import os
from threading import local
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import time
import shutil

from numpy import source

imageExtension = ['.JPEG','.JPG','.JPE','.JIF','.JFI','.JFIF','.GIF','.PNG','.BMP','.TIF','.jpeg','.jpg','.jpe','.jif','.jfi','.jfif','.gif','.png','.bmp','.tif']

"""Split pdf in sheets"""
def PDF2Sheets(pdfsPath: str, sheetsPath: str, imagesPath: str):
    try:
        files = os.listdir(pdfsPath)
        for file in files:
            if ".pdf" in file:
                time.sleep(0.1)
                fileName = file.replace(".pdf", "")
                
                """Read PDF file"""
                pdfPath = os.path.join(pdfsPath,file)
                pdfReader = PdfFileReader(open(pdfPath, "rb"))
                numberPages = pdfReader.getNumPages()
                """Container of each page in the pdf file"""
                container = {}

                """Split in pages"""
                for numberPage in range(numberPages):
                    container[f"pdfWriter{numberPage}"] = PdfFileWriter()
                    container[f"pdfWriter{numberPage}"].addPage(pdfReader.getPage(numberPage))
                    
                    """Create a new file"""
                    with open(f"{sheetsPath}/{fileName}_page_number_{numberPage+1}.pdf","wb") as newFile:
                        container[f"pdfWriter{numberPage}"].write(newFile)
                    time.sleep(0.1)
                print(f"PDF was split in {numberPages} pages, successful.")
            elif any(x in file for x in imageExtension):
                print("Copy image file into the folder of images")
                source = pdfsPath + "/" + file
                destination = imagesPath + "/" + file
                shutil.copy(source, destination)
            else:
                print("This is other file")
    except Exception as err:
        print(err)