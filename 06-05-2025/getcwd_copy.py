import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "demo.txt")

with open(file_path, "w") as f:
    f.write("This file is created next to the script.")
