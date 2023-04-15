from pathlib import Path

"""
# On Windows we can use
Path("C:\\Program Files\\Microsoft")
# Or
Path(r"C:\Program Files\Microsoft")
# In Mac or Linux we can use
Path("/usr/local/bin")
# We can use a Path object that represents the curent folder
Path()
# We can use a relative path startin from the current folder then acces to sub folders
Path("sub_folder/__init__.py")
# We can conbine tow paths
Path() / Path("sub_folder/__init__.py")
# We can conbine paths with strings
Path() / "ecommers" / "__init__.py"
# We can get the home directory of the current user
Path().home()
"""

path = Path("sub_folder/__init__.py")
# We can check if the path exists, is file, the name
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)  # file name  with out extention
print(path.suffix)  # extention of the file
print(path.parent)  # name of the parent
# We can create new path in the same path, but the file doesn't exist
path2 = path.with_name("fiele.txt")
path2 = path.with_suffix(".txt")  # we can change the sufix
print(path.absolute)  # obtenemos el path absolute
