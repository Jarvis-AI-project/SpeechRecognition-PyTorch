import pydub
import multiprocessing as mp
import os


#read the folder for files
folder_path = str(input("Enter the cv-corpus-clips folder path: "))
lst_mp3 = os.listdir(folder_path)
count_mp3 = 0
for i in lst_mp3:
    if i.endswith('.mp3'):
        count_mp3 += 1
    else:
        continue
print('No of mp3 files found: ', count_mp3)