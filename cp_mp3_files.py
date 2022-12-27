import threading as th
import os
import time
max_threads = 50

# read master folder
master_folder = r'D:\cv-corpus-12.0-2022-12-07\en\clips'
destination_folder = r"C:\cv-corpus-12.0-2022-12-07\en\clips"
lst_files = os.listdir(master_folder)
# global skip, index
skip, index = 0, 0

print("Total number of files in the folder: ", len(lst_files))

# def copy(source, destination):
#     command = "xcopy {} {}".format(source, destination)
#     return command


def copy_file(file_name):
    if os.path.exists(destination_folder+'\\'+file_name):
        global skip
        skip += 1
        return
    command = command = "xcopy {} {}".format(
        master_folder+'\\'+file_name, destination_folder)
    while True:
        if len(th.enumerate()) < max_threads:
            th.Thread(target=os.system, args=(command,)).start()
            global index
            index += 1
            return
        else:
            time.sleep(0.1)


def status():
    time.sleep(3)
    while True:
        print("Files copied: '{}' | Files Skipped: '{}'".format(
            index, skip), end='\r')


th.Thread(target=status).start()

for i in lst_files:
    if i.endswith('.mp3'):
        copy_file(i)
    else:
        print("'{}'Not an mp3 file".format(i))
