import os 

jpgLocation = os.getcwd() + '/PeopleJpg2/'
jpgFileList = os.listdir(jpgLocation)
jpgNum = len(jpgFileList)
txtfile = os.getcwd() + '/jpgLocation.txt'

for i in range(0, jpgNum):
    a = jpgLocation + jpgFileList[i] + '\n'
    with open(txtfile, mode='a') as f:
        f.write(a)
