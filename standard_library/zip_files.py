from pathlib import Path
from zipfile import ZipFile

# Create zip file
"""
with ZipFile("files.zip", "w") as zip_file:
    for path in Path("modules").rglob("*.*"):
        zip_file.write(path)
"""

# Open zip file
with ZipFile("files.zip") as zip_file:
    print(zip_file.namelist())
    # read file inside zipFile
    info = zip_file.getinfo("modules/app.py")
    print(info.file_size)
    print(info.compress_size)
    # Extract all files
    zip_file.extractall("extract")
