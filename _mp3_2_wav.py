from pydub import AudioSegment
import multiprocessing as mp
import os
from time import sleep

max_processes = 100

#read the folder for files
folder_path = str(input("Enter the cv-corpus-clips folder path: "))
wave_path = str(input("Enter the output folder path: "))
lst_mp3 = os.listdir(folder_path)
count_mp3 = 0
for i in lst_mp3:
    if i.endswith('.mp3'):
        count_mp3 += 1
    else:
        continue
print('No of .mp3 files found: ', count_mp3)

class mp3_2_wave:
    def __init__(self):
        #nothing to do here
        pass
        
    def convert(self,mp3_path, wave_path):
        mp3 = AudioSegment.from_mp3(mp3_path)
        mp3.expoet(wave_path, format="wav")
        
if __name__ == '__main__':
    cvt = mp3_2_wave()
    for mp3 in lst_mp3:
        if mp3.endswith('.mp3'):
            mp3_path = folder_path + '/' + mp3
            wave_path = wave_path + '/' + mp3.replace('.mp3', '.wav')
            while True:
                if mp.active_children() < max_processes:
                    p = mp.Process(target=cvt.convert, args=(mp3_path, wave_path))
                    p.start()
                    p.join()
                else:
                    # print('Waiting for a process to finish...')
                    print('Active processes: ', mp.active_children())
                    print(mp3)
                    print('-'*50)
                    sleep(.5)
                
        else:
            print("{} not a mp3 file", mp3)