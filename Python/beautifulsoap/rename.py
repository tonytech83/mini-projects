import os

PATH = "./output"
EXTENSION = ".html"

files = os.listdir(PATH)

def change_file_extension(file):
  file_path = os.path.join(PATH, file)
  pre, ext = os.path.splitext(file_path)
  os.rename(file_path, pre + EXTENSION)

for file in files:
  change_file_extension(file)