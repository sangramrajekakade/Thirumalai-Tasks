import shutil
import os
source = os.listdir("//")
destination = ("/tmp/newtemp/")
for files in source:
    if files.endswith(".txt"):
        shutil.copy(files,destination)
