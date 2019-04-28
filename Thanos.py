import os
import random
import shutil

def thanos(dir_path):
    files = os.listdir(dir_path)
    sample = random.sample(files, len(files) // 2)
    for each in sample:
        file_path = os.path.join(dir_path, each)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except PermissionError as e:
            pass


print("=========start==========")
path = input("choose an earch(dir), null is now folder")
if path == '':
    path = os.getcwd()
flag = input('press y to start , other to exit')
if flag == 'y':
    thanos(path)
    print("==========finish===========")
else: 
    print("========exit========")