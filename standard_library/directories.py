from pathlib import Path

path = Path("modules")
# We can
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# Search Files
for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir()]
print(paths)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# Search recursively
path.glob("*.*")  # all files
path.glob("**/*.*")  # all files
path.glob("*.py")
path.rglob("*.py")  # busca recursivamente

py_files = [p for p in path.rglob("*.py")]
print(py_files)
