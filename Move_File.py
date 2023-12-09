import os
import shutil

from_dir = "C:/Users/seanl/Downloads"
to_dir = "C:/Users/seanl/OneDrive/Desktop/Coding/Sean Code/PRO/Projects 102+/Project-102 AUTOMATE_FILE_SEGREGATION/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name, ext = os.path.splitext(filename)
    
    if ext == "":
        continue
    if ext in [ ".txt", ".doc", ".docx", ".txt"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "Document_Files"
        path3 = path2 + "/" + filename

        if os.path.exists(path2):
            print("Moving " + filename + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving", filename + "...")
            shutil.move(path1, path3)