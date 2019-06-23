import cv2
import os
import sys

portrait = False
try:
    portrait = sys.argv[1] == 'p'
except:
    pass

sizes = [{'3,5 inch iPhone 3 4': (640, 960)},
{'4 inch iPhone 5': (640, 1136)},
{'4,7 inch iPhone 6 7 8': (750, 1334)},
{'5,5 inch iPhone 6 7 8 Plus': (1242 , 2208)},
{'5,8 inch iPhone X': (1125 , 2436)},
{'6,5 inch iPhone Xs Max': (1242 , 2688)},
{'9,7 inch iPad (Air and Mini Retina)': (1536 , 2048)},
{'10,5 inch iPad (Air and Mini Retina)': (1668 , 2224)},
{'11 inch iPad Pro': (2048 , 2732)},
]

def resizeFile(file, dimension):
    if portrait:
        resized =  cv2.resize(file, dimension, interpolation = cv2.INTER_AREA)
    else:
        resized =  cv2.resize(file, (dimension[1],dimension[0]), interpolation = cv2.INTER_AREA)
    return resized

def createDir(path):
    try:  
        os.mkdir(path)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory for %s " % path)

directory = os.fsencode('.')

filesToSave = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('.png') or filename.endswith('.jpg'):
        filesToSave.append(filename)

for sizeData in sizes:
    key = next(iter(sizeData))
    createDir(key)
    for imageFileName in filesToSave:
        newSizeTuple = sizeData[key]
        fileNameParts = imageFileName.split('.')
        extension = fileNameParts[1]
        onlyFileName = fileNameParts[0]
        imgToResize = cv2.imread(imageFileName, cv2.IMREAD_UNCHANGED)
        newSizeImg = resizeFile(imgToResize, newSizeTuple)
        nameToSave = os.path.join(key,onlyFileName + '.' + extension)
        cv2.imwrite(nameToSave,newSizeImg)

print('done!')




