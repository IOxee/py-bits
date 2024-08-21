import os
import shutil

def zip_and_delete_folders(path):
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            zip_file = os.path.join(root, f"{dir_name}.zip")
            shutil.make_archive(zip_file.replace('.zip', ''), 'zip', dir_path)
            shutil.rmtree(dir_path)

path_to_your_directory = './'
zip_and_delete_folders(path_to_your_directory)
