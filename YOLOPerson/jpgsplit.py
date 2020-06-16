import os
import shutil

TxtLocation = '/home/robotheli/YOLOPerson/YoloTxt/'
ListTxt = os.listdir(TxtLocation)
ListTxtNum = len(ListTxt)
LoadJPG = '/home/robotheli/YOLOPerson/COCOjpg/'
SaveJPG = '/home/robotheli/YOLOPerson/PeopleJpg/'

for i in range(0, ListTxtNum):
    Txtfile = ListTxt[i]
    LoadJPGfile = LoadJPG + Txtfile.replace('.txt', '') + '.jpg'
    SaveJPGfile = SaveJPG + Txtfile.replace('.txt', '') + '.jpg'
    shutil.copy2(LoadJPGfile, SaveJPGfile)
