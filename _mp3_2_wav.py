from pydub import AudioSegment
# import multiprocessing as mp
import threading as th
import os
import sys
from time import sleep
from time import time
# import argparse

# max_processes = 100
max_threads = 400
current_time = time()
# read the folder for files
# folder_path = str(input("Enter the cv-corpus-clips folder path: "))
# wave_path = str(input("Enter the output folder path: "))
folder_path = "clips_test"
wave_out_path = "wav_audio_dataset"
lst_files = os.listdir(folder_path)
count_mp3 = 0
index = 1

# make wav_audio_dataset folder if it doesn't exist
if not os.path.exists(wave_out_path):
    print("Creating wav_audio_dataset folder")
    os.mkdir(wave_out_path)
else:
    print("wav_audio_dataset folder already exists")

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
    try:
        # print(mp3_path)
        # print(wave_path)
        mp3 = AudioSegment.from_mp3(mp3_path)
        mp3.export(wave_path, format="wav")
    except OSError as e:
        print(e)
        print("OS Error")
        sys.exit(1)


if __name__ == '__main__':
    # print('No of .mp3 files found: ', count_mp3)
    for mp3 in lst_files:
        if mp3.endswith('.mp3'):
            mp3_path = folder_path + '\\' + mp3
            wave_path = wave_out_path + '\\' + mp3.replace('.mp3', '.wav')
            print("converting file " + str(index) + "/" + str(count_mp3) + " to wav" + '\t \t' +
                  'Time passed: ', round(time() - current_time, 2), 's' + '\t \t' +
                  'Time remaining: ', round((time() - current_time) * (count_mp3 - index) / index, 2), 's', end='\r')
            # print('\r\r\r')
            # print('Time passed: ', time() - current_time, 'seconds', end='\r')
            index += 1
            sleep(.001)

            while True:
                # mp.Process(target=temp).start()
                # th.Thread(target=temp).start()

                # print('{} processes are running',len(mp.active_children()))

                # if len(mp.active_children())<max_processes:
                # print(len(th.enumerate()))
                if len(th.enumerate()) < max_threads:
                    # print(mp.active_children())
                    # p = mp.Process(target=convert, args=(mp3_path, wave_path))
                    th.Thread(target=convert, args=(
                        mp3_path, wave_path)).start()
                    break
                else:
                    sleep(1)
                    # print('-'*50, end = '\r')
                    # print('\n')
                    # print('Waiting for a thread to finish...', end='\r')
                    # print('Waiting for a process to finish...')
                    # print('Active processes: ', mp.active_children())
                    # print('Active threads: ', len(th.enumerate()), end='\n\n')
                    # print(mp3)
                    # print('-'*50, end = '\r')

        else:
            print("'{}' not a mp3 file".format(mp3))

    print("Congratulations '{}' files have been successfully converted to wave in '{}' seconds".format(
        index-1, round(time() - current_time, 2)))
    print('Conversion Speed: "{}" files per second'.format(
        round((index-1)/(time() - current_time))))

    # remove wav_audio_dataset folder if it exists
    if len(th.enumerate()) > 0:
        print('Waiting for threads to finish', end='\r')
        sleep(1)
    os.system('rmdir /s /q "{}"'.format(wave_out_path))
    print('wav_audio_dataset folder removed')
