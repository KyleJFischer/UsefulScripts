from os import listdir
import os
from os.path import isfile, join
import time
import sys


def MoveFilesBasedExtension(sourcePath, destinationPath, extension):
        onlyfiles = [f for f in listdir(sourcePath) if isfile(join(sourcePath, f))]
        for x in onlyfiles:
            if x.endswith(extension):
                print("Moving: " + x)
                os.replace(join(sourcePath, x), join(destinationPath, x.replace('', '')))


if __name__ == "__main__" :
    if (len(sys.argv) > 3):
        sourcePath = sys.argv[1]
        destinationPath = sys.argv[2]
        extension = sys.argv[3]
    elif (len(sys.argv) == 3):
        sourcePath = os.getcwd()
        destinationPath = sys.argv[1]
        extension = sys.argv[2]
    else:
        sourePath = input('What is your Source Path?')
        destinationPath = input('What is your Destination Path?')
        extension = input('What is your extension to filter?')
    
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    print(sourcePath, destinationPath, extension)
    while True:
        MoveFilesBasedExtension(sourcePath, destinationPath, extension);
        time.sleep(1)
