from pydub import AudioSegment
# import multiprocessing as mp
import threading as th
import os
from time import sleep
from time import time
# import argparse

# max_processes = 100
max_threads = 400
current_time = time()
# read the folder for files
# folder_path = str(input("Enter the cv-corpus-clips folder path: "))
# wave_path = str(input("Enter the output folder path: "))
folder_path = r"clips_test"
wave_out_path = r"wav_audio_dataset"
lst_files = os.listdir(folder_path)
count_mp3 = 0
index = 1


for i in lst_files:
    if i.endswith('.mp3'):
        count_mp3 += 1

    else:
        continue
print('Total number of files in the folder: ', len(lst_files))
print(".mp3 files found: ", count_mp3)


# def temp():
#     r = 9542358932693*9295239632
#     return r


def convert(mp3_path, wave_path):
    # print(mp3_path)
    # print(wave_path)
    mp3 = AudioSegment.from_mp3(mp3_path)
    mp3.export(wave_path, format="wav")


if __name__ == '__main__':
    # print('No of .mp3 files found: ', count_mp3)
    for mp3 in lst_files:
        if mp3.endswith('.mp3'):
            mp3_path = folder_path + '\\' + mp3
            wave_path = wave_out_path + '\\' + mp3.replace('.mp3', '.wav')
            print("converting file " + str(index) + "/" + str(count_mp3) + " to wav" +
                  '\t \t' + 'Time passed: ', round(time() - current_time, 2), 'seconds', end="\r")
            # print('Time passed: ', time() - current_time, 'seconds', end='\r')
            index += 1

            while True:
                # mp.Process(target=temp).start()
                # th.Thread(target=temp).start()

                # print('{} processes are running',len(mp.active_children()))

                # if len(mp.active_children())<max_processes:
                # print(len(th.enumerate()))
                if len(th.enumerate()) < max_threads:
                    # print(mp.active_children())
                    # p = mp.Process(target=convert, args=(mp3_path, wave_path))
                    p = th.Thread(target=convert, args=(mp3_path, wave_path))
                    p.start()
                    break
                else:
                    print('-'*50)
                    print('Waiting for a thread to finish...')
                    # print('Waiting for a process to finish...')
                    # print('Active processes: ', mp.active_children())
                    print('Active threads: ', len(th.enumerate()))
                    # print(mp3)
                    print('-'*50)
                    sleep(.5)

        else:
            print("'{}' not a mp3 file".format(mp3))

    print("Congratulations '{}' files have been successfully converted to wave in '{}' seconds".format(index-1, round(time() - current_time, 2)))
    print('Conversion Speed: "{}" files per second: '.format(round((index-1)/(time() - current_time), 2)))