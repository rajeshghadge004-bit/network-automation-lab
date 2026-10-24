import subprocess
import os
import sys

putty_path = r"C:\Program Files\PuTTY\putty.exe"

if os.path.exists(putty_path):
    subprocess.Popen([putty_path])
    print("PuTTY successfully opened!")
else:
    print("PuTTY not exit. Need to check Installation path .")
    sys.exit(1)
