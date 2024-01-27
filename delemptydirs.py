import os
from sys import argv
from pathlib import Path

if len(argv) <= 1:
    print('Usage: delenv <directory>')
    exit()
path = Path(argv[1])

print('Deleting empty directiories\n')
count = 0

def remove_dir(dirpath: Path):
    contents = os.listdir(dirpath)
    for subdir in contents:
        subdir_path = dirpath.joinpath(subdir)
        if os.path.isdir(subdir_path):
            remove_dir(subdir_path)
    if len(os.listdir(dirpath)) == 0:
        abspath = dirpath.absolute()
        print(f'Delete {abspath}')
        os.rmdir(abspath)
        global count
        count += 1

for i in os.listdir(path):
    p = path.joinpath(i)
    if os.path.isdir(p):
        remove_dir(p)

print(f'Deleted {count} empty director{"y" if count == 1 else "ies"}')
