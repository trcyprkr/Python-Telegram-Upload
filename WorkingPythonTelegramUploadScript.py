import os
import subprocess
import time

#Number_Of_Files=0
PATH = '/home/pi/Public/'

for root, subFolder, files in os.walk(PATH):
    files.sort(key=str.lower)  # This sorts in-place
    subFolder.sort() # If you want sorted directories
    for item in files:
        #Number_Of_Files=Number_Of_Files+1
        fileNamePath = os.path.join(root, item)
        subprocess.run(['telegram-upload', '-f', 'file_dumpster', str(fileNamePath)])
        os.remove(fileNamePath)
        print(fileNamePath)
        time.sleep(2800)
