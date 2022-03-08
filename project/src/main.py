#!/usr/bin/env bash
import flask as Flask
import sys
import os
import time
import asyncio

from numpy import quantile

from lib.tools.verificationDirectories import verificationDirectories
from lib.pdf.splitPdfInSheets import PDF2Sheets
from lib.tools.balance.fileBalance import fileBalance, movingFiles
from lib.img.pdf2images import pdf2img
from lib.img.extract.extractImage import extractImage


argv = "C:/Users/mahechacruz.6/BackUP/Rimac/" #Path


"""Main function"""
async def main(pdfsPath):
    pdfsPath_ = pdfsPath + "/pdfs/" 
    
    """New folder"""
    newRoutePdf = pdfsPath + "MovingFiles"
    imagesPath = pdfsPath + "Images"
    imagesExtracted = pdfsPath + "Extracted"
    arr = [newRoutePdf, imagesPath, imagesExtracted]

    """Verify the directories"""
    for i in arr:
        verificationDirectories(i)
        time.sleep(0.1)
    
    quantity = 20

    PDF2Sheets(pdfsPath_ , newRoutePdf, imagesPath)
    arrayOfFiles = fileBalance(newRoutePdf, quantity)
    time.sleep(0.1)
    newDirectories = await movingFiles(arrayOfFiles, newRoutePdf)
    time.sleep(0.1)
    """pdf to images"""
    for dir in newDirectories:
        print(dir)
        pdf2img(dir, imagesPath, 'zip')

    time.sleep(0.1)

    """Extract images"""
    for dir in newDirectories:
        extractImage(dir, imagesExtracted)
        
if __name__ == "__main__":
    print("Dev: Juanmahecha9")
    """Starts async function"""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(argv))


       