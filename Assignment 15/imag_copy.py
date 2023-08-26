import os
import shutil

cwd = os.getcwd()
files = os.listdir()
path = cwd + "\img"
pas_files = ["jpeg", "jpg", "png", "gif"]

if "img" not in files:
    os.mkdir(path)

for i in files:
    if "." in i:
        for j in pas_files:
            if i.split(".")[1] == j:
                shutil.copy(i, path)