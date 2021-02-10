import os
import subprocess
import time
import shutil

Number_Of_Files=0
#PATH = r'C:\Users\trcyp\Documents' 
PATH = '/home/pi/Public/'

for root, subFolder, files in os.walk(PATH):
    files.sort(key=str.lower)  # This sorts in-place
    subFolder.sort() # If you want sorted directories
    for item in files:
        #Number_Of_Files=Number_Of_Files+1
        fileNamePath = os.path.join(root, item)
        #sorted = sorted(fileNamePath)
        #subprocess.run(['telegram-upload', '-f', 'file_dumpster', str(sorted)])
        subprocess.run(['telegram-upload', '-f', 'file_dumpster', str(fileNamePath)])
        os.remove(fileNamePath)
        print(fileNamePath)
        time.sleep(3)
    #else:
        #print(Number_Of_Files)
