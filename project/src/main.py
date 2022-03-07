#!/usr/bin/env bash
import flask as Flask
import sys
import os
import time
import asyncio

from pandas import array
from lib.tools.verificationDirectories import verificationDirectories
from lib.pdf.splitPdfInSheets import PDF2Sheets
from lib.tools.balance.fileBalance import fileBalance, movingFiles

argv = "/Users/juanmaheha/Documents/all/jairo/test"
  
"""Main function"""
async def main(pdfsPath):
    
    """New folder"""
    newRoutePdf = os.path.join(pdfsPath, "MovingFiles")
    imagesPath = os.path.join(pdfsPath, "Images")
    arr = [newRoutePdf, imagesPath]

    """Verify the directories"""
    for i in arr:
        verificationDirectories(i)
        time.sleep(0.1)
    
    PDF2Sheets(pdfsPath, newRoutePdf, imagesPath)
    arrayOfFiles = fileBalance(newRoutePdf, 8)
    time.sleep(0.1)
    newDirectories = await movingFiles(arrayOfFiles, newRoutePdf)
    time.sleep(0.1)
    """pdf to images"""
    

if __name__ == "__main__":
    print("Dev: Juanmahecha9")
    """Starts async function"""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(argv))


       