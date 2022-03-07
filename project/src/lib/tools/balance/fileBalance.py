import os
import math
import asyncio
import shutil
from lib.tools.verificationDirectories import verificationDirectories

def fileBalance(path: str, number: int):
    """path is the directory that contain pdf files"""
    """number is the queanty of files for new folder"""
    try:
        files = os.listdir(path)
        filesCount = len(files)
        quantityOfFiles = math.ceil(filesCount/number)

        """Balance of files"""
        balance = lambda arr, n: [arr[i:i+n] for i in range(0, len(arr), n)]
        return balance(files, quantityOfFiles)
    except Exception as err:
        print(err)
        return "Error"

async def movingFiles(array: list, path: str):
    """array, files to move"""
   
    try:
        array_length = len(array)
        await asyncio.sleep(0.2)
        count = sum( [ len(listElem) for listElem in array])
        #print(f"Total files to copy: {count}")
        
        directory_array = []

        for index in range(array_length):
            verificationDirectories(path+"/Files package "+str(index+1))
            """print(outPath+"/Files package "+str(index+1))"""
            for file in array[index]:   
                total_items = len(array[index])
                source = path + "/" + file
                destination = path + "/Files package " + str(index+1)
                """print("Total files in this array: " + str(total_items))"""
                shutil.move(source, destination)  
            """Save new directory into the array"""
            directory_array.append(path + "/Files package " + str(index+1))
        return directory_array
    except Exception as err:
        print(err)
        return "Error"