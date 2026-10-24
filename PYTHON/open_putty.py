import subprocess
import os
import sys

paths = [
    r"C:\Program Files\PuTTY\putty.exe",
]

putty_path = next((p for p in paths if os.path.exists(p)), None)

if not putty_path:
    print("Error: not found.")
    sys.exit(1)

ip_address = input("192.168.1.1: ").strip()

if not ip_address:
    print("Error: do not empty.")
    sys.exit(1)

command = [
    putty_path,
    "-ssh",
    "-P", "22",
    ip_address
]

subprocess.Popen(command)

print(f"PuTTY SSH connection has been started: {ip_address}")
