import os
import shutil

from_dir = 'C:/Users/pangp/Downloads'
to_dir = 'C:/Users/pangp/OneDrive/Desktop/Document_Files_Folder'
list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)
    string = f'{name} {extension}'

    print(string)
    if(extension == ''):
        continue
    if(extension in [".txt", ".doc", ".docx", ".pdf"]):
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + 'Document_Files'
        path3 = to_dir + '/' + 'Document_Files' + '/' + i

        if(os.path.exist(path2)):
            print('moving the file', f'"{file}"', 'from', f'"{path1}"', 'to', f'"{path3}"')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('moving the file', file, 'from', path1, 'to', path3)
            shutil.move(path1, path3)

