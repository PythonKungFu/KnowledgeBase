import os


directory = 'path/to/dir'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.txt'):
            print(os.path.join(root, file))
