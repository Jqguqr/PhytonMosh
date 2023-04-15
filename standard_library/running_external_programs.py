import subprocess

# We can execute comands and get information about
"""
completed = subprocess.run(["ls", "-l"],
                           capture_output=True,
                           text=True)
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)
"""

# We can execute another python programs
try:
    completed = subprocess.run(["python3", "app.py"],
                               capture_output=True,
                               text=True,
                               check=True)  # con este parametro se levanta una exepcion automaticamente si falla el comando
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
