import os
import shutil

source = input("ENTER SOURCE FOLDER NAME ")
destination = input("ENTER DESTINATION FOLDER NAME ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source + file), destination)