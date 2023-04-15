from pathlib import Path
from time import ctime

import shutil

path = Path("modules/app.py")
# We can
# path.exist()
# path.rename("__app__.py")
# path.unlink()  # delete file
# path.stat()  # get information about the file

print(path.stat())
print(ctime(path.stat().st_ctime))  # read time for humans understanding

# Reading data from the files
path.read_bytes()  # retunrs the content of the file as bytes
path.read_text()  # return the conten of the file as a string
print(path.read_text())

# Write text
path.write_text("Ok")
path.write_bytes("")  # write bytes

# We can copy the information of a file and past to other location like this
source = Path("modules/app.py")
target = Path()  # current folder

target.write_text(source.read_text())

# Best practice to copy info to anoter file
# import shutil
shutil.copy(source, target)

# We can get information of the file usein "open" function
# With "open" function we'll have to specify the file name, the mode
# save in an object and then close the file,

file = open("paths.py", "r")

# Best practice is using with
with open("paths.py", "r") as file:
    pass
