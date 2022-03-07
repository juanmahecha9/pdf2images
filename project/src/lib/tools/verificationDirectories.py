import os
import time
import shutil

def verificationDirectories(path: str):
    print(f"Verification of {path} in process")
    result = ""
    try:
        if os.path.exists(path):
            print(f"Dropping {path}")
            shutil.rmtree(path)
            time.sleep(0.2)
            print(f"Creating {path}")
            os.mkdir(path)
        else:
            os.mkdir(path)
        print("Verification successful...")
        
    except Exception as err:
        print(err)
        