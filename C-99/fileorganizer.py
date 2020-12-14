import os
import shutil

path = input("enter the name of the dirctory that is to be sorted by this computer ")
list_of_file = os.listdir(path)
for file in list_of_file:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)