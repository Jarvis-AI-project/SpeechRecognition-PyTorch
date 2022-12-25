from pydub import AudioSegment
import multiprocessing as mp
import os
from time import sleep
# import argparse

max_processes = 100

#read the folder for files
# folder_path = str(input("Enter the cv-corpus-clips folder path: "))
# wave_path = str(input("Enter the output folder path: "))
folder_path = r"clips_test"
wave_out_path = r"wav_audio_dataset"
lst_mp3 = os.listdir(folder_path)
count_mp3 = 0
for i in lst_mp3:
    if i.endswith('.mp3'):
        count_mp3 += 1
    else:
        continue


def temp():
    r=9542358932693*9295239632
        
def convert(mp3_path, wave_path):
    # print(mp3_path)
    # print(wave_path)
    mp3 = AudioSegment.from_mp3(mp3_path)
    mp3.export(wave_path, format="wav")
        
if __name__ == '__main__':
    print('No of .mp3 files found: ', count_mp3)
    for mp3 in lst_mp3:
        if mp3.endswith('.mp3'):
            mp3_path = folder_path + '\\' + mp3
            wave_path = wave_out_path + '\\' + mp3.replace('.mp3','.wav')
            while True:
                mp.Process(target=temp).start()
                
                # print('{} processes are running',len(mp.active_children()))
                
                if len(mp.active_children())<max_processes:
                    # print(mp.active_children())
                    p = mp.Process(target=convert, args=(mp3_path, wave_path))
                    p.start()
                    break
                else:
                    # print('-'*50)
                    print('Waiting for a process to finish...')
                    # print('Active processes: ', mp.active_children())
                    # print(mp3)
                    # print('-'*50)
                    sleep(.5)
                
        else:
            print("{} not a mp3 file", mp3)