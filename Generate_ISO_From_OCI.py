import os
import subprocess
from datetime import datetime
import pycdlib

def create_iso_from_directory(source_dir, iso_path):
    iso = pycdlib.PyCdlib()
    iso.new(rock_ridge='1.09', joliet=True)
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            iso_path_in_iso = '/' + os.path.relpath(file_path, source_dir).replace('\\', '/')
            iso.add_file(file_path, iso_path_in_iso)
    iso.write(iso_path)
    iso.close()
    print(f"ISO creada exitosamente en {iso_path}")

download_path = input("Enter the path to the existing image file (.img): ")
download_path = os.path.abspath(download_path)
if not os.path.isfile(download_path):
    print(f"El archivo {download_path} no existe.")
else:
    time = datetime.now().strftime('%Y%m%d_%H%M%S')
    iso_path = f'bootable_image_{time}.iso'
    mount_dir = "mnt_dir"

    if not os.path.exists(mount_dir):
        os.makedirs(mount_dir)

    wsl_download_path = subprocess.run(['wsl', 'wslpath', download_path], capture_output=True, text=True).stdout.strip()
    wsl_mount_dir = subprocess.run(['wsl', 'wslpath', os.path.abspath(mount_dir)], capture_output=True, text=True).stdout.strip()

    print(f"WSL download path: {wsl_download_path}")
    print(f"WSL mount dir: {wsl_mount_dir}")

    mount_command = f"wsl sudo mount -o loop {wsl_download_path} {wsl_mount_dir}"
    result = subprocess.run(mount_command, shell=True)
    if result.returncode != 0:
        print("Error al montar la imagen con WSL")
    else:
        create_iso_from_directory(mount_dir, iso_path)

        umount_command = f"wsl sudo umount {wsl_mount_dir}"
        result = subprocess.run(umount_command, shell=True)
        if result.returncode != 0:
            print("Error al desmontar la imagen con WSL")

        os.rmdir(mount_dir)
