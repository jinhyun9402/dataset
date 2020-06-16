import os

LoadLocation = '/home/robotheli/YOLOPerson/YoloTxt/'
FileNum = len(os.listdir(LoadLocation))
FileList = os.listdir(LoadLocation)
SaveLocation = '/home/robotheli/YOLOPerson/PeopleTxt/'

for i in range(0, FileNum):
    count = 0
    FileName = FileList[i]
    LoadFileLocation = LoadLocation + FileName

    with open(LoadFileLocation, mode='r') as f1:
        LineNum = len(f1.readlines())

    with open(LoadFileLocation, mode='r') as f2:
        for j in range(0,LineNum):
            a = f2.readline()
            if a[0] == '0':
                SaveFileLocation = SaveLocation + FileName
                with open(SaveFileLocation, mode='a') as f3:
                    f3.write(a)
            else:
                count = count + 1
        print(LineNum)

    if count == LineNum:
        print(FileName)
        print(count)
        JPGFile = FileName.replace('.txt', '') + '.jpg'
        JPGFileLocation = '/home/robotheli/YOLOPerson/PeopleJpg/' + JPGFile
        if os.path.isfile(JPGFileLocation):
            os.remove(JPGFileLocation)
            print('delete')

