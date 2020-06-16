import os
import shutil

Location = os.getcwd() 
TxtLocation = Location + '/PeopleTxt/'
JpgLocation = Location + '/PeopleJpg/'
TxtFile = os.listdir(TxtLocation)
JpgFile = os.listdir(JpgLocation)
FileNum = len(TxtFile)

SaveTxt = Location + '/PeopleTxt2/'
SaveJpg = Location + '/PeopleJpg2/'

for i in range(0, FileNum):
    a = TxtFile[i]
    b = a.replace('.txt', '') + '.jpg'
    shutil.copy2(TxtLocation + a, SaveTxt + '%d.txt'%i)
    shutil.copy2(JpgLocation + b, SaveJpg + '%d.jpg'%i)
